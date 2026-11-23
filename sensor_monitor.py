import csv
import random
import matplotlib.pyplot
import numpy

def ask_int(prompt): 
    """Heel getal en geeft error als het niet heel of een getal is"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error! voer een geldig geheel getal in")


def ask_float(prompt): 
    """kommagetal en geeft error als het niet en kommagetal of een getal is"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error! voer een geldig getal in")

def get_user_input(): 
    """Vraagt alle instellingen voor metingen"""
    sensor_type = input("Sensortype (temperature/light): ").strip()
    if not sensor_type:
        sensor_type = "sensor"

    while True:
        count = ask_int("Aantal metingen: ")
        if count > 0:
            break
        print("Error! het aantal metingen moet groter dan 0 zijn")

    while True:
        min_val = ask_float("Minimale sensorwaarde: ")
        max_val = ask_float("Maximale sensorwaarde: ")
        if min_val < max_val:
            break
        print("Error! de minimale waarde moet kleiner zijn dan de maximale waarde.")

    threshold = ask_float("Waarschuwingsdrempel (alert threshold): ")
    return sensor_type, count, min_val, max_val, threshold


def generate_readings(count, min_val, max_val, seed=42): 
    """Genereert de sensor metingen."""
    random.seed(seed)
    readings = []
    for _ in range(count):
        value = round(random.uniform(min_val, max_val), 2)
        readings.append(value)
    return numpy.array(readings)