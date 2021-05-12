# from osgeo import gdal
# import numpy as np

# ### tiff image reading
# def readTiff(path_in):
#     '''
#     author: xin luo, date: 2021.4.11
#     return: 
#         img: numpy array, exent: tuple, (x_min, x_max, y_min, y_max) 
#         proj info, and dimentions: (row, col, band)
#     '''
#     RS_Data=gdal.Open(path_in)
#     im_col = RS_Data.RasterXSize  # 
#     im_row = RS_Data.RasterYSize  # 
#     im_bands =RS_Data.RasterCount  # 
#     im_geotrans = RS_Data.GetGeoTransform()  # 
#     im_proj = RS_Data.GetProjection()  # 
#     RS_Data = RS_Data.ReadAsArray(0, 0, im_col, im_row)  # 
#     x_min = im_geotrans[0]
#     x_max = x_min + im_geotrans[1] * im_col
#     y_max = im_geotrans[3]
#     y_min = y_max + im_geotrans[5] * im_row
#     extent = (x_min, x_max, y_min, y_max)

#     if im_bands > 1:
#         RS_Data = np.transpose(RS_Data, (1, 2, 0)).astype(np.float)  # 
#         return RS_Data,extent,im_geotrans,im_proj,im_row,im_col,im_bands
#     else:
#         return RS_Data,extent,im_geotrans,im_proj,im_row,im_col,im_bands

# ###  .tiff image write
# def writeTiff(im_data, im_geotrans, im_proj, path_out):
#     '''
#     im_data: tow dimentions (order: row, col),or three dimentions (order: row, col, band)
#     '''
#     if 'int8' in im_data.dtype.name:
#         datatype = gdal.GDT_Byte
#     elif 'int16' in im_data.dtype.name:
#         datatype = gdal.GDT_UInt16
#     else:
#         datatype = gdal.GDT_Float32
#     if len(im_data.shape) == 3:
#         im_data = np.transpose(im_data, (2, 0, 1))
#         im_bands, im_height, im_width = im_data.shape
#     else:
#         im_bands,(im_height, im_width) = 1,im_data.shape
#     driver = gdal.GetDriverByName("GTiff")
#     dataset = driver.Create(path_out, im_width, im_height, im_bands, datatype)
#     if(dataset!= None):
#         dataset.SetGeoTransform(im_geotrans)    # 
#         dataset.SetProjection(im_proj)      # 
#     if im_bands > 1:
#         for i in range(im_bands):
#             dataset.GetRasterBand(i+1).WriteArray(im_data[i])
#         del dataset
#     else:
#         dataset.GetRasterBand(1).WriteArray(im_data)
#         del dataset


import rasterio as rio
import numpy as np

def readTiff(path_in):
    ''' 
        author: xin luo, date: 2021.4.11
        input: path of the .tif image
        output: rasterio DatasetReader object, and np.array data (image)
    '''
    image_src = rio.open(path_in)
    if image_src.count > 1:
        bands_ind = [i for i in range(1, image_src.count+1)]
        image = image_src.read(bands_ind)
        image = image.transpose(1, 2, 0)
    else: 
        image = image_src.read(1)
    return image_src, image

def writeTiff(im_data, im_transform, im_crs, path_out):
    '''im_data: 3d (row, col, band) np.array.'''
    if len(im_data.shape) > 2:
        im_data = im_data.transpose(2,0,1)
        im_bands, im_height, im_width = im_data.shape
    else:
        im_bands, (im_height, im_width) = 1, im_data.shape
        im_data = np.expand_dims(im_data, axis=0)
    with rio.open(
        path_out, 'w',
        driver='GTiff',
        height=im_height,
        width=im_width,
        count=im_bands,
        dtype=im_data.dtype,
        crs = im_crs,
        transform=im_transform,
) as dst:
        dst.write(im_data)
