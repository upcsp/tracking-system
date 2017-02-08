#!/usr/bin/python


import csv	
data_initial = open("gps_balloon.csv", "rb")
data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",")

f = open('path.kml', 'w')


f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
f.write("	<Document>\n")
f.write("	<name>Balloon path</name>\n")
f.write('	<Style id="style1">\n')
f.write("		<LineStyle>\n")
f.write("			<color>64B40014</color>\n")
f.write("			<width>4</width>\n")
f.write("		</LineStyle>\n")
f.write("		<PolyStyle>\n")
f.write("			<color>5aFFFFFF</color>\n")
f.write("		</PolyStyle>\n")
f.write("	</Style>\n")
f.write("		<Placemark>\n")
f.write("			<name> Balloon Path </name>\n")
f.write("			<styleUrl>#style1</styleUrl> \n")
f.write("   		<LineString>\n")
f.write("   		<extrude>1</extrude>\n")
f.write("   		<tessellate>1</tessellate>\n")
f.write("   		<altitudeMode>absolute</altitudeMode>\n")
f.write("			<coordinates>")
for row in data:
	f.write("			"+row[2]+","+row[1]+","+row[3]+"\n")
f.write("			</coordinates>\n")
f.write("			</LineString>\n")
f.write("		</Placemark>\n")
f.write("</Document>")
f.write("</kml>")
f.close()



