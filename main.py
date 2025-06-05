from collections import namedtuple
from math import sqrt
### 1-masala
# Car = namedtuple('Car', ['model', 'year', 'price'])
# cars = [
#     Car('BMW', 2020, 30000),
#     Car('Toyota', 2018, 20000),
#     Car('Audi', 2021, 35000)
# ]
# most_expensive_car = max(cars, key=lambda c: c.price)
# print("Eng qimmat mashina:", most_expensive_car)

### 2-masala
# Student = namedtuple('Student', ['name', 'age', 'grades'])
# students = [
#     Student('Ali', 20, [80, 85, 90]),
#     Student('Vali', 21, [70, 75, 80]),
#     Student('Gulbahor', 22, [90, 95, 85]),
#     Student('Dildora', 19, [88, 92, 84]),
#     Student('Jasur', 20, [78, 83, 77])
# ]
#
# average_grade = sum(sum(s.grades) for s in students) / (len(students) * 3)
# print(round(average_grade, 2))

### 3-masala
# Color = namedtuple('Color', ['red', 'green', 'blue'])
# color1 = Color(100, 150, 200)
# color2 = Color(50, 100, 150)
# mixed_color = Color(
#     (color1.red + color2.red) // 2,
#     (color1.green + color2.green) // 2,
#     (color1.blue + color2.blue) // 2
# )
# print(mixed_color)

### 4-masala
# Product = namedtuple('Product', ['name', 'quantity', 'price'])
# products = [
#     Product('Olma', 3, 5000),
#     Product('Banan', 2, 7000),
#     Product('Nok', 5, 4000),
#     Product('Uzum', 1, 10000)
# ]
#
# total_sum = sum(p.quantity * p.price for p in products)
# print(total_sum)

### 5-masala
# Coordinates = namedtuple('Coordinates', ['latitude', 'longitude'])
# point1 = Coordinates(41.3111, 69.2797)  # Toshkent
# point2 = Coordinates(39.6542, 66.9597)  # Samarqand
# distance = sqrt((point2.latitude - point1.latitude)**2 + (point2.longitude - point1.longitude)**2)
# print("Taxminiy masofa:", round(distance, 2), "gradus")

### 6-masala
# Time = namedtuple('Time', ['hours', 'minutes', 'seconds'])
# time1 = Time(1, 20, 15)
# time2 = Time(2, 45, 50)
# total_seconds = (time1.hours + time2.hours) * 3600 + (time1.minutes + time2.minutes) * 60 + (time1.seconds + time2.seconds)
# h = total_seconds // 3600
# m = (total_seconds % 3600) // 60
# s = total_seconds % 60
# summed_time = Time(h, m, s)
# print("Yig‘indi vaqt:", summed_time)

### 7-masala
# Animal = namedtuple('Animal', ['name', 'species', 'age'])
# animals = [
#     Animal('Leo', 'Lion', 5),
#     Animal('Misha', 'Bear', 7),
#     Animal('Kesha', 'Parrot', 2),
#     Animal('Sharik', 'Dog', 4),
#     Animal('Tom', 'Cat', 3)
# ]
# sorted_animals = sorted(animals, key=lambda a: a.age)
# print("Yosh bo‘yicha saralangan hayvonlar:")
# for animal in sorted_animals:
#     print(animal)

### 8-masala
# BankAccount = namedtuple('BankAccount', ['owner', 'balance'])
# accounts = [
#     BankAccount('Ali', 500000),
#     BankAccount('Vali', 800000),
#     BankAccount('Karim', 750000)
# ]
# richest = max(accounts, key=lambda acc: acc.balance)
# print("Eng boy hisob egasi:", richest)

### 9-masala
# Movie = namedtuple('Movie', ['title', 'director', 'year'])
# movies = [
#     Movie('Inception', 'Christopher Nolan', 2010),
#     Movie('The Matrix', 'Lana Wachowski', 1999),
#     Movie('Interstellar', 'Christopher Nolan', 2014),
#     Movie('Gladiator', 'Ridley Scott', 2000)
# ]
# recent_movies = [m for m in movies if m.year > 2000]
# print("2000-yildan keyingi filmlar:")
# for m in recent_movies:
#     print(m)

### 10-masala
# Computer = namedtuple('Computer', ['brand', 'RAM', 'CPU'])
# computers = [
#     Computer('HP', 8, 'i5'),
#     Computer('Lenovo', 16, 'i7'),
#     Computer('Dell', 16, 'i9'),
#     Computer('Asus', 8, 'Ryzen 5')
# ]
# cpu_power_order = {'i3': 1, 'i5': 2, 'i7': 3, 'Ryzen 5': 4, 'i9': 5}
# strongest = max(computers, key=lambda c: cpu_power_order.get(c.CPU, 0))
# print("Eng kuchli CPU’li kompyuter:", strongest)

### 11-masala
# import math
# def heron(a, b, c):
#     s = (a + b + c) / 2
#     area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#     return area

### 12-masala
# def correct_polish_letters(text):
#     polish_map = {
#         'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l',
#         'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
#         'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L',
#         'Ń': 'N', 'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z'
#     }
#     return ''.join(polish_map.get(char, char) for char in text)

### 13-masala
# def build_string(*args):
#     return f"I like {', '.join(args)}!"

### 14-masala
# def mouth_size(animal):
#     if animal.lower() == "alligator":
#         return "small"
#     else:
#         return "wide"

### 15-masala
# def count_char_occurrences(strng, char):
#     return strng.count(char)