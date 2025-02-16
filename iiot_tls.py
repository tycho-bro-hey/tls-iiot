import socket
import ssl
import time

'''
The following loads a server certificate and key,
creates a TLC context and a socket.  Then it is 
wrapped with TLS.
'''
def control_server():
    server_address = ('localhost', 8443)

    server_cert = 'server_cert.pem'
    server_key = 'server_key.pem'

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=server_cert, keyfile=server_key)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as server_socket:
        server_socket.bind(server_address)
        server_socket.listen(5)
        print("Control server listening on port 8443...")

        with context.wrap_socket(server_socket, server_side=True) as tls_socket:
            while True:
                client_connection, client_address = tls_socket.accept()
                print(f"Connection from {client_address}")

                try:
                    while True:
                        data = client_connection.recv(1024).decode('utf-8')
                        if not data:
                            break
                        print(f"Received data: {data}")
                        client_connection.sendall("Data received securely.".encode('utf-8'))
                except Exception as e:
                    print(f"Error while processing client: {e}")
                finally:
                    client_connection.shutdown(socket.SHUT_RDWR)
                    client_connection.close()


def iiot_device():
    server_address = ('localhost', 8443)

    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations('server_cert.pem')

    with socket.create_connection(server_address) as client_socket:
        with context.wrap_socket(client_socket, server_hostname='localhost') as tls_socket:
            print("Connected to control server via TLS.")
            try:
                for i in range(5): 
                    sensor_data = f"IIoT Sensor Data: Pressure={50 + i} PSI"
                    print(f"Sending data: {sensor_data}")
                    tls_socket.sendall(sensor_data.encode('utf-8'))

                    response = tls_socket.recv(1024).decode('utf-8')
                    print(f"Server response: {response}")
                    time.sleep(2)  # include delay between transmission
            except Exception as e:
                print(f"Error during communication: {e}")


'''
We start the simulation in main and start
the servce + client process.
'''

if __name__ == "__main__":
    import multiprocessing

    server_process = multiprocessing.Process(target=control_server)
    client_process = multiprocessing.Process(target=iiot_device)

    server_process.start()
    time.sleep(1)  
    client_process.start()

    client_process.join()
    server_process.terminate()
