import shapefile
from shapely.geometry import Point, LineString, Polygon
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import json
import geojson


# create geojson file.
# credit : http://www-udc.ig.utexas.edu/external/plates/data.htm

# shp_path = "./input/ridge.shp"
# output_path = "./output/ridge.geojson"

# shp_path = "./input/transform.shp"
# output_path = "./output/transform.geojson"

shp_path = "./input/trench.shp"
output_path = "./output/trench.geojson"

src = shapefile.Reader(shp_path, encoding="utf-8")

# geometry.
shps = src.shapes()
# attribute.
recs = src.records()

with open(output_path, "w", encoding="utf-8") as w:
    feature_list = []
    for i, (s, r) in enumerate(zip(shps, recs)):
        points = s.points
        area_name = r[-1]
        parts = [i for i in s.parts] + [len(points) - 1]
        points_hole = [points[parts[i] : parts[i + 1]] for i in range(len(parts) - 1)]

        # create geometry.
        poly = geojson.Polygon(points_hole)
        attr = {"area_name": area_name}
        feature = geojson.Feature(geometry=poly, id=i, properties=attr)
        feature_list.append(feature)
    feature_collection = geojson.FeatureCollection(feature_list)
    w.write(json.dumps(feature_collection, indent=2))
