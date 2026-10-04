mirocard-scanner-python
=======================

Simple Python 3 scripts to detect MiroCard beacons on Linux (BlueZ).

| Script | Library | What it does |
|---|---|---|
| `mirocard-scanner.py` | [bluepy](https://github.com/IanHarvey/bluepy) | Scans for MiroCard beacons (MAC prefix `60:77:71`) and decodes temperature and humidity |
| `mirocard-discovery.py` | [gattlib](https://github.com/oscaracena/pygattlib) | Lists nearby BLE devices by name |

## mirocard-scanner.py

```
$ sudo apt-get install python3-pip libglib2.0-dev
$ sudo pip3 install bluepy
$ sudo python3 mirocard-scanner.py
```

Set `DEBUG = 1` in the script to print the raw payload bytes.

## mirocard-discovery.py

```
$ sudo apt-get install python3-pip libbluetooth-dev libboost-python-dev libglib2.0-dev
$ sudo pip3 install gattlib
$ sudo python3 mirocard-discovery.py
```

`mirocard-discovery.py` was previously published as
[mirocard-discovery-python](https://github.com/ansgomez/mirocard-discovery-python), now archived.

## MiroCard project

The MiroCard is a batteryless, light-powered BLE smart card, designed by Andres Gomez
(Miromico AG) and inspired by the
[Transient BLE Node](https://gitlab.ethz.ch/tec/public/employees/sigristl/transient_ble_node)
project developed at ETH Zurich. It was presented in:

> Andres Gomez. 2020. *Demo Abstract: On-Demand Communication with the Batteryless MiroCard.*
> In The 18th ACM Conference on Embedded Networked Sensor Systems (SenSys '20).
> [doi:10.1145/3384419.3430440](https://doi.org/10.1145/3384419.3430440)

Related repositories:

| Repository | Contents |
| --- | --- |
| [mirocard-hardware](https://github.com/ansgomez/mirocard-hardware) | Hardware: datasheet, schematics and Altium PCB project (MiroCard V2.0) |
| [mirocard-contiki-ng](https://github.com/ansgomez/mirocard-contiki-ng) | Firmware: Contiki-NG fork with the MiroCard platform and example applications |
| [miroreader-app](https://github.com/ansgomez/miroreader-app) | Android app to receive and display MiroCard beacons |
| **mirocard-scanner-python** (this repository) | Python scripts to scan for and decode MiroCard beacons (bluepy) and discover devices (gattlib) |
| [mirocard-scanner-mqtt](https://github.com/ansgomez/mirocard-scanner-mqtt) | Node.js bridge forwarding MiroCard beacons to an MQTT broker |
| [mirocard-scanner-influx](https://github.com/ansgomez/mirocard-scanner-influx) | Node.js bridge storing MiroCard beacons in InfluxDB |
| [mirocard-webid](https://github.com/ansgomez/mirocard-webid) | Web Bluetooth demo page for identification and sensor readout |
| [mirocard-postprocessing](https://github.com/ansgomez/mirocard-postprocessing) | Jupyter notebook to post-process RocketLogger power measurements |
| [mirocard-plotly](https://github.com/ansgomez/mirocard-plotly) | Plotly Dash web app visualizing a RocketLogger measurement |

## License

BSD-3-Clause. Copyright (c) 2021-2022, Andres Gomez. See [LICENSE](LICENSE).
