def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    return {
        'Charlotte': 183,
        'Tampa': 220,
        'Pittsburgh': 222,
        'Los Angeles': 475
    }[city]


def rental_car_cost(days):
    daily = days * 40
    if days >= 7:
        return daily - 50
    elif days >= 3:
        return daily - 20
    else:
        return daily


def trip_cost(city, days, spending_money):
    daily_cost = rental_car_cost(days) + hotel_cost(days)
    return plane_ride_cost(city) + daily_cost + spending_money


print trip_cost('Los Angeles', 5, 600)
