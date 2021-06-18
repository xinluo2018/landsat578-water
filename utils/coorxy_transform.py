import pyproj

def coorxy_transform(srs_from, srs_to, x, y):
    """
    Transform coordinates from srs_from to srs_to
    input:
        srs_from and srs_to are EPSG number (e.g., 4326, 3031)
        x and y are x-coord and y-coord corresponding to srs_from and srs_to    
    return:
        x-coord and y-coord in srs_to 
    """
    srs_from = pyproj.Proj(int(srs_from))
    srs_to = pyproj.Proj(int(srs_to))
    return pyproj.transform(srs_from, srs_to, x, y, always_xy=True)

