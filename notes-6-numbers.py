# author: julian
# 5 nov 2025
#
#
# Create an algorithm to gather
# data to fimd the most popular
# bubble tea place around us
# version 1
def vote_listed_choices():
    """display all voting choices
    users vote for their choice
    results will be printed"""
    CHOICES = ["A. CoCo", "B. Chatime", "C. Bubble Waffle", "D. Gong Cha"]
    # show all the bbt chocies
    print("vote for your favourite from the list")
    print("give the letter of your choice")
    for choice in CHOICES:
        print(choice)

    # buckets to hold all the votes
    coco = 0
    chatime = 0
    bubble_waffle = 0
    gong_cha = 0

    # ask the user for their choice
    vote = input("your vote: ").lower().strip(",.?! ")
    # add their vote to a running
    # tally
    # give some raw scores
    # give scores as a percentage
    #
    # version 2
    # ask the user what their fave
    # bbt place is
    # add their vote to a running
    if vote == "a":
        coco = coco + 1
    elif vote == "b":
        chatime += 1

    # tally
    # gvie the raw score
    # give score as percentage


#
#
def main():
    pass


if __name__ == "__main__":
    main()
