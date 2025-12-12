# bgtjljtgtrkljg
# author: julian
# december 1


def part_one():
    cur_loc = 50
    zeronum = 0
    # read every line in the instructions
    with open("data/aoc-2025-day1.txt") as f:
        for line in f:
            # instruction example "R10" -> right 10
            direction = line[0]
            distance = int(line[1:])

            # if we go RIGHT -> add
            if direction == "R":
                cur_loc += distance
            # if we go left -> subtract
            else:
                cur_loc -= distance

            # if we land on zero keep track of it
            if cur_loc > 100:
                cur_loc -= 100

            if cur_loc < 0:
                cur_loc += 100

            # print how many times we landed on zero
            if cur_loc % 100 == 0:
                zeronum += 1

        print(zeronum)


if __name__ == "__main__":
    part_one()
