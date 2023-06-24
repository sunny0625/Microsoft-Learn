def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
    
    distance_from_earth()

    distance_from_earth("Moon")

    distance_from_earth("Saturn")

    def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

days_to_complete(238855, 75)

total_days = days_to_complete(238855, 75)
round(total_days)

round(days_to_complete(238855, 75)) 