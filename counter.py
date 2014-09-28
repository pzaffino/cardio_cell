#! /usr/bin/env python

import scipy.misc
from scipy import ndimage
import sys

# Define utility function
def remove_edge(im, num_pixel):
    return im[num_pixel:-num_pixel, num_pixel:-num_pixel]

def threshold_image(im, threshold):
    im[im<=threshold]=0
    return im

def count_cell(img, edge_pixels, threshold, erosion_iterations):
    img_no_edge = remove_edge(img, edge_pixels)
    img_thr = threshold_image(img_no_edge, threshold)
    eroded_img = ndimage.morphology.binary_erosion(img_thr, iterations = erosion_iterations)
    labels, number_labels = ndimage.label(eroded_img)
    return number_labels
   
# Define common stuff
edge_pixels = 10
threshold = 50
erosion_iterations = 4

# Read image and split channels
cell_image = scipy.misc.imread(sys.argv[1])
red, green, blu = [cell_image[:,:,i] for i in range(3)]

# Count 
number_blu_labels = count_cell(blu, edge_pixels, threshold, erosion_iterations)
number_green_labels = count_cell(green, edge_pixels, threshold, erosion_iterations)

# Print results
print ("Blu cells = %d" % number_blu_labels)
print ("Green cells = %d" % number_green_labels)

