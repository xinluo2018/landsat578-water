from osgeo import ogr, gdal
import numpy as np

def mask_by_shp(path_raster, path_shp, path_output):
    """
    author: jinhua zhang, date: 2021.3.13
    description: generate/save mask file using the .shp file.
    input: 
        path_raster, path_shp, path_output: str
    retrun: 
        mask, np.array.
        a .tiff file written to the given path
    """
    raster,shp = gdal.Open(path_raster, gdal.GA_ReadOnly), ogr.Open(path_shp)
    x_res = raster.RasterXSize
    y_res = raster.RasterYSize
    layer = shp.GetLayer()
    targetDataset = gdal.GetDriverByName('GTiff').Create(path_output, x_res, y_res, 1, gdal.GDT_Byte)
    targetDataset.SetGeoTransform(raster.GetGeoTransform())
    targetDataset.SetProjection(raster.GetProjection())
    band = targetDataset.GetRasterBand(1)
    NoData_value = -9999
    band.SetNoDataValue(NoData_value)
    band.FlushCache()
    gdal.RasterizeLayer(targetDataset, [1], layer)
    mask = targetDataset.ReadAsArray(0, 0, x_res, y_res)
    mask = np.where(mask>0, 1, 0)
    return mask