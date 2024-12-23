# tls-iiot
I wanted to learn how secure TLS communcation is setup and used.  Moreover, being that I am studying cyber-physical systems (CPSs) and how to secure them, I aimed to make it incorporate a model demonstrating communication for an industrial internet of things (IIoT) device. 

The Python script models a secure TLS communication between an IIoT device (client) and a control server. The server listens for incoming TLS connections on port 8443, authenticates itself using a self-signed certificate, and securely exchanges data with clients. Upon receiving data from the client, the server prints the received message and sends an acknowledgment. The IIoT device (client) simulates a sensor that periodically sends encrypted sensor data (e.g., pressure readings) to the server over a TLS connection, ensuring the confidentiality and integrity of the data. After sending data, the client waits for a response from the server before closing the connection.

This script demonstrates the use of Python's `ssl` module to wrap standard TCP sockets with TLS encryption, providing secure data exchange between devices in industrial environments. It also includes error handling to manage connection issues and ensures that both client and server properly close the connection after communication.
 
