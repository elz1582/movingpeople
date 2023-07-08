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


