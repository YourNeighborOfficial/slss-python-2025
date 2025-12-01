# Big Data
# Author: Ubial
# 17 November

# Process files
# Ingest large data
# Make sense of data


def main():
    # Get the file
    path = "data/sfu_best_cmpt120.csv"
    file = open(path)
    header_row = file.readline()

    # get information about the fave pizza place
    uncle_fatihs = 0
    club_ilia = 0
    pizza_hut = 0
    # read the rest of the file
    for line in file:
        # fave pizza is in column 5 (index 4)
        # each line is a string
        # split the string wherever a , is
        # convert from string -> list
        info = line.split(",")
        fave_pizza = info[4]

        if fave_pizza == "Uncle Fatih's":
            uncle_fatihs += 1
        elif fave_pizza == "Club Ilia":
            club_ilia += 1
        elif fave_pizza == "Pizza Hut":
            pizza_hut += 1

    # display results
    print("--------------------")
    print("Results:")
    print(f"Uncle Fatih's votes: {uncle_fatihs}")
    print(f"Club Ilia votes: {club_ilia}")
    print(f"Pizza Hut votes: {pizza_hut}")

    file.close()


if __name__ == "__main__":
    main()
