def main():
    path = "data/sfu_best_cmpt120.csv"
    file = open(path)
    header_row = file.readline()

    quesadaCS = 0
    quadalupeMBC = 0

    for line in file:
        info = line.split(",")
        fave_burrito = info[5]

        if fave_burrito == "Quesada (Cornerstone)":
            quesadaCS += 1
        elif fave_burrito == "Guadalupe (MBC)":
            quadalupeMBC += 1

    # display results
    print("--------------------")
    print("Results:")
    print(f"Quesada (Cornerstone) votes: {quesadaCS}")
    print(f"Quadalupe (MBC): {quadalupeMBC}")

    file.close()


if __name__ == "__main__":
    main()
