
#object to hold a single coordinate with an "x" and "y"
class coordinate:
    def __init__(self, x, y):
        self.x = (int)(x * 10000)
        self.y = (int)(y * 10000)
    def __str__(self):
        return "(x=" + str(self.x) + ", y=" + str(self.y) + ")"

#method for determining if a terminal's location resides within a list of coordinates (polygon).
#uses a ray casting method
def isInside(coordinates, terminal):
    intersections = 0
    for i in range(len(coordinates) - 1):
        #makes sure we are working with a ray and not a line
        if coordinates[i].x < terminal.x:
            continue
        #simple case of the ray intersecting an edge
        if terminal.y < coordinates[i].y:
            if terminal.y > coordinates[i+1].y:
                intersections += 1
        if terminal.y > coordinates[i].y:
            if terminal.y < coordinates[i+1].y:
                intersections += 1
        #edge case of the ray intersecting a vertex
        if terminal.y == coordinates[i].y:
            if terminal.y < coordinates[i-1].y:
                if terminal.y > coordinates[i+1].y:
                    intersections += 1
            if terminal.y > coordinates[i-1].y:
                if terminal.y < coordinates[i+1].y:
                    intersections += 1
    #prints intersetions for debugging
    print("Intersections = " + str(intersections))
    #if intersections is even the terminal is not inside the polygon
    if intersections % 2 == 0:
        return False
    
    return True


#---temporary immediate testing---
#Polygon1 uses a polygon directly from a sample file
testPolygon1 = [coordinate(-73.7244, 33.7311),
               coordinate(-73.7555, 34.2152),
               coordinate(-74.1122, 34.8130),
               coordinate(-74.2455, 34.9554),
               coordinate(-74.7267, 35.3478),
               coordinate(-75.3157, 35.6751),
               coordinate(-75.3927, 35.7595),
               coordinate(-76.0458, 36.2051),
               coordinate(-76.6294, 36.3936),
               coordinate(-75.7077, 37.2388),
               coordinate(-75.5692, 37.3625),
               coordinate(-75.0669, 38.0845),
               coordinate(-74.7391, 38.9278),
               coordinate(-74.7663, 39.1631),
               coordinate(-75.1261, 39.7447),
               coordinate(-75.3294, 39.8481),
               coordinate(-76.2150, 39.8367),
               coordinate(-76.6440, 39.6596),
               coordinate(-77.3920, 39.1118),
               coordinate(-77.6849, 38.7677),
               coordinate(-78.0312, 37.9284),
               coordinate(-78.0361, 37.4859),
               coordinate(-77.8527, 37.1289),
               coordinate(-77.5438, 36.6058),
               coordinate(-76.9700, 36.3765),
               coordinate(-77.6915, 35.5569),
               coordinate(-77.9967, 35.3648),
               coordinate(-78.5894, 34.7429),
               coordinate(-79.2555, 33.9647),
               coordinate(-79.2650, 33.9520),
               coordinate(-79.6439, 33.1854),
               coordinate(-79.5971, 32.8502),
               coordinate(-79.4686, 32.4516),
               coordinate(-79.0242, 32.2083),
               coordinate(-78.3990, 31.7634),
               coordinate(-78.3954, 31.7595),
               coordinate(-77.8375, 31.0819),
               coordinate(-77.7949, 31.0640),
               coordinate(-77.8520, 31.0342),
               coordinate(-78.4461, 30.3208),
               coordinate(-78.9365, 29.8907),
               coordinate(-79.1253, 29.5860),
               coordinate(-79.3265, 28.8780),
               coordinate(-79.3208, 28.4420),
               coordinate(-79.2883, 28.1861),
               coordinate(-79.0043, 27.5095),
               coordinate(-78.8920, 27.2584),
               coordinate(-78.5310, 26.8457),
               coordinate(-78.3327, 26.5955),
               coordinate(-77.6841, 26.2888),
               coordinate(-76.9053, 26.4727),
               coordinate(-76.3787, 26.9257),
               coordinate(-75.8621, 27.6291),
               coordinate(-75.6697, 28.3267),
               coordinate(-75.7523, 29.0198),
               coordinate(-75.9718, 29.6928),
               coordinate(-75.9856, 29.7133),
               coordinate(-76.4052, 30.4057),
               coordinate(-76.2746, 31.1296),
               coordinate(-75.2758, 31.7763),
               coordinate(-75.1090, 31.9099),
               coordinate(-74.1729, 32.6918),
               coordinate(-74.0711, 32.8579),
               coordinate(-73.7318, 33.4604),
               coordinate(-73.7244, 33.7311)]

