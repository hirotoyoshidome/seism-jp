from typing import Any
import csv
import json


# create csv file that active volcanoes data at jma.
# credit : https://www.data.jma.go.jp/svd/vois/data/tokyo/STOCK/souran/appendix/active_volcanoes.pdf
# download zip from that link, unzip and http://ogre.adc4gis.com/ convert geojson then move convert.json file to input directory.

# format convert.json to geojson
filepath = "./input/convert.json"
output_path = "./output/volcanoes.geojson"
fil = open(filepath, "r")
data = json.load(fil)

with open(output_path, "w", encoding="utf-8") as w:
    w.write(json.dumps(data, indent=2))
