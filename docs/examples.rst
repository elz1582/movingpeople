Examples
=====

Here's a basic example to get you started with **movingpeople**:

.. code-block:: bash

    from movingpeople import visualise_route, generate_routes
    import osmnx as ox

    # Search query for a geographic area
    query = "City of Westminster"
    # Get the walking network for the query location
    G = ox.graph.graph_from_place(query, network_type="walk", simplify=True)
    # Project the graph to WGS84
    Gp = ox.project_graph(G, to_crs="4326")

    # To make two randomised routes
    two_routes = generate_routes(
                              Gp,
                              time_from="2015-02-26 21:42:53",
                              time_until=None,
                              time_strategy="fixed",
                              route_strategy="many-many",
                              origin_destination_coords=None,
                              total_routes=2,
                              walk_speed=1.4,
                              frequency="1s",
                              )

    # Visualise the results in keplerGL
    visualise_route(two_routes, 500)

In the example above, we first create a ``Graph`` object to define the transportation network. We then generate two routes which have the same start time however randomised origins and destinations.



Here's some basic examples to get you started with **movingpeople**. First you'll need to have a graph network read:

.. code-block:: bash
   from movingpeople import visualise_route, generate_routes

   import osmnx as ox

   # Search query for a geographic area
   query = "City of Westminster"
   # Get the walking network for the query location
   G = ox.graph.graph_from_place(query, network_type="walk", simplify=True)
   # Project the graph to WGS84
   Gp = ox.project_graph(G, to_crs="4326")

Now lets try making some synthetic route data with different parameters:

To make a single route with a randomised origin and destination and fixed start time:
.. code-block:: bash
   generate_routes(
                  Gp,
                  time_from="2015-02-26 21:42:53",
                  time_until=None,
                  time_strategy="fixed",
                  route_strategy="many-many",
                  origin_destination_coords=None,
                  total_routes=1,
                  walk_speed=1.4,
                  frequency="1s",
                  )

To make a single route with a randomised origin and destination and randomised start time between a range.
.. code-block:: bash
   generate_routes(
                  Gp,
                  time_from="2015-02-26 21:42:53",
                  time_until="2015-02-26 22:42:53",
                  time_strategy="fixed",
                  route_strategy="many-many",
                  origin_destination_coords=None,
                  total_routes=1,
                  walk_speed=1.4,
                  frequency="1s",
                  )

To make a single route with a fixed origin and randomised destination and randomised start time between a range.
.. code-block:: bash
   generate_routes(
                  Gp,
                  time_from="2015-02-26 21:42:53",
                  time_until="2015-02-26 22:42:53",
                  time_strategy="fixed",
                  route_strategy="one-many",
                  origin_destination_coords=[51.499127, -0.153522],
                  total_routes=1,
                  walk_speed=1.4,
                  frequency="1s",
                  )

To make a single route with a randomised origin and fixed destination and randomised start time between a range.
.. code-block:: bash
   generate_routes(
                  Gp,
                  time_from="2015-02-26 21:42:53",
                  time_until="2015-02-26 22:42:53",
                  time_strategy="fixed",
                  route_strategy="many-one",
                  origin_destination_coords=[51.499127, -0.153522],
                  total_routes=1,
                  walk_speed=1.4,
                  frequency="1s",
                  )

To make a single route with a fixed origin and destination and randomised start time between a range.
.. code-block:: bash
   generate_routes(
                  Gp,
                  time_from="2015-02-26 21:42:53",
                  time_until="2015-02-26 22:42:53",
                  time_strategy="fixed",
                  route_strategy="one-one",
                  origin_destination_coords=[51.499127, -0.153522, 51.498523, -0.155438],
                  total_routes=1,
                  walk_speed=1.4,
                  frequency="1s",
                  )

To make ten routes with a fixed origin and randomised destination and randomised start time between a range, with a walking speed of 2m/s.
.. code-block:: bash
   generate_routes(
                Gp,
                time_from="2015-02-26 21:42:53",
                time_until="2015-02-26 22:42:53",
                time_strategy="fixed",
                route_strategy="one-many",
                origin_destination_coords=[51.499127, -0.153522],
                total_routes=10,
                walk_speed=2,
                frequency="1s",
                )

.. toctree::
   Home 
   usage
   examples <self>