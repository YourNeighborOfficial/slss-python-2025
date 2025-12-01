def main():
    path = "data/sfu_best_cmpt120.csv"
    file = open(path)
    header_row = file.readline()

    pokebar = 0
    choppedleaf = 0
    garden = 0
    lunch = 0

    for line in file:
        info = line.split(",")
        fave_healthy = info[6]

        if fave_healthy == "Steve's Poke Bar":
            pokebar += 1
        elif fave_healthy == "Chopped Leaf":
            choppedleaf += 1
        elif fave_healthy == "Nature's garden":
            garden += 1
        elif fave_healthy == "Veggie Lunch":
            lunch += 1

    # display results
    print("--------------------")
    print("Results:")
    print(f"Steve's Poke Bar votes: {pokebar}")
    print(f"Chopped Leaf votes: {choppedleaf}")
    print(f"Nature's Garden: {garden}")
    print(f"Veggie Lunch: {lunch}")

    file.close()


if __name__ == "__main__":
    main()
