#3
lenght = float(input("Podaj długość prostokąta: "))
width = float(input("Podaj szerokość prostokąta: "))
area = lenght * width
print(f" obszar prostokąta z długością {lenght} i szerokośćą {width} prostokąta ruwnia się {area}  ")


#4

import random
distance = random.randint(1, 100000)
fuel_consumption = float(input("Podaj średnie spalanie samochodu ( w litrach na 100 km): "))
fuel_price_per_liter = 6.5
fuel_consumed = (distance / 100) * fuel_consumption
travel_cost = fuel_consumed * fuel_price_per_liter

print(f"Przejechana droga: {distance} km")
print(f"Przewidywane zużycie paliwa: {fuel_consumed:.2f} litrów")
print(f"Szacowane koszty podróży: {travel_cost:.2f} zł")





