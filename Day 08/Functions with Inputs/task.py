def life_in_weeks (age):
    weeks_90_years_old = 4680
    weeks_my_age = age * 52
    weeks_until_death = weeks_90_years_old - weeks_my_age
    print(f"You have {weeks_until_death} left to live")

life_in_weeks(30)