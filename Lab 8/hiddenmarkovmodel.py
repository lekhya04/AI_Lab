states = ["Rain", "Sun"]
rain = 0.60                
sun = 0.40                  
rain_to_rain = 0.70
sun_to_rain = 0.40
rain_to_sun = 0.30
sun_to_sun = 0.60
umbrella_if_rain = 0.90
umbrella_if_sun = 0.20
no_umbrella_if_rain = 0.10
no_umbrella_if_sun = 0.80
observations = ["U", "U", "N"]
for day in range(len(observations)):
    observation = observations[day]
    if day > 0:                    # not before day 1
        next_rain = rain * rain_to_rain + sun * sun_to_rain
        next_sun = rain * rain_to_sun + sun * sun_to_sun
        rain = next_rain
        sun = next_sun
    if observation == "U":
        rain_score = rain * umbrella_if_rain
        sun_score = sun * umbrella_if_sun
    else:
        rain_score = rain * no_umbrella_if_rain
        sun_score = sun * no_umbrella_if_sun
    evidence = rain_score + sun_score
    rain = rain_score / evidence
    sun = sun_score / evidence
    print("Day", day + 1, "observation:", observation,
          "Rain:", round(rain, 4), "Sun:", round(sun, 4))