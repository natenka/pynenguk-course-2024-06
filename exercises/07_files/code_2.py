from pprint import pprint
import re


regex1 = r"(\d+) +(\S+) +\S+ +(\S+)"

def parse(filename):
    data = []
    with open(filename) as f:
        for line in f:
            m = re.search(regex1, line)
            if m:
                data.append(m.groups())
    return data




def parse(filename):
    data = []
    with open(filename) as f:
        all_file = f.read()
    m = re.finditer(regex1, all_file)
    for line_match in m:
        data.append(line_match.groups())
    return data


pprint(parse("CAM_table.txt"))
