import osmnx as ox
from shapely.geometry import LineString, Point
import geopandas as gpd
import numpy as np
import keplergl
import random
import pandas as pd

import unittest
from ..src.movingpeople import (
    generate_route,
    generate_routes,
    visualise_route,
)

# Search query for a geographic area
query = "City of Westminster"
# Get the walking network for the query location
G = ox.graph.graph_from_place(query, network_type="walk", simplify=True)
# Project the graph to WGS84
Gp = ox.project_graph(G, to_crs="4326")


def test_():
    # To make a single randomised route
    single_route = generate_route(
        Gp, "2015-02-26 21:42:53", route_location="random", walk_speed=1.4
    )