#---Testing Polygon 1---
#Simple known coordinate within polygon1
testTerminal = coordinate(-75.2700, 39.7481)
test = isInside(testPolygon1, testTerminal) #1
print(test) #true
#Simple known coordinate west of polygon
testTerminal = coordinate(-80.8998, 27.5555)
test = isInside(testPolygon1, testTerminal) #2
print(test) #false
#Simple known coordinate east of polygon
testTerminal = coordinate(-72.3456, 27.5555)
test = isInside(testPolygon1, testTerminal) #0
print(test) #false


#Polygon2 is a simple square polygon
testPolygon2 = [coordinate(0.0000, 0.0000),
               coordinate(0.0000, 100.0000),
               coordinate(100.0000, 100.0000),
               coordinate(100.0000, 50.0000),
               coordinate(100.0000, 0.0000),
               coordinate(0.0000, 0.0000)]

#---Testing Polygon 2---
#Simple known coordinate at center of square
testTerminal = coordinate(50.0000, 50.0000)
test = isInside(testPolygon2, testTerminal) #1
print(test) #true
#Simple known coordinate just outside of square
testTerminal = coordinate(100.0001, 50.0000)
test = isInside(testPolygon2, testTerminal) #0
print(test) #false
#Known coordinate inside square that intersects with vertex
testTerminal = coordinate(25.0000, 50.0000)
test = isInside(testPolygon2, testTerminal) #1
print(test) #true

#Polygon3 is a known edge case that will cause multiple 
#intersections and a potential bug with vertex intersection
testPolygon3 = [coordinate(0.0000, 0.0000),
               coordinate(0.0000, 100.0000),
               coordinate(100.0000, 100.0000),
               coordinate(100.0000, 0.0000),
               coordinate(75.0000, 0.0000),
               coordinate(50.0000, 50.0000),
               coordinate(25.0000, 0.0000),
               coordinate(0.0000, 0.0000)]

#---Testing Polygon 3---
#Coordinate with multiple intersections (inside)
testTerminal = coordinate(1.0000, 25.0000)
test = isInside(testPolygon3, testTerminal) #3
print(test) #true
#Coordinate with multiple intersections (outside)
testTerminal = coordinate(-1.0000, 25.0000)
test = isInside(testPolygon3, testTerminal) #4
print(test) #false
#Intersecting vertex without leaving polygon
testTerminal = coordinate(25.0000, 50.0000)
test = isInside(testPolygon3, testTerminal) #1
print(test) #true


#---Parsing a Demo KML Fie---


#helper method to add coordinates into a polygon
def addCoordinate(currPolygon, lineToParse):
    #example line
    #\t\t\t\t\t\t\t-105.4836,27.1211,0.0\n
    #first finds the individual "x" and "y" bounds
    xEnd = 0
    yEnd = 0
    xPos = True
    for i in range(len(lineToParse)):
        if lineToParse[i] == ',' and xPos == True:
            xEnd = i
            xPos = False
        if lineToParse[i] == ',' and xPos == False:
            yEnd = i

    #edge case catching while parsing files
    if lineToParse[7] == 'r' or xEnd == 0:
        return

    #converts to float and appends a coordinate to the list
    x = float(lineToParse[7:xEnd])
    y = float(lineToParse[xEnd+1:yEnd])
    currPolygon.append(coordinate(x, y))


#opens file in working directory
try:
    f = open("doc.kml", 'r') 
    print("Opening File...")
except IOError: 
    print("Error: File does not appear to exist.")

#Reads all contents into an array of lines
contents = f.readlines()

#Parses and populates all the polygons into the array "allPolygons"
allPolygons = []
currentPolygon = 0
write = False
print("Creating Polygons...")
for line in contents:
    #toggles writing coordinates
    if line == "\t\t\t\t\t\t<coordinates>\n":
        if currentPolygon == 0:
            print("Populating New Polygon...")
        if write == True:
            write = False
            print("Populating New Polygon...")
            currentPolygon += 1
        else:
            write = True
            allPolygons.append([])
        continue
    if write == True:
        #writing coordinates into the allPolygons list
        addCoordinate(allPolygons[currentPolygon], line)

f.close()
print("File Closed.")

#for i in range(len(allPolygons)):
    #print("Polygon: " + str(i))
    #for j in range(len(allPolygons[i])):
        #print(allPolygons[i][j])