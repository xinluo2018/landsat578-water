// author: xin luo
// create: 2020.11.25
// des: search the landsat images

/////////////////////////////////////////////////////////////////
// var bands_vis = ['B5', 'B4', 'B3']   // landsat 8
var bands_vis = ['B3', 'B2', 'B1']       // landsat 5,7

var region = ee.Geometry.Rectangle(46.03, 40.78, 46.45, 41.07) //(lon_min,lat_min,lon_max,lat_max)
// the area may be appropriate in 1,000,000,000-2,000,000,000
print('scene area:', region.area())

/// Landsat 578 images
var start_time = '1993-6-10'
var end_time = '2013-10-01'

// ----- Landsat 578 images selection ----- 
var img_col = ee.ImageCollection('LANDSAT/LT05/C01/T1_SR')
// var img_col = ee.ImageCollection('LANDSAT/LE07/C01/T1_SR')
// var img_col = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR')
  .filter(ee.Filter.lt('CLOUD_COVER_LAND', 20))
  .filter(ee.Filter.gt('CLOUD_COVER_LAND', 0))
  .filterBounds(region)
  .filterDate(start_time, end_time);

// ----- Ensure the landsat image fully contain the training region. ----- 
var condition = function(image){
    var footprint = ee.Geometry(image.get('system:footprint'))
    var condition = ee.Geometry.Polygon(footprint.coordinates()).contains(region)
    return ee.Algorithms.If(condition, 
                            image.set('data', 'true'), 
                            ee.Image([]).set('data', 'false'))};

var img_sel = img_col.map(condition).filterMetadata('data', 'equals','true')
print(img_sel)

// ---- specific landsat image selection ---- 
var image = img_sel.first().clip(region)
// var image = ee.Image('LANDSAT/LE07/C01/T1_SR/LE07_175044_20000325')
            // .clip(region)
print(image)


// ---- visualization: outline and selection image ---- 
Map.centerObject(region, 9);
var empty = ee.Image().byte();
var scene_outline = empty.paint({
    featureCollection: region, color: 1, width: 3});

Map.addLayer(image, {bands: bands_vis, min:0, max:4000}, 'Landsat 5');
Map.addLayer(scene_outline, {palette: '#FFFF00'}, 'scene_outline')



