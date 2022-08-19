#!/usr/bin/env python3

import sys
import geopandas as gpd

school_grounds = gpd.read_file("data/Public_School_Grounds.geojson")
streets = gpd.read_file("data/Street_Right_of_Way_Polygons.geojson")

