def city_info(city, country, population=None):
    """Возвращает строку с информацией о городе и стране, в которйо он находится."""
    if population:
        population = str(population)
        info = f'{city.title()}, {country.title()} - population {population[0]} {population[1:4]} {population[4:]}.'
    else:
        info = f'{city.title()}, {country.title()}'
    return info
