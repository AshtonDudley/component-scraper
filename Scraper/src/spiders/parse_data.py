import re

def parse_info(info):
    rep = []
    out = ["NULL","NULL","NULL",]
    for i in info:
        rep.append(i.strip())

    for i in rep:
        if re.search("MF([\S]*)$", i):
            out[0] = re.search(r"MF([\S]*)$",i)
        elif i == 'Manufacturer: Royal OHM':
            out[1] = "Royal OHM"
        elif re.search(r"^Resistan", i):
            out[2] =re.search(r"\d+.?", i).group()





parse_info(info = ['Manufacturer: Royal OHM', '\r\nManufacturer Part#: ', 'MF0W4FF100KA50', '\r\n', 'Datasheet: ', 'Click Here', '\r\nRoHS LEAD FREE', '\r\nHigh Performance Quality', '\r\nCopper Plated Wires', '\r\nLeads thickness: 0.54mm', '\r\nCapsule Dimensions: 2.5mm*6.8mm', '\r\nOverall Length: 52mm', '\r\n', 'Power (Watts) 0.25 (1/4 Watts)', '\r\nResistance in Ohms 1', '\r\nTolerance ±1%', '\r\nFeature Low noise, Low voltage coefficient', '\r\nResistor Type Metal Film'])