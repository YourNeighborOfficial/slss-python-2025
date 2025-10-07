# (string) methods
# # author: julian
# 6 october 2025

# ask the user about the weather
weather = input("Whats the weather like today")

if weather.lower().strip("!?,. ") == "rainy":
    # Rainy, RAINY, RAinY
    # Rainy!
    # Rainy.
    print("You should bring an umbrella")
else:
    print("ok")
