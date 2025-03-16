2017 - This is the Python/Django backend for an app, VisHere. The iOS app sends the GPS coordinates of the user to the server,
the server runs find_close_buildings from views.py to find the closest (currently random 10..35 I believe) buildings. Returns them as JSON.
Data taken from two different NYC Open Data platform DBs. Currently basic implementation/proof of concept.

Centroids are calculated based on the GIS data taken from NYC - most extreme corners of a given building are used to calculate centroid, which
is then used to find closest buildings to user's location.
