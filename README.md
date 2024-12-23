# Cyber-Physical Systems: Transport Layer Security and Industrial Internet of Things 
I wanted to learn how secure transport layer security (TLS) communcation is setup and used.  Moreover, being that I am studying cyber-physical systems (CPSs) and how to secure them, I aimed to make it incorporate a model demonstrating communication for an industrial internet of things (IIoT) device. 

The Python script models a secure TLS communication between an IIoT device (client) and a control server. The server listens for incoming TLS connections on port 8443, authenticates itself using a self-signed certificate, and securely exchanges data with clients. Upon receiving data from the client, the server prints the received message and sends an acknowledgment. The IIoT device (client) simulates a sensor that periodically sends encrypted sensor data (e.g., pressure readings) to the server over a TLS connection, ensuring the confidentiality and integrity of the data. After sending data, the client waits for a response from the server before closing the connection.

This script demonstrates the use of Python's `ssl` module to wrap standard TCP sockets with TLS encryption, providing secure data exchange between devices in industrial environments. It also includes error handling to manage connection issues and ensures that both client and server properly close the connection after communication.
 
## Transport Layer Security (TLS)
Transport Layer Security is a crypographic protocol that ensures secure communication over a network.  It is used to protect data transmitted between applications.  Without knowing, you have used it when browsing the web and establishing a secure implementation of HTTP using TLS.  Overall, TLS guarantees: 

- confientiality: data is encrypted to prevent unauthorized access,
- integrity: data is protected from tampering during transmission, 
- and authentication: verifies the identity of the communicating parties using certificates.

### How TLS Works - Using the OSI Model
TBD