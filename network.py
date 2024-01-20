import socket
import json
from sheet_importer import pullexcel


HOST = "10.0.0.69"
PORT = 65432

commands = [
    ('A1', 6000), ('A2', 5750), ('A3', 5500), ('A4', 5250), ('A5', 5000), ('A6', 4750), ('B1', 4500), ('B2', 4250), ('B3', 4000), ('B4', 3750), ('B5', 3500), ('B6', 3250), ('C1', 3000), ('C2', 2750), ('C3', 2500), ('C4', 2250), ('C5', 2000), ('C6', 1750), ('D1', 1500), ('D2', 1250), ('D3', 1000), ('D4', 750), ('D5', 500), ('D6', 250), "STOP"
    ]
raw = json.dumps(commands)

def ot_send(data, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #print("Binding...")
        s.connect((host, port))
        #print("Bound.")
        s.sendall(bytes(raw, encoding="utf-8"))
        data = s.recv(1024)
        return data
        #print(f"Received {data}")

#ot_send(commands, HOST, PORT)

