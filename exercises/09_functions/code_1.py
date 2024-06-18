with open("config_r1.txt") as f:
    found_ip = False
    for line in f:
        line = line.rstrip()
        if line.startswith("interface"):
            intf = line.split()[-1]
            found_ip = False
        elif line.startswith(" ip address"):
            ip = line.split()[-2]
            found_ip= True
        elif "!" in line and found_ip:
            print(intf, ip)

