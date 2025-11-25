# Data Analysis
# Author: Julian Sauvageau
#

# Analyse the data provided in class
def main():
    path = "data/NYC_Central_Park_weather_1869-2022.csv"
    file = open(path)
    header_row = file.readline()

    total_data = 0
    total_precipitation = 0
    total_min_temp = 0
    total_june_temp = 0

    for line in file:
        info = line.split(",")

        total_data += 1

        weather_date = info[0]
        precipitation = float(info[1])
        snow_inches = info[2]
        snow_depth = info[3]

        if info[4]:
            temp_min = float(info[4])

        if weather_date.split("-")[1] == "06":
            # This is june
            total_june_temp += float(info[5])

        # add the precipitation to the total

        total_precipitation = precipitation + total_precipitation

        total_min_temp = temp_min + total_min_temp

        rain_answer = total_precipitation / 56245
        min_temp_answer = total_min_temp / 56245
        f_to_c = (min_temp_answer - 32) / 1.8
        june_answer = total_june_temp / 4620
    # print(line.strip())

    # display results
    print("--------------------")
    print("Results:")
    print(f"There are {total_data} data points!")
    print(f"there was an average of {rain_answer} inches of rain!")
    print(
        f"the average minimum temperature was {min_temp_answer} Celsius or {f_to_c} Fahrenheit!"
    )
    print(f"the average maximum temperature in june was {june_answer} Celsius!")

    file.close()


if __name__ == "__main__":
    main()
