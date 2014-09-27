#! /usr/bin/env python

import scipy.misc
from scipy import ndimage
import sys

im1 = scipy.misc.imread(sys.argv[1])

blu = im1[:,:,2]

blu_no_edge = blu[10:-10,10:-10]

blu_no_edge[blu_no_edge<=50]=0

eroded_blu = ndimage.morphology.binary_erosion(blu_no_edge,iterations=4)

labels, nb = ndimage.label(eroded_blu)

print (nb)

