if __name__ == "__main__":
    import sys
    import statistics

    if len(sys.argv) < 2:
        print("Arguments required.")
        exit()


    else:
        temps = list(map(int, sys.argv[1:]))
        max_temp = max(temps)
        min_temp = min(temps)
        mean_temp = statistics.mean(temps)
        mean_temp = round(mean_temp, 2)
        print(f"Max value {max_temp}C")
        print(f"Min value {min_temp}C")
        print(f"Mean temperature {mean_temp}C")