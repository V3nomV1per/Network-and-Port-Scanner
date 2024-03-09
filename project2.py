import socket

def scan_port(host, port):
    """Scan a single port on the target host."""
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout of 1 second for connection attempt
        s.settimeout(1)
        # Attempt to connect to the target host and port
        result = s.connect_ex((host, port))
        # If connection was successful, the port is open
        if result == 0:
            print(f"Port {port} is open")
        # Close the socket
        s.close()
    except KeyboardInterrupt:
        print("\nExiting program.")
        exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        exit()
    except socket.error:
        print("Could not connect to server.")
        exit()

def get_user_input(prompt):
    """Prompt user for input."""
    while True:
        user_input = input(prompt)
        if user_input:
            return user_input

if __name__ == "__main__":
    # Prompt user for target host IP address
    host = get_user_input("Enter target host IP address: ")
    
    # Prompt user for port range
    port_range = get_user_input("Enter port range (e.g., '1-1024'): ")
    start_port, end_port = map(int, port_range.split("-"))
    
    print(f"Scanning ports {start_port}-{end_port} on host {host}...")
    
    # Scan ports in the specified range
    for port in range(start_port, end_port + 1):
        scan_port(host, port)