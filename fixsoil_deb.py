   # Will have to run this code everytime you create a new wrfinput_dXX.nc file (i.e. after ./real.exe)
   # To run script type:
   # python soil_em
  
from netCDF4 import Dataset as NetCDFFile
import numpy as np

geo_nc=NetCDFFile("/data/hpcdata/users/empott15/PhD/debris_paper_runs/noahLSM_newWRF_WPS/WPS_debris_soilchanged/geo_em.d04.nc","r+")

######################################################
# Adjust dominant top and bottom soil categories
######################################################
var1='SCT_DOM'
geo_nc.variables[var1][:]=np.where(geo_nc.variables['LU_INDEX'][:]==24, 16, geo_nc.variables[var1][:]) # if it's clean ice, change soil type to 16
geo_nc.variables[var1][:]=np.where(geo_nc.variables['LU_INDEX'][:]==20, 5, geo_nc.variables[var1][:]) # if it's debris, change soil type to debris (5)
geo_nc.variables[var1][:]=np.where((geo_nc.variables['LU_INDEX'][:]!=24) & (geo_nc.variables['LU_INDEX'][:]!=20) & (geo_nc.variables[var1][:]==16), 6, geo_nc.variables[var1][:]) #if it's not glacier, change to soil type 6

var2='SCB_DOM'
geo_nc.variables[var2][:]=np.where(geo_nc.variables['LU_INDEX'][:]==24, 16, geo_nc.variables[var2][:])
geo_nc.variables[var2][:]=np.where(geo_nc.variables['LU_INDEX'][:]==20, 5, geo_nc.variables[var2][:])
geo_nc.variables[var2][:]=np.where((geo_nc.variables['LU_INDEX'][:]!=24) & (geo_nc.variables['LU_INDEX'][:]!=20) & (geo_nc.variables[var2][:]==16), 9, geo_nc.variables[var2][:])

#######################################################
# Adjust fractional soil cagegories
#######################################################

var3='SOILCTOP'
geo_nc.variables[var3][0,15,:,:]=np.where(geo_nc.variables['LU_INDEX'][0]==24, 1, 0)
geo_nc.variables[var3][0,4,:,:]=np.where(geo_nc.variables['LU_INDEX'][:]==20, 1, 0)
geo_nc.variables[var3][0,5,:,:]=np.where((geo_nc.variables['LU_INDEX'][0]==24) | (geo_nc.variables['LU_INDEX'][:]==20), 0, 1)
print('checking SOILCTOP still sum to 1, max of the sum='+str(np.max(np.sum(geo_nc.variables[var3],axis=1)))+'min of the sum='+str(np.min(np.sum(geo_nc.variables[var3],axis=1))))

var4='SOILCBOT'
#If main landuse is 24 (snow and ice), set fraction of  bottom soil category that's landice to 1, otherwise 0
geo_nc.variables[var4][0,15,:,:]=np.where(geo_nc.variables['LU_INDEX'][0]==24, 1, 0)
geo_nc.variables[var4][0,4,:,:]=np.where(geo_nc.variables['LU_INDEX'][:]==20, 1, 0)

#If main landuse is 24, set fraction of other soil categories to 0, otherwise leave them be
geo_nc.variables[var4][0,8,:,:]=np.where((geo_nc.variables['LU_INDEX'][0]==24) | (geo_nc.variables['LU_INDEX'][:]==20), 0, geo_nc.variables[var4][0,8,:,:])
geo_nc.variables[var4][0,5,:,:]=np.where((geo_nc.variables['LU_INDEX'][0]==24) | (geo_nc.variables['LU_INDEX'][:]==20), 0, geo_nc.variables[var4][0,5,:,:])
#If the main landuse is not ice (and it's not anything else), set fraction =8 to  1-(fraction=5) (as opposed to having ice under soil
geo_nc.variables[var4][0,8,:,:]=np.where((geo_nc.variables['LU_INDEX'][0]!=24) & (geo_nc.variables['LU_INDEX'][:]!=20), 1-geo_nc.variables[var4][0,5,:,:], geo_nc.variables[var4][0,8,:,:])
print('checking SOILCTOP still sum to 1, max of the sum='+str(np.max(np.sum(geo_nc.variables[var4],axis=1)))+'min of the sum='+str(np.min(np.sum(geo_nc.variables[var4],axis=1))))


geo_nc.close()
#for debris cover you'll need this syntax:
#nc1.variables['ISLTYP'][:]=np.where((nc1.variables['LU_INDEX'][:]==24) | (nc1.variables['LU_INDEX'][:]==28),16,nc1.variables['ISLTYP'][:])




