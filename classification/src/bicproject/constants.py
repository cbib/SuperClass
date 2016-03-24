#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Short summary

Longer summary
"""

# imports
import numpy as np


# obj_df = pd.read_csv(per_object_file, names=PER_OBJECT_COLS, header=None, sep=',')
# for ROI, data in df.groupby('ImageNumber'):

# Columns to read in the CSV file
ROI_COL = 'ROI'
TRACE_COL = 'Trace'
DENSITY_COL = 'D(µm²/s)'
MSD_COL = 'MSD(0)'
MSE_COL = 'MSE'

# extremum of densities for the histograms
DENSITY_MAX = 10e1
DENSITY_MIN = 10e-5
DENSITY_HISTOGRAM_BINS = np.logspace(-4, 1, num=20) # BINS to compute the density histogram
DENSITY_HISTOGRAM_LABELS = ["HIST_DENSITY_%f" % _ for _ in DENSITY_HISTOGRAM_BINS[:-1]]


# extremim of densities for the number of frames per trajectory
TRAJECTORY_FRAMES_MAX = 20
TRAJECTORY_FRAMES_MIN = 1
TRAJECTORY_FRAMES_HISTOGRAM_BINS = np.linspace(TRAJECTORY_FRAMES_MIN, TRAJECTORY_FRAMES_MAX, num=20)
TRAJECTORY_FRAMES_HISTOGRAM_LABELS = ["HIST_NB_FRAMES_%f" % _ for _ in TRAJECTORY_FRAMES_HISTOGRAM_BINS[:-1]]


MSD_MAX = 0.5
MSD_MIN = -0.5
MSD_HISTOGRAM_BINS = np.linspace(MSD_MIN, MSD_MAX, num=20)
#print ("MSD_HISTOGRAM_BINS", MSD_HISTOGRAM_BINS)
MSD_HISTOGRAM_LABELS = ["HIST_MSD_%f" % _ for _ in MSD_HISTOGRAM_BINS[:-1]]


# MSD_MAX = 0.5
# MSD_MIN = -0.5
# MSD_HISTOGRAM_BINS = np.linspace(MSD_MIN, MSD_MAX, num=20)
# MSD_HISTOGRAM_LABELS = ["HIST_MSD_%f" % _ for _ in MSD_HISTOGRAM_BINS[:-1]]


# metadata
__author__ = 'Romain Giot'
__copyright__ = 'Copyright 2014, LaBRI'
__credits__ = ['Romain Giot']
__licence__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Romain Giot'
__email__ = 'romain.giot@u-bordeaux1.fr'
__status__ = 'Prototype'

