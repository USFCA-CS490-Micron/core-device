# Raspberry Pi Bluetooth Chat Server with API Query Handling

### This code establishes a Bluetooth communication link where:

The Raspberry Pi acts as a Bluetooth server and waits for incoming connections.
Upon receiving a query from the Bluetooth client (e.g., glasses), the server sends the query to an external API and retrieves the response.
The response is displayed on the Raspberry Pi's terminal.

### Setup Requirements
- Raspberry Pi (with Bluetooth capability, e.g., Raspberry Pi 4 or 5).
- Python Libraries:
- bluetooth: Use the PyBluez library.
- requests: Install this library to enable HTTP requests to the API.
- Python 3: Ensure Python 3.x is installed on your Raspberry Pi.

## Install PyBluez for Bluetooth functionality
```bash
sudo apt update
sudo apt install python3-pip -y
pip3 install pybluez
```

## Install requests for making API calls
```bash
pip3 install requests
```

### Project Structure
- pi_server.py: The main script that runs the Bluetooth server, receives queries, makes an API call, and displays the response.
- process_query(query): This function in the script is responsible for sending the query to an API endpoint and retrieving the response.
- init_server(): Initializes the Bluetooth server, listens for incoming connections, and sets up the Bluetooth service.
- main(): Starts the server, manages incoming queries, and handles responses in a loop.

### Running the Code
Start the Server on the Raspberry Pi:

```bash
python3 pi_server.py
```

#### Waiting for Client Connection:

The server will display "Searching for connection..." until a client device attempts to connect.

#### Connect to the Raspberry Pi:

Use bluetoothctl on a Linux machine or any Bluetooth terminal app.

#### Pair and connect to the Raspberry Pi.

Restart the Bluetooth service if connections fail:

```bash
sudo systemctl restart bluetooth
```
