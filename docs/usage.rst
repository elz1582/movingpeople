Usage
=====

.. _installation:

Installation
------------

To use movingpeople, first install it using pip:

.. code-block:: console

   (.venv) $ pip install movingpeople


.. function:: generate_route(Gp, start_time, origin_node, destination_node, walk_speed=1.4, frequency="30s")

   Creates a DataFrame of evenly spaced points from an origin to a destination in a graph network.

   :param Gp: MultiDiGraph
      Graph network representing a geographic network of routes
   :param start_time: str
      Starting time at the origin point of the route
      Example: '2015-02-26 21:00:00'
   :param origin_node: int
      Node ID from OpenStreetMap
   :param destination_node: int
      Node ID from OpenStreetMap
   :param walk_speed: float, optional
      Walking speed measured in meters per second (default: 1.4)
   :param frequency: str, optional
      Time interval for sampling location points along a route (default: "30s")

   :return: gdf (DataFrame)
      Shapely Points with continuous timestamps along a route

.. function:: generate_routes(Gp, time_from, time_until=None, time_strategy="fixed", route_strategy="many-many", origin_destination_coords=None, total_routes=1, walk_speed=1.4, frequency="1s")

   Creates a DataFrame of evenly spaced points from randomly generated origins to destinations in a graph network.

   :param Gp: MultiDiGraph
      Graph network representing a geographic network of routes
   :param time_from: str
      Timestamp of the earliest start time possible
      Example: '2015-02-26 21:00:00'
   :param time_until: str, optional
      Timestamp of the latest start time possible (default: None)
      Example: '2015-02-26 22:00:00'
   :param time_strategy: str, optional
      Determines whether the route start time is fixed or randomised. If randomised, 'time_until' must be defined (default: "fixed")
   :param route_strategy: str, optional
      Determines fixed or randomised origin and destination locations. Options are 'many-many', 'one-one', 'one-many', 'many-one' (default: "many-many")
   :param origin_destination_coords: list, optional
      Coordinates in EPSG:4326 used if the route_strategy is 'one-one', 'one-many', 'many-one' for defining the origin or destination (default: None)
      Example: [51.499127, -0.153522, 51.498523, -0.155438] when route_strategy is 'one-one'
   :param total_routes: int, optional
      Total number of individual routes (default: 1)
      Example: 5
   :param walk_speed: float, optional
      Walking speed measured in meters per second (default: 1.4)
      Example: 1.4
   :param frequency: str, optional
      Time interval for sampling location points along a route (default: "1s")
      Example: '30s'

   :return: df (DataFrame)
      Shapely Points with continuous timestamps along multiple routes

.. function:: visualise_route(dataset, height=400)

   Creates a visualization of a route in a graph network.

   :param dataset: DataFrame
      DataFrame containing a geometry column of Shapely Points and IDs
   :param height: int, optional
      Height of the output map (default: 400)

   :return: map
      KeplerGL visualisation


.. function:: clip_routes_to_polygon(routes, polygon)

    Creates a DataFrame of routes that are clipped by a single polygon.

    :param routes: GeoDataFrame
        DataFrame containing route locations. See :func:`generate_routes` for information.
    :param polygon: GeoDataFrame
        Contains a 'geometry' column representing the clipping polygon.

    :return: GeoDataFrame
        A subset of routes that are clipped inside the input polygon.

    :raises AssertionError:
        If the input polygon is not a Shapely 'Polygon'.
        If the polygon GeoDataFrame doesn't have a column named 'geometry'.
        If the input routes GeoDataFrame doesn't have a 'geometry' column with Point geometries.


.. function:: get_entry_exit_times(clipped_routes)

    Gets the start and end times of unique routes.

    :param clipped_routes: GeoDataFrame
        DataFrame containing routes. Ideally used after :func:`clip_routes_to_polygon`.

    :return: DataFrame
        Start and end times for each unique route, along with their duration.

    :raises AssertionError:
        If the 'id' column is not found in the input clipped_routes.
        If the 'time' column is not found in the input clipped_routes.
        If the 'time' column in clipped_routes is not of datetime type.

.. toctree::
   Home