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

The **OSI (Open Systems Interconnection)** model is a conceptual framework used to understand and implement network communication. It divides communication into seven distinct layers, each with specific roles and functions.

---

| **Layer Number** | **Layer Name**         | **Description**                                                                                   | **Examples**                          |
|-------------------|------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------|
| 7                 | **Application Layer** | Interfaces with user applications to provide network services like data transfer and resource sharing. | HTTP, FTP, SMTP, DNS, SSH            |
| 6                 | **Presentation Layer**| Translates, encrypts, and compresses data to ensure it is readable for the application layer.      | SSL/TLS, JPEG, GIF, ASCII            |
| 5                 | **Session Layer**     | Establishes, maintains, and terminates communication sessions between applications.               | NetBIOS, RPC, PPTP                   |
| 4                 | **Transport Layer**   | Ensures reliable delivery of data with error detection, retransmission, and flow control.         | TCP, UDP                             |
| 3                 | **Network Layer**     | Manages routing and forwarding of data across different networks.                                 | IP, ICMP, ARP, OSPF                  |
| 2                 | **Data Link Layer**   | Handles node-to-node communication, error detection, and framing of data packets.                 | Ethernet, Wi-Fi, PPP, MAC Address    |
| 1                 | **Physical Layer**    | Transmits raw binary data over the physical medium (e.g., cables, radio waves).                   | Ethernet cables, fiber optics, hubs  |

---