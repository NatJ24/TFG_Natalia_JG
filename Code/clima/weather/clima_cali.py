#!/usr/bin/env python3

import carla
import random
import math

# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
world = client.get_world()
atributos_weather = carla.WeatherParameters(
    cloudiness=30.0,                # Algo de nubosidad o bruma
    precipitation=0.0,              # Sin lluvia
    precipitation_deposits=0.0,     # Suelo seco
    wind_intensity=20.0,            # Viento suave que arrastra partculas
    fog_density=20.0,               # Densidad visible de calima
    fog_distance=40.0,              # Visibilidad reducida
    fog_falloff=0.8,                # Cae rpidamente la visibilidad a distancia
    wetness=10.0,                   # Ligeramente hmedo
    scattering_intensity=0.7,       # Luz muy dispersa (efecto neblinoso)
    mie_scattering_scale=0.2,       # Alta dispersin por polvo (calima)
    rayleigh_scattering_scale=0.02, # Menos azul, cielo ms blanquecino/ocre
    dust_storm=1.0,                 # Activa efecto de calima/polvo
    sun_azimuth_angle=100.0,        # Sol en el sureste
    sun_altitude_angle=40.0         # Sol en altura media
)
world.set_weather(atributos_weather)

