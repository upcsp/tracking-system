# tracking-system


Live tracking system of a Xbee-based payload with Google Earth.

Done by UPC Space Program - ESEIAAT, UPC - 2017

What can you find here? 

#Main Scripts

- conversor.py -> Python script to create a KML spline from a CSV document. Please notice this CSV document has a structure of "time", "Latitude", "Longitude", "Altitude" for each column. GPS_ballon.csv is an exemple of a CSV document and "path.kml" is the KML file 

- xbee_balloon -> python script that creates a KML point readint from a Serial port and appends data to a CSV file.  

- xbee_car -> python script that creates a KML point reading from a Serial port. 

#Calling scripts for unix-based systems

- xbee_balloon_command -> it calls forever "xbee_balloon"

- xbee_car_comand -> it calls forever "xbee_car"

- xbee_csvtokml_command -> it calls forever "conversor.py"


Other PNG files and KML files are just an exemple that could be added to a Google Earth.

Please change boundrate and port from main scripts to your preferences

