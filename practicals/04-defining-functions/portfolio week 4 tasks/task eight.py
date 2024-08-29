from statistics import mean


def temperatureCalculator():
    
    temperatures = [6, 4, 7, 2, 7, 9]
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = mean(temperatures)
    mean_temp = round(mean_temp, 2)

    print(f"Max value {max_temp}C")
    print(f"Min value {min_temp}C")
    print(f"Mean temperature {mean_temp}C")


temperatureCalculator()
