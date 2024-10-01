# eci_to_ecef.py

# Usage: python3 script_name.py arg1 arg2 ...
#  Converts ECI vector components to ECEF

# Parameters:
# year: year of date
# month: month of date
# day: day of date
# hour: hour of time
# minute: minute of time
# second: second of time
# eci_x_km: x value of ECI vector in km
# eci_y_km: y value of ECI vector in km
# eci_z_km: z value of ECI vector in km
# Output:
#  Prints the coordinates in the ecef reference frame (x, y, z), answer in degrees

# Written by Maxwell Oross
# Other contributors: None

# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys  # argv

# "constants"
w = 7.292115*10e-5 #rad/sec
sec_per_day = 86400.0  # Seconds in a day

# initialize script arguments
year = float(sys.argv[1])
month = float(sys.argv[2])
day = float(sys.argv[3])
hour = float(sys.argv[4])
minute = float(sys.argv[5])
second = float(sys.argv[6])
ecef_x_km = float(sys.argv[7])
ecef_y_km = float(sys.argv[8])
ecef_z_km = float(sys.argv[9])

# parse script arguments
if len(sys.argv)==10:
  year = float(sys.argv[1])
  month = float(sys.argv[2])
  day = float(sys.argv[3])
  hour = float(sys.argv[4])
  minute = float(sys.argv[5])
  second = float(sys.argv[6])
  ecef_x_km = float(sys.argv[7])
  ecef_y_km = float(sys.argv[8])
  ecef_z_km = float(sys.argv[9])

else:
  print(\
   'Usage: '\
   'python3 ecef_to_llh.py r_x_km r_y_km r_z_km'\
  )
  exit()

# write script below this line
#Convert JD to JDfrac
JD = day-32075+1461*(year+4800+(month-14)/12)/4+367*(month-2-(month-14)/12*12)/12-3*((year+4900+(month-14)/12)/100)/4
JDi = int(JD)
JDm = JDi-0.5
Dfrac = (second+60*(minute+60*hour))/86400
JDfrac = JDm+Dfrac

#Calculate GMST
JDut1 = JDfrac
Tut1 = (JDut1-2451545.0)/36525.0
thetagmst = 67310.54841+(876600*60*60+8640184.812866)*Tut1+0.093104*Tut1**2+(-6.2*10**-6*Tut1**3)
thetagmst_rad = ((thetagmst/sec_per_day)*w+2*math.pi)
thetagmst_rad = (math.fmod(thetagmst_rad,2*math.pi))/10

ecef_x_km = (eci_x_km*math.cos(-thetagmst_rad))+(eci_y_km*(-math.sin(-thetagmst_rad)))
ecef_y_km = (eci_x_km*math.sin(-thetagmst_rad))+(eci_y_km*(math.cos(-thetagmst_rad)))
ecef_z_km = eci_z_km
#Final answers
print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)
