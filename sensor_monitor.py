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

def calculate_statistics(readings, threshold):
    """Berekent de statistieken"""
    stats = {
        "count": len(readings),
        "mean": numpy.mean(readings),
        "min": numpy.min(readings),
        "max": numpy.max(readings),
        "std": numpy.std(readings),
        "above_threshold": int(numpy.sum(readings > threshold)),
    }
    return stats


def show_statistics(sensor_type, stats, threshold):
    """Laat de statistieken zien"""
    print(f"\n--- Analyse voor sensor: {sensor_type} ---")
    print(f"Aantal metingen: {stats['count']}")
    print(f"Gemiddelde: {stats['mean']:.2f}")
    print(f"Minimum: {stats['min']:.2f}")
    print(f"Maximum: {stats['max']:.2f}")
    print(f"Standaardafwijking: {stats['std']:.2f}")
    print(f"Aantal boven drempel ({threshold}): {stats['above_threshold']}")


def find_outliers(readings, threshold):
    """Laat alle metingen boven de drempelwaarde zien"""
    outliers = []
    for index, value in enumerate(readings, start=1):
        if value > threshold:
            outliers.append((index, float(value)))

    if outliers:
        print("\nMetingen boven de drempelwaarde:")
        for sample_nr, value in outliers:
            print(f"  Sample {sample_nr}: {value:.2f}")
    else:
        print("\nGeen metingen boven de drempelwaarde gevonden.")
    return outliers