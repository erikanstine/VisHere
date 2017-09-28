This is the Python/Django backend for an app of mine, VisHere. The iOS app sends the GPS coordinates of the user to the server,
the server runs find_close_buildings to find the closest (currently random 10..35 I believe) buildings. Returns them as JSON.
Data taken from two different NYC Open Data platform DBs. Currently basic implementation/proof of concept.
