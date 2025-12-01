# Maths Stuff with Python
# Author: Ubial
# 12 November 2025

import math
import time

# Do math things with Python
# Machines are good at crunching numbers - faster
# and more accurately than most humans!
# Create a small program that calculates something useful
# to you (making you smile is useful). It should take
# user input, at use at least one of the number
# operators we saw in class: + / * -. You may modify one
# of your previous exercises to include calculations,
# if you wish.


def pythagorean_theorem(a: int, b: int) -> int:
    return math.sqrt(a**2 + b**2)


def main():
    time_initial = time.time()

    while True:
        # stop when 5 second has passed
        time_final = time.time()

        time_difference = time_final - time_initial

        if time_difference >= 5:
            break

    print(
        f"{time_difference} seconds has passed. Please shut down your game and computer."
    )

    while True:
        # stop when 5 second has passed
        time_final = time.time()

        time_difference = time_final - time_initial

        if time_difference >= 10:
            break

    print(f"{time_difference} seconds has passed. Computer will self destruct now.")


if __name__ == "__main__":
    main()
