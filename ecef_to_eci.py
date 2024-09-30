# script_name.py
#
# Usage: python3 script_name.py arg1 arg2 ...
# Text explaining script usage
# Parameters:
# arg1: description of argument 1
# arg2: description of argument 2
# ...
# Output:
# A description of the script output
#
# Written by Erik Judy
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.
# import Python modules
# e.g., import math # math module
import sys
import math
import numpy as np
# "constants"
R_E_KM = 6378.137
w=7.292115*(10**-5)
# helper functions
## function description
# def calc_something(param1, param2):
# pass
# initialize script arguments
year=float('nan')
month=float('nan')
day=float('nan')
hour=float('nan')
minute=float('nan')
second=float('nan')
ecef_x_km=float('nan')
ecef_y_km=float('nan')
ecef_z_km=float('nan')
if len(sys.argv)==10:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day  = float(sys.argv[3])
    hour = float(sys.argv[4])
    minute = float(sys.argv[5])
    second = float(sys.argv[6])
    ecef_x_km=float(sys.argv[7])
    ecef_y_km=float(sys.argv[8])
    ecef_z_km=float(sys.argv[9])
else:
    print(\
     'Usage: '\
     'python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km'\
    )
    exit()
# write script below this line
A = math.floor(year / 100)
B = 2 - A + math.floor(A / 4) 
jd = math.floor(365.25 * (year + 4716)) + math.floor(30.6001 * (month + 1)) + day + B - 1524.5
# Add the fractional part of the day
d_frac = (hour + minute / 60 + second / 3600) / 24
jd_frac=jd+d_frac
T = (jd_frac - 2451545.0) / 36525.0
gmst_0 = (67310.54841 + (876600 * 60*60 +8640184.812866)*T + 0.093104 * T**2 - 6.2e-6 * T**3)
gmst_rad = math.fmod(gmst_0%86400 * w +2*math.pi, 2*math.pi)
ecef_vec=np.array([ecef_x_km, ecef_y_km, ecef_z_km])
rot_matrix= np.array([[math.cos(-gmst_rad), -math.sin(-gmst_rad), 0], 
                    [math.sin(-gmst_rad), math.cos(-gmst_rad), 0],
                    [0,0,1]])
rot_inverse= np.linalg.inv(rot_matrix)
r_eci=np.dot(rot_inverse, ecef_vec)
eci_x_km=r_eci[0]
eci_y_km=r_eci[1]
eci_z_km=r_eci[2]
print(eci_x_km)
print(eci_y_km)
print(eci_z_km)