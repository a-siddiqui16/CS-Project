#Imports
import requests
import sqlite3

def get_satellite_tle(norad_id):

    #Builds a URL that can fetch the TLE data for any satellite
    url = f"https://celestrak.org/NORAD/elements/gp.php?CATNR={norad_id}&FORMAT=tle"

    #Sends request to Celestrak
    print(f"Fethcing TLE data for {norad_id} ")
    response = requests.get(url)


    #Check if request was succesful
    if response.status_code == 200:
        print("Data retrieved succesfully")

        #Split TLE Data into lines
        data = response.text
        lines = data.split('\n')
        
        satellite_name = lines[0].strip()
        tle_line1 = lines[1].strip()
        tle_line2 = lines[2].strip()

        #Return individual lines for celstrak
        return {
            'norad_id': norad_id,
            'satellite_name': satellite_name,
            'tle_line1': tle_line1,
            'tle_line2': tle_line2

        }
    else:
        print(f"Error: Status code {response.status_code}")
        return None


def insert_tle_into_database(satellite_data):
    pass

def import_satellite(norad_id):
    pass





