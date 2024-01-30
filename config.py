""" Configure file for hypoDD interface
"""
import os
import numpy as np


class Config(object):
  def __init__(self):

    self.ctlg_code = 'subei'
    self.fsta_in = 'input/XC_station.sta'
    self.fsta_out = 'input/station.dat'
    self.fpha_in = 'input/suei_phase.pha'
    self.dep_corr = 5 # avoid air quake
    self.ot_range = '20231024-20240128'
    self.lat_range = [39.1,39.4]
    self.lon_range = [97.1,97.5]
    self.num_grids = [1,1] # x,y (lon, lat)
    self.xy_pad = [0.06,0.05] # degree
    self.num_workers = 1
    self.keep_grids = False

