from random import choice
from typing import Tuple
from geopy.geocoders import Nominatim


places = ['Бенджамин', 'Фуджи', 'Комод']
places_visited = list()


def get_coordinates_by_city(city_name:str) -> Tuple[int]:
    '''
    retrieve tuple of two coordinates 
    by given city name within the country
    '''

    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(city_name)
    if location is None:
        return f'город написан с ошибкой'
    coordinates = (location.latitude, location.longitude)
    return coordinates


def get_country_by_city(city_name:str) -> str:
    '''
    retrieve country name 
    by given city name within the country
    '''

    geolocator = Nominatim(user_agent="MyApp")
    coordinates = get_coordinates_by_city(city_name)
    location = geolocator.reverse(coordinates)
    address = location.raw['address']
    country = address['country']
    return country


def get_country_by_coordinates(coordinates:Tuple[int]) -> str:
    '''
    retrieve country name 
    by given coordinates: latitude, longitude
    '''

    geolocator = Nominatim(user_agent="MyApp")
    #coordinates = get_geolocation_by_city(city_name)
    location = geolocator.reverse(coordinates)
    address = location.raw['address']
    country = address['country']
    return country


# print(get_country_by_city('Берлин'))  #Deutschland
# print(get_coordinates_by_city('Берлин'))  #(52.5170365, 13.3888599)
# print(get_country_by_coordinates(get_coordinates_by_city('Miami')))  #United States


def show_place_to_go(places) -> str:
    '''
    retrieve one brand-new place to go on dating (randomly)
    '''
    place_to_go = choice(places)

    if place_to_go not in places_visited:
        places_visited.append(place_to_go)
        return place_to_go
    
    return 'везде уже были'

