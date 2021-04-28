import matplotlib.pyplot as plt
import numpy as np

def imgShow(img, extent=None, col_bands=(2,1,0), clip_percent=2, per_band_clip='False'):
    '''
    Arguments:
        img: (row, col, band) or (row, col)
        num_bands: a list/tuple, [red_band,green_band,blue_band]
        clip_percent: for linear strech, value within the range of 0-100. 
        per_band: if 'True', the band values will be clipped by each band respectively. 
    '''
    img = img/(np.amax(img)+0.00001)
    img = np.squeeze(img)
    if np.isnan(np.sum(img)) == True:
        where_are_NaNs = np.isnan(img)
        img[where_are_NaNs] = 0
    elif np.min(img) == np.max(img):
        if len(img.shape) == 2:
            plt.imshow(np.clip(img, 0, 1), extent=extent, vmin=0,vmax=1) 
        else:
            plt.imshow(np.clip(img[:,:,0], 0, 1), extent=extent, vmin=0,vmax=1)
    else:
        if len(img.shape) == 2:
            img_color = img
        else:
            img_color = img[:,:,[col_bands[0], col_bands[1], col_bands[2]]]    
        img_color_clip = np.zeros_like(img_color)
        if per_band_clip == 'True':
            for i in range(3):
                img_color_hist = np.percentile(img_color[:,:,i], [clip_percent, 100-clip_percent])
                img_color_clip[:,:,i] = (img_color[:,:,i]-img_color_hist[0])\
                                    /(img_color_hist[1]-img_color_hist[0]+0.0001)
        else:
            img_color_hist = np.percentile(img_color, [clip_percent, 100-clip_percent])
            img_color_clip = (img_color-img_color_hist[0])\
                                    /(img_color_hist[1]-img_color_hist[0]+0.0001)
        plt.imshow(np.clip(img_color_clip, 0, 1), extent=extent, vmin=0,vmax=1)

def imsShow(img_list, img_name_list, clip_list, col_bands_list):
    ''' des: visualize multiple images.
        input: 
            img_list: containes all images
            img_names_list: image names corresponding to the images
            clip_list: percent clips (histogram) corresponding to the images
            col_bands_list: color bands combination corresponding to the images
    '''
    for i in range(len(img_list)):
        plt.subplot(1, len(img_list), i+1)
        plt.title(img_name_list[i])
        imgShow(img=img_list[i],\
                    col_bands=col_bands_list[i],clip_percent=clip_list[i])
        plt.axis('off')