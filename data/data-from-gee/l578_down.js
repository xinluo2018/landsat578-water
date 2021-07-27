// author: xin luo
// create: 2020.11.9
// des: This code export the selected l578 image to the google drive.

/////////////////////////////////////////
var image_id = 'LANDSAT/LT05/C01/T1_SR/LT05_169032_20000204'

var region = ee.Geometry.Rectangle(46.03, 40.78, 46.45, 41.07)
// var bands_sel = ['B2', 'B3', 'B4', 'B5', 'B6', 'B7']  // landsat 8
// var bands_vis = ['B5', 'B4', 'B3']   // landsat 8
var bands_sel = ['B1', 'B2', 'B3', 'B4', 'B5', 'B7']  // landsat 5,7
var bands_vis = ['B4', 'B3', 'B2']                    // landsat 5,7

// source images and scene region

var l578_scene = ee.Image(image_id).clip(region).select(bands_sel)
print('l578_scene', l578_scene)


// visualization
Map.centerObject(region, 9);
Map.addLayer(l578_scene, {bands: bands_vis, min:0, max:3000}, 'l578_scene');

// // Export to Google Drive
// Export.image.toDrive({
//   image: l578_scene,
//   description: 'l5_scene_20',
//   folder: 'landsat578_water',
//   scale: 30,
//   fileFormat: 'GeoTIFF',
//   region: region
//   });

