import bluetooth

target_address = "<MAC-address-of-glasses>"

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((target_address, 1))

sock.send("Hello from Raspberry Pi!")
sock.close()
