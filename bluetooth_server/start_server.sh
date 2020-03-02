python3 bluetooth_server.py "$(hcitool dev | tail -n1 | awk {'print($2)'})"
