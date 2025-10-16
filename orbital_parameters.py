from skyfield.api import EarthSatellite
from skyfield.api import load
from skyfield.api import wgs84
from tle_fetcher import get_satellite_tle


ts = load.timescale()

norad_id = input("Enter NORAD ID: ")

satellite_data = get_satellite_tle(norad_id)

if satellite_data:
    satellite_name = satellite_data['satellite_name']
    line1 = satellite_data['tle_line1']
    line2 = satellite_data['tle_line2']
  
#Retreives satellite epoch
satellite_epoch = EarthSatellite(line1, line2, satellite_name, ts)

#Generates geocentric satellite position
year, month, day, hour, minute, second = satellite_epoch.epoch.utc
t = ts.utc(year, month, day, hour, minute, second)
geocentric = satellite_epoch.at(t)

#Stores satellite latitude, longitude and height
lat, lon = wgs84.latlon_of(geocentric)
height = wgs84.height_of(geocentric)

def find_Cartesian(x,y,z):
  x, y, z = position.xyz.km
  
  print('  x = {:.3f} km'.format(x))
  print('  y = {:.3f} km'.format(y))
  print('  z = {:.3f} km'.format(z))

find_Cartesian(lat, lon, height)