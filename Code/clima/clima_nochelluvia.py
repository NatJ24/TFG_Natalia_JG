#!/usr/bin/env python3

import carla
import random
import math

# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
world = client.get_world()
atributos_weather = carla.WeatherParameters(
    cloudiness=100.0,               # Cielo completamente cubierto
    precipitation=100.0,            # Lluvia intensa
    precipitation_deposits=90.0,    # Charcos grandes en la carretera
    wind_intensity=30.0,            # Viento moderado (tormenta)
    fog_density=10.0,               # Ligera niebla por humedad
    fog_distance=50.0,              # Visibilidad más reducida
    fog_falloff=1.0,                # Niebla uniforme
    wetness=100.0,                  # Todo está empapado
    scattering_intensity=0.2,       # Menor dispersión de la luz (ambiente más oscuro)
    mie_scattering_scale=0.03,      # Ligera bruma
    rayleigh_scattering_scale=0.01, # Cielo muy oscuro
    dust_storm=0.0,                 # Sin calima
    sun_azimuth_angle=300.0,        # Sol bajo o fuera del horizonte
    sun_altitude_angle=-10.0        # Sol bajo el horizonte → noche
)
world.set_weather(atributos_weather)
