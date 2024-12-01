import math
from math import sin, cos

# Inputs are given in degrees
# E and N are +ve; W and S are -ve
input_coord = [0, 0]
input_coord[0] = float(input("Latitude (in degrees): "))
input_coord[1] = float(input("Longitude (in degrees): "))

squares_east = int(input("Kilometers to the east: "))
squares_south = int(input("Kilometers to the south: "))

list_coordinates = []

# Constants
equator_radius = 6378.1  # km
polar_radius = 6356.8  # km
distance_between_lat = 110.574  # km per degree of latitude

def rad_2_deg(rads):
    return (rads * 180) / math.pi

def deg_2_rad(deg):
    return (deg * math.pi) / 180

# Radius at latitude (assuming geoid shape)
def radius_at_latitude(latitude):
    latitude_rad = deg_2_rad(latitude)
    return equator_radius*math.sqrt(
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

# Main function
def _main():
    for i in range(squares_south + 1): 
        new_latitude = input_coord[0] - latitude_difference(i)  # Moves south, decrease latitude
        for j in range(squares_east + 1):  
            new_longitude = input_coord[1] + longitude_difference(new_latitude, j)  # Moves east
            list_coordinates.append([new_latitude, new_longitude])
            print([new_latitude, new_longitude])

_main()
