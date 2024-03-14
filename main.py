from star_wars_api import StarWarsApi

api_client = StarWarsApi()

person = api_client.get_person(1)
print(f"Person name: {person.name}")
print(person.skin_color)

planet = api_client.get_planet(3)
print(f"Planet name: {planet.name}")

starhip = api_client.get_starhip(9)
print(f"Starhip name: {starhip.name}")
