import yaml


command = "sh ip int br"
with open("devices.yaml") as f:
    devices = yaml.safe_load(f)
    r1 = devices[0]
    
print(r1)
