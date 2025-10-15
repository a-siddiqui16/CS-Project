import requests

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

        #Print individual lines for celstrak
        print(f"Satellite data for {norad_id}")
        print(f"Name: {satellite_name}")
        print(f"Line 1: {tle_line1}")
        print(f"Line 2: {tle_line2}")
        

print(get_satellite_tle(205))


