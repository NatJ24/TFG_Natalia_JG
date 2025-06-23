#!/usr/bin/env python3

import carla
import random
import math

# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
world = client.get_world()
atributos_weather = carla.WeatherParameters(
    cloudiness=10.0,                # Cielo mayormente despejado
    precipitation=0.0,              # Sin lluvia
    precipitation_deposits=0.0,     # Suelo seco, sin acumulacion de agua
    wind_intensity=10.0,            # Brisa ligera
    fog_density=0.0,                # Sin niebla
    fog_distance=100.0,             # Muy buena visibilidad
    fog_falloff=1.0,                # Disminucion suave de la niebla (si la hubiera)
    wetness=10.0,                   # Algo de humedad residual
    scattering_intensity=0.3,       # Dispersion de la luz estandar
    mie_scattering_scale=0.01,      # Muy poca bruma
    rayleigh_scattering_scale=0.10, # Azul claro del cielo
    dust_storm=0.0,                 # Sin calima
    sun_azimuth_angle=90.0,         # Sol saliendo por el este
    sun_altitude_angle=60.0         # Sol alto, casi mediodia
)
world.set_weather(atributos_weather)

