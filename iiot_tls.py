import socket
import ssl
import time

# Server-side setup
def control_server():
    server_address = ('localhost', 8443)

    # Load server certificate and key
    server_cert = 'server_cert.pem'
    server_key = 'server_key.pem'

    # Create a TLS context
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=server_cert, keyfile=server_key)

    # Create a socket and wrap it with TLS
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as server_socket:
        server_socket.bind(server_address)
        server_socket.listen(5)
        print("Control server listening on port 8443...")

        with context.wrap_socket(server_socket, server_side=True) as tls_socket:
            while True:
                client_connection, client_address = tls_socket.accept()
                print(f"Connection from {client_address}")

                try:
                    # Receive and process data
                    while True:
                        data = client_connection.recv(1024).decode('utf-8')
                        if not data:
                            break
                        print(f"Received data: {data}")
                        client_connection.sendall("Data received securely.".encode('utf-8'))
                except Exception as e:
                    print(f"Error while processing client: {e}")
                finally:
                    # Properly shutdown the connection
                    client_connection.shutdown(socket.SHUT_RDWR)
                    client_connection.close()


# Client-side setup (IIoT Device)
def iiot_device():
    server_address = ('localhost', 8443)

    # Create a TLS context
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations('server_cert.pem')

    with socket.create_connection(server_address) as client_socket:
        with context.wrap_socket(client_socket, server_hostname='localhost') as tls_socket:
            print("Connected to control server via TLS.")
            try:
                for i in range(5):  # Simulating periodic sensor data
                    sensor_data = f"IIoT Sensor Data: Pressure={50 + i} PSI"
                    print(f"Sending data: {sensor_data}")
                    tls_socket.sendall(sensor_data.encode('utf-8'))

                    # Receive server acknowledgment
                    response = tls_socket.recv(1024).decode('utf-8')
                    print(f"Server response: {response}")
                    time.sleep(2)  # Simulate delay between transmissions
            except Exception as e:
                print(f"Error during communication: {e}")


# Run the simulation
if __name__ == "__main__":
    import multiprocessing

    # Create processes for server and client
    server_process = multiprocessing.Process(target=control_server)
    client_process = multiprocessing.Process(target=iiot_device)

    # Start server and client
    server_process.start()
    time.sleep(1)  # Ensure the server starts first
    client_process.start()

    # Wait for client to finish
    client_process.join()
    server_process.terminate()
