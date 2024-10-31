# Raspberry Pi Caldera Set Up

## Project Overview

This project aims to set up a Raspberry Pi to interface with Brilliant Frame glasses for local processing of AI models, using the Pi to handle Bluetooth communication with wearable devices. The following documentation details the step-by-step process I followed to set up the Raspberry Pi, install software, and establish communication between the Pi and the glasses.

## Hardware Requirements

This is the hardware that I used:

- Raspberry Pi 4 or 5 (we are using the 8GB RAM version)
- microSD Card (we are using a 256gb microSD)
- keyboard and mouse
- HDMI monitor
- Raspberry Pi power supply

## Initial Raspberry Pi Setup

### 1. Downloading Ubuntu Server

I started by downloading **Ubuntu Server (minimal)** from the [official Ubuntu website](https://ubuntu.com/download/raspberry-pi) to keep resource usage on the Pi low. Once I had the image, I flashed it onto a microSD card using the [Rasberry pi imager](https://www.raspberrypi.com/software/).

### 2. Booting the Raspberry Pi

Once the microSD card was ready, I inserted it into the Raspberry Pi and powered it on. I connected a monitor and keyboard initially to go through the standard setup process. During the setup, I created a username and password.

### 3. Updating the Raspberry Pi

After logging in for the first time, I updated the system by running:
```bash
sudo apt update
sudo apt upgrade -y
```

## Connecting to the Raspberry Pi via SSH

After setting up the Pi, I wanted to use it headless (without a monitor), so I enabled SSH access using `raspi-config`.

### 1. Enabling SSH

To enable SSH, I used the installed the `raspi-config` tool. Here's what I did:

1. Open the terminal on the Raspberry Pi and run the following command to open the configuration tool:

```bash
sudo apt install raspi-config -y
sudo raspi-config
```

2. Navigate to Interfacing Options and then select SSH.

1. Choose Enable when prompted to enable SSH access.

Exit the raspi-config tool and reboot the Raspberry Pi to apply the changes:
```bash
sudo reboot
```
### Finding the Pi’s IP Address
Once the Pi rebooted, I needed its IP address to connect via SSH. I found the IP address by running:

```bash
ip a
```

I used this command because `net-tools` did not come preinstalled.

### 3. Connecting via SSH
After finding the IP address, I used the following command from my laptop to connect to the Raspberry Pi via SSH:

```bash
ssh caldera@172.20.10.2
```

# Installing Python, Virtual Environment, and Dependencies

## Installing Python 3 and Pip
Since I was going to use Python to handle Bluetooth communication and other tasks, I installed Python 3, along with pip and the virtual environment package:

```bash
sudo apt install python3 python3-pip python3-venv -y
```

2. Setting Up a Virtual Environment
I created a virtual environment to isolate the Python dependencies for the project. Here's how I set it up:

```bash
mkdir ~/core-device
cd ~/core-device
python3 -m venv venv
```

Then, I activated the virtual environment:
```bash
source venv/bin/activate
```

3. Installing Required Python Packages
With the virtual environment active, I installed the necessary Python packages,
including Flask for handling the server logic and PyBluez for Bluetooth communication:
```bash
pip install flask pybluez
```
Setting Up Bluetooth Communication
1. Installing Bluetooth Utilities
To handle Bluetooth, I installed the required utilities:
```bash
sudo apt install bluetooth bluez libbluetooth-dev -y
```
2. Starting and Enabling the Bluetooth Service
I started the Bluetooth service and made sure it would automatically start on boot:
```bash
sudo systemctl start bluetooth
sudo systemctl enable bluetooth
```
## Still needs to be tested:
3. Pairing the Raspberry Pi with Brilliant Frame Glasses
I then used bluetoothctl to scan for and pair the Pi with the Brilliant Frame glasses:
```bash
sudo bluetoothctl
```
Inside the bluetoothctl interface, I ran the following commands:
```bash
power on                # Turned on the Bluetooth adapter
agent on                # Enabled the pairing agent
scan on                 # Scanned for nearby devices
```

Once I found the MAC address of the Brilliant Frame glasses, I paired them:
```bash
pair <MAC-address-of-glasses>
connect <MAC-address-of-glasses>
```
After pairing, I made sure to check the connection status:
```bash
info <MAC-address-of-glasses>
```
Testing Bluetooth Communication
1. Creating a Python Test Script
With the Bluetooth connection established, I wrote a Python script to test sending a message
from the Raspberry Pi to the Brilliant Frame glasses.
I created a file called bluetooth_test.py inside my project directory:
```python
import bluetooth

target_address = "<MAC-address-of-glasses>"

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((target_address, 1))
sock.send("Hello from Matthew!")
sock.close()

print("Message sent successfully!")
```
