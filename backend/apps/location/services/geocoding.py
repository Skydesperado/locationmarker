from arcgis.gis import GIS
from arcgis.geocoding import geocode

gis = GIS()

def geocode_address(address):
    """
    Geocodes an Address Using The ArcGIS Geocoding Service

    Args:
        address (str): The Address To Geocode

    Returns:
        tuple: A Tuple Containing The Latitude and Longitude or (None, None) If Geocoding Fails
    """
    try:
        results = geocode(address)
        if results:
            location = results[0]["location"]
            return location["y"], location["x"]
    except Exception as e:
        print(f"Error during geocoding: {e}")
    
    return None, None
