import socket

# Define the range of ports to scan
for port in range(80, 91):  # Correct range includes 5005
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a timeout to avoid long waits
    
    # Attempt to connect to the port
    result = sock.connect_ex(("223.233.86.110", port))
    
    # Check the result and print the status of the port
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    
    # Close the socket
    sock.close()
