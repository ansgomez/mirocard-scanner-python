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

## License

BSD-3-Clause. Copyright (c) 2021-2022, Andres Gomez. See [LICENSE](LICENSE).
