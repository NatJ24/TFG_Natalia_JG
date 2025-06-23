#!/usr/bin/env python3

import carla
import random
import math
import time

# Conexión con el servidor de CARLA
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)
world = client.get_world()

# Lista de escenarios con nombre y parámetros climáticos
escenarios_visibilidad = {
    "niebla_espesa_amanecer": carla.WeatherParameters(
        cloudiness=70.0,
        precipitation=0.0,
        precipitation_deposits=0.0,
        wind_intensity=5.0,
        fog_density=100.0,
        fog_distance=5.0,
        fog_falloff=1.0,
        wetness=10.0,
        scattering_intensity=0.2,
        mie_scattering_scale=0.7,
        rayleigh_scattering_scale=0.3,
        dust_storm=0.0,
        sun_azimuth_angle=45.0,
        sun_altitude_angle=5.0
    ),

    "tormenta_tropical": carla.WeatherParameters(
        cloudiness=100.0,
        precipitation=100.0,
        precipitation_deposits=100.0,
        wind_intensity=80.0,
        fog_density=70.0,
        fog_distance=20.0,
        fog_falloff=1.0,
        wetness=100.0,
        scattering_intensity=0.2,
        mie_scattering_scale=0.5,
        rayleigh_scattering_scale=0.3,
        dust_storm=0.0,
        sun_azimuth_angle=120.0,
        sun_altitude_angle=-5.0
    ),

    "deslumbramiento_sol_bajo": carla.WeatherParameters(
        cloudiness=10.0,
        precipitation=0.0,
        precipitation_deposits=0.0,
        wind_intensity=10.0,
        fog_density=5.0,
        fog_distance=200.0,
        fog_falloff=0.2,
        wetness=0.0,
        scattering_intensity=0.7,
        mie_scattering_scale=0.2,
        rayleigh_scattering_scale=0.4,
        dust_storm=0.0,
        sun_azimuth_angle=90.0,
        sun_altitude_angle=2.0
    ),

    "noche_sin_luna": carla.WeatherParameters(
        cloudiness=100.0,
        precipitation=0.0,
        precipitation_deposits=0.0,
        wind_intensity=0.0,
        fog_density=0.0,
        fog_distance=0.0,
        fog_falloff=1.0,
        wetness=0.0,
        scattering_intensity=0.0,
        mie_scattering_scale=0.0,
        rayleigh_scattering_scale=0.0,
        dust_storm=0.0,
        sun_azimuth_angle=180.0,
        sun_altitude_angle=-90.0
    ),

    "calima_densa": carla.WeatherParameters(
        cloudiness=30.0,
        precipitation=0.0,
        precipitation_deposits=0.0,
        wind_intensity=50.0,
        fog_density=60.0,
        fog_distance=25.0,
        fog_falloff=1.2,
        wetness=0.0,
        scattering_intensity=0.9,
        mie_scattering_scale=1.0,
        rayleigh_scattering_scale=0.3,
        dust_storm=80.0,
        sun_azimuth_angle=70.0,
        sun_altitude_angle=30.0
    ),

    "noche_con_niebla": carla.WeatherParameters(
        cloudiness=100.0,
        precipitation=0.0,
        precipitation_deposits=0.0,
        wind_intensity=10.0,
        fog_density=80.0,
        fog_distance=10.0,
        fog_falloff=1.0,
        wetness=0.0,
        scattering_intensity=0.1,
        mie_scattering_scale=0.5,
        rayleigh_scattering_scale=0.2,
        dust_storm=0.0,
        sun_azimuth_angle=0.0,
        sun_altitude_angle=-80.0
    )
}

# Selección del escenario deseado
escenario_deseado = "deslumbramiento_sol_bajo"  # Cambiar por otro nombre según se desee

# Aplicar condiciones climáticas
world.set_weather(escenarios_visibilidad[escenario_deseado])

print(f"Escenario aplicado: {escenario_deseado}")

