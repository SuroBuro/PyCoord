import math
from math import sin, cos, pi, sqrt
from pyproj import Transformer

# Inputs are given in degrees
# E and N are +ve; W and S are -ve
input_coord = [0, 0]
input_coord[0] = float(input("Latitude (in degrees): "))
input_coord[1] = float(input("Longitude (in degrees): "))

squares_east = int(input("Kilometers to the east: "))
squares_south = int(input("Kilometers to the south: "))

list_coordinates = []
converted_coordinates = []
lonlat_to_webmercator = Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True)

# Constants
equator_radius = 6378.1  # km
polar_radius = 6356.8  # km
distance_between_lat = 110.574  # km per degree of latitude

def rad_2_deg(rads):
    return (rads * 180) / pi

def deg_2_rad(deg):
    return (deg * pi) / 180

# Radius at latitude (assuming geoid shape)
def radius_at_latitude(latitude):
    latitude_rad = deg_2_rad(latitude)
    return equator_radius*sqrt(
        (equator_radius**2 * cos(latitude_rad)**2 + polar_radius**2 * sin(latitude_rad)**2)
        / (equator_radius**2 * cos(latitude_rad)**2 + polar_radius**2 * sin(latitude_rad)**2)
    )

# Longitude difference based on distance
def longitude_difference(latitude, distance):
    radius = radius_at_latitude(latitude)
    return rad_2_deg(distance / (radius * cos(deg_2_rad(latitude))))

# Latitude difference based on distance
def latitude_difference(distance):
    return distance / distance_between_lat

def mytransform(lon, lat):
    x, y = lonlat_to_webmercator.transform(lon, lat)
    return x, y

def conversion():
    for coords in range(len(list_coordinates)):
        new_xy = [0,0]
        new_xy[0], new_xy[1] = mytransform(list_coordinates[coords][0],list_coordinates[coords][1]) 
        converted_coordinates.append(new_xy)
    


# Main function
def _main():
    for i in range(squares_south + 1): 
        new_latitude = input_coord[0] - latitude_difference(i)  # Moves south, decrease latitude
        for j in range(squares_east + 1):  
            new_longitude = input_coord[1] + longitude_difference(new_latitude, j)  # Moves east
            list_coordinates.append([new_latitude, new_longitude])
            
_main()
conversion()

def extent():
    for i in range(squares_south - 1):
        for j in range(squares_east - 1):
            print("Extent for zone", i, j , "is ", converted_coordinates[i*squares_east + j ], converted_coordinates[i*squares_east + j +1], converted_coordinates[(i+1)*squares_east + j], converted_coordinates[(i+1)*squares_east + j + 1] )
            print("Extent for coordinates", i, j, "is ",list_coordinates[i*squares_east + j ], list_coordinates[i*squares_east + j +1], list_coordinates[(i+1)*squares_east + j], list_coordinates[(i+1)*squares_east + j + 1] )
            

extent()

