#!/usr/bin/env python3
"""PyBluez ble example scan.py"""

from gattlib import DiscoveryService

service = DiscoveryService("hci0")

debug=False

while True:
    devices = service.discover(1)
    
    for address, name in devices.items():
        if(name is not None): 
            if ("BLE" in name):
                print("Name: {}, address: {}".format(name, address))
        if(debug == True):
            print("Name: {}, address: {}".format(name, address))
