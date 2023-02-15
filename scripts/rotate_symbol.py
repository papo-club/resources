import xml.etree.ElementTree as ET
from sys import argv
import math

mapperns = "http://openorienteering.org/apps/mapper/xml/v2"
ET.register_namespace("", mapperns)
ns = {"mapper": mapperns}

file = argv[1]
symbol_code = input("symbol code to rotate: ")
rotation = float(input("amount to rotate (in DEG): ")) * math.pi / 180

omap = ET.parse(argv[1])
root = omap.getroot()

symbol_id = root.find(f".//mapper:symbol[@code='{symbol_code}']", ns).attrib["id"]
symbols = root.findall(f".//mapper:object[@symbol={repr(symbol_id)}]", ns)
for symbol in symbols:
    try:
        old_rotation = float(symbol.attrib["rotation"])
        new_rotation = (old_rotation + rotation) % (2 * math.pi)
        symbol.set("rotation", f"{new_rotation:.5f}")
        print(f"{symbol_code}: {old_rotation} -> {new_rotation:.5f}")
    except KeyError:
        pass

omap.write(file, encoding="UTF-8", xml_declaration=True)