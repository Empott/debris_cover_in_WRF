   # Will have to run this code everytime you create a new wrfinput_dXX.nc file (i.e. after ./real.exe)
   # To run script type:
   # python soil_em
  
from netCDF4 import Dataset as NetCDFFile
import numpy as np

deb_orig_nc=NetCDFFile("/data/hpcdata/users/empott15/PhD/debris_paper_runs/noahLSM_newWRF_WPS/WPS_debris_soilchanged/geo_em.d04.nc","r+")

#height_orig=nosmth_nc.variables['HGT_M'][:]

deb_orig_nc.variables['LU_INDEX'][0,61,72]=20
deb_orig_nc.variables['LU_INDEX'][0,62,73]=20
deb_orig_nc.variables['LU_INDEX'][0,63,73]=20
deb_orig_nc.variables['LU_INDEX'][0,63,72]=19
deb_orig_nc.variables['LU_INDEX'][0,64,72]=19
deb_orig_nc.variables['LU_INDEX'][0,66,73]=19
deb_orig_nc.variables['LU_INDEX'][0,65,72]=20
deb_orig_nc.variables['LU_INDEX'][0,68,76]=24
deb_orig_nc.variables['LU_INDEX'][0,68,77]=24

deb_orig_nc.close()
#nosmth_nc.variables['HGT_M']=height_orig
#nosmth_nc.close()
#smth_nc.close()




