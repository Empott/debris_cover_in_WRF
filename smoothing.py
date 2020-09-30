   # Will have to run this code everytime you create a new wrfinput_dXX.nc file (i.e. after ./real.exe)
   # To run script type:
   # python soil_em
  
from netCDF4 import Dataset as NetCDFFile
import numpy as np

nosmth_nc=NetCDFFile("/data/hpcdata/users/empott15/PhD/debris_paper_runs/noahLSM_newWRF_WPS/WPS_debris_soilchanged/geo_em.d04.nc","r+")
smth_nc=NetCDFFile("/data/hpcdata/users/empott15/PhD/debris_paper_runs/noahLSM_newWRF_WPS/WPS_debris_soilchanged/smthdesmth_1pass/geo_em.d04.nc","r+")

#height_orig=nosmth_nc.variables['HGT_M'][:]
height_smoothed=smth_nc.variables['HGT_M'][:]

for i in range(81,87):
    for j in range(62,67):
#        height_orig[0,j,i]=height_smoothed[0,j,i]
        nosmth_nc.variables['HGT_M'][0,j,i]=height_smoothed[0,j,i]

nosmth_nc.close()
#nosmth_nc.variables['HGT_M']=height_orig
#nosmth_nc.close()
#smth_nc.close()




