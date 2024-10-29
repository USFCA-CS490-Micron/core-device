import bluetooth
import requests 
import sys

def init_server():
    """
    Initializes the Bluetooth server and waits for a connection from the client.

    This function sets up a Bluetooth socket on the Raspberry Pi, binds it to any available
    port, and listens for incoming connections. Once it connects, the function 
    advertises the service as "PiChatService" to allow communication. I have no idea if this will
    actually work because I have not tested it. :D 

    Returns:
        tuple: A tuple containing the client socket and server socket:
            - client_sock: The socket connected to the client (glasses).
            - server_sock: The server socket listening for connections.
    """
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(("", bluetooth.PORT_ANY))
    server_sock.listen(1)

    bluetooth.advertise_service(server_sock, "PiChatService",
                                service_classes=[bluetooth.SERIAL_PORT_CLASS],
                                profiles=[bluetooth.SERIAL_PORT_PROFILE])
    print("Searching for connection...")
    client_sock, address = server_sock.accept()
    print(f"Connected to {address}")
    return client_sock, server_sock

def process_query(query):
    """
    Processes a query received from the client by making an API call.

    This function sends the received query to an external API and retrieves the response. 
    It checks for a successful HTTP status code (200) and, if successful, parses the 
    JSON response for the result. If there is an error, it returns the error status code.

    Args:
        query (str): The query received from the client (glasses).

    Returns:
        str: The result from the API if successful, or an error message if not.
    """
    print(f"Received query from glasses: {query}")
    
    api_url = "chatgpt" 
    response = requests.get(api_url, params={"q": query})
    
    if response.status_code == 200:
        result = response.json().get("response", "No response found")
    else:
        result = f"Error: {response.status_code}"
    return result


def main():
    """
    Main function to start the Bluetooth server and handle continuous communication.

    This function initializes the Bluetooth server, waits for queries from the client, 
    processes each query by calling `process_query()`, and prints the response. The 
    conversation continues until the connection is closed or an error occurs.
    """
    client_sock, server_sock = init_server()
    
    try:
        while True:
            query = client_sock.recv(1024).decode("utf-8")
            
            response = process_query(query)
            
            print(f"Pi: {response}")
            
    finally:
        client_sock.close()
        server_sock.close()

if __name__ == "__main__":
    main()
