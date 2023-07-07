import osmnx as ox
from shapely.geometry import LineString, Point
import geopandas as gpd
import numpy as np
import keplergl
import random
import pandas as pd

def generate_route(Gp, start_time, route_location='random', origin_destination_coords=None, walk_speed=1.4, frequency = '30s'):
    """
    Creates a DataFrame of evenly spaced points from an origin to a destination in a graph network.

    Parameters:
            Gp : MultiDiGraph
                Graph network representing a geographic network of routes
            start_time : str
                Starting time at the origin point of the route
                Example: '2015-02-26 21:00:00'
            route_location : str
                Whether route origin/destination are user-defined or randomised
            origin_destination: list
                List of coordinates used if origin/destination points are used defined. 
                Example: [origin_lon, origin_lat, dest_lon, dest_lat]
            walk_speed : float
                Walking speed measured in meters per second
            frequency: str
                Time interval for sampling location points along a route
                
    Returns:
            gdf (DataFrame): Shapely Points with continuous timestamps along a route
    """
    
    # Checking theres a valid route_location
    assert route_location in ['random', 'fixed'], "Invalid input, available inputs are 'random' or 'fixed'."
    # Checking there is more than one node in the network
    assert len(list(Gp.nodes)) != 1, "Graph network only contains one node."

    
    if route_location == 'random':
        # Selecting random origin and destination nodes from the graph
        origin_node = list(Gp.nodes)[random.randint(0, len(list(Gp.nodes)))]
        destination_node = list(Gp.nodes)[random.randint(0, len(list(Gp.nodes)))]
    else:
        # Checking fixed coordinates are defined
        assert origin_destination_coords != None, "No origin or destination coordinates specified."
        # Checking all required origin/destination coordinates are present
        assert len(origin_destination_coords) == 4, "Invalid number of coordinates. Coordinates should follow the scheme [origin_lon, origin_lat, dest_lon, dest_lat]"

        # Selecting predefined origin and destination nodes from the graph
        origin_node = ox.nearest_nodes(Gp, origin_destination_coords[1], origin_destination_coords[0])
        destination_node = ox.nearest_nodes(Gp, origin_destination_coords[3], origin_destination_coords[2])

    # Find the shortest path between origin and destination
    route = ox.distance.shortest_path(Gp, origin_node, destination_node, weight='length', cpus=1)

    # Find the nodes along the shortest route
    nodes = ox.graph_to_gdfs(G, nodes=True, edges=False)
    route_nodes = nodes.loc[route]

    # Convert the CRS so route length is in meters
    gdf = gpd.GeoDataFrame(route_nodes, geometry='geometry', crs=4326)
    gdf = gdf.to_crs(epsg=3857)

    # Converting points to a LineString
    route_line = LineString(gdf['geometry'].tolist())
    # Creating an array of even spacing
    distances = np.arange(0, route_line.length, walk_speed)
    # Interpolate evenly spaced points along the LineString
    points = [route_line.interpolate(distance) for distance in distances]
    # Convert to a GeoDataFrame
    gdf = gpd.GeoDataFrame(geometry=points, crs=3857)
    # Add a continuous timestamp to each point along the route
    gdf['time'] = pd.date_range(start_time, freq=frequency, periods=len(gdf))

    return gdf

def generate_random_routes(Gp, time_from, time_until, route_location='random', origin_destination_coords=None, total_routes = 1, walk_speed = 1.4, frequency = '30s'):
    """
    Creates a DataFrame of evenly spaced points from an randomised origins to destinations in a graph network.

    Parameters:
            Gp : MultiDiGraph
                Graph network representing a geographic network of routes
            total_routes : int
                Total number of individual routes
                Example: 5
            time_from : str
                Timestamp of the earliest start time possible
                Example: '2015-02-26 21:00:00'
            time_until : str
                Timestamp of the latest start time possible
                Example: '2015-02-26 22:00:00'
            walk_speed : float
                Walking speed measured in meters per second
                Example : 1.4
            frequency : str
                Time interval for sampling location points along a route
                Example : '30s'
    Returns:
            df (DataFrame): Shapely Points with continuous timestamps along a multiple routes
    """

    # Creating an empty list
    route_dfs = []

    for i in range(total_routes):
        #Convert strings to datetime
        time_from = pd.to_datetime(time_from)
        time_until = pd.to_datetime(time_until)
        # Create a random start time
        random_date = time_from + (time_until - time_from) * random.random()

        # Use the generate_route function to output a route
        route = generate_route(Gp, random_date, route_location, origin_destination_coords, walk_speed, frequency)
        # Add a route ID
        route['id'] = i + 1
        # Append back to the list
        route_dfs.append(route)
    # Concatenate list elements into a DataFrame
    df = pd.concat(route_dfs, ignore_index=True)

    return df

def visualise_route(dataset, height = 400):
    """
    Creates a DataFrame of evenly spaced points from an randomised origins to destinations in a graph network.

    Parameters:
            dataset : DataFrame
                DataFrame containing a geometry column of Shapely Points and IDs
            height : int
                Height of the output map

    Returns:
            map : KeplerGL visualisation
    """
    
    # Checking if all relevant columns exist
    assert 'geometry' in dataset.columns, "'geometry' column not found."
    assert 'time' in dataset.columns, "'time' column not found."

    # Checking data types in columns are correct
    for geometry in dataset['geometry']:
        assert isinstance(geometry, Point), f"Invalid geometry type: {type(geometry)}"

    # Setting up a map
    map = keplergl.KeplerGl(height=height)
    # Adding the data points to the map
    map.add_data(data=dataset, name='Route Points')

    return map
