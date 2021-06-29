# -*- coding: utf-8 -*-
"""0629_folium_screening center

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n0Ch_4bs0FXrUVduRT8t3ioMDTM7PiWG
"""

import pandas as pd
import folium
from folium import plugins
import numpy as np
import os

data = pd.read_excel('./선별진료소_20210629150601.xls')

data = data.dropna(axis=0, subset=["의료기관명", "Latitude", "Longitude"])

data

data.columns

data_1 = data.loc[:,['의료기관명','Latitude', 'Longitude']]
data_1

data_1.columns

data.isnull().sum()

data.info()

loc = folium.Map(location =[37.516258,127.042214 ] ,
                 zoom_start = 15)

loc

name = data_1.loc[:,'의료기관명' ]
name = list(name)
name

geocode = list(zip(data_1['Latitude'], data_1['Longitude']))
geocode

plugins.MarkerCluster(geocode, popups = name).add_to(loc)

loc

loc.save('screening center') 
loc

