#!/usr/bin/env python3

import carla
import random
import math

# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
world = client.get_world()
atributos_weather = carla.WeatherParameters(
    cloudiness=10.0,                # Cielo casi despejado
    precipitation=0.0,              # Sin lluvia
    precipitation_deposits=0.0,     # Suelo seco
    wind_intensity=60.0,            # Viento intenso (típico del Terral)
    fog_density=5.0,                # Ligero efecto térmico
    fog_distance=100.0,             # Buena visibilidad
    fog_falloff=0.2,                # Transición muy suave de la niebla
    wetness=5.0,                    # Superficies secas
    scattering_intensity=0.4,       # Ligera distorsión en la luz
    mie_scattering_scale=0.02,      # Algo de bruma
    rayleigh_scattering_scale=0.06, # Cielo ligeramente apagado
    dust_storm=0.0,                 # No hay polvo suspendido
    sun_azimuth_angle=270.0,        # Sol en el oeste (tarde)
    sun_altitude_angle=55.0         # Sol alto pero más cálido
)
world.set_weather(atributos_weather)
