# author: julian
# 5 nov 2025
#
#
# Create an algorithm to gather
# data to fimd the most popular
# bubble tea place around us
# version 1
from asyncio import set_event_loop_policy


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
    spoiled_votes = 0

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
    elif vote == "c":
        bubble_waffle += 1
    elif vote == "d":
        gong_cha += 1
    else:
        spoiled_votes += 1

    # tally
    # gvie the raw score
    # show the scores of coco...... etc
    print(f"CoCo votes: {coco}")
    print(f"Chatime votes: {chatime}")
    print(f"BUBBLE WAFFEL votes: {bubble_waffle}")
    print(f"Gong Cha votes: {gong_cha}")
    print(f"Spoiled votes: {spoiled_votes}")
    # give score as percentage

    coco_percentage = coco / (coco + chatime + bubble_waffle + gong_cha + spoiled_votes)
    print(f"CoCo Percentage: {coco_percentage * 100}%")
    chatime_percentage = chatime / (
        coco + chatime + bubble_waffle + gong_cha + spoiled_votes
    )
    print(f"Chatime Percentage: {chatime_percentage * 100}%")
    bubble_waffle_percentage = bubble_waffle / (
        coco + chatime + bubble_waffle + gong_cha + spoiled_votes
    )
    print(f"CoCo Percentage: {bubble_waffle_percentage * 100}%")
    gong_cha_percentage = gong_cha / (
        coco + chatime + bubble_waffle + gong_cha + spoiled_votes
    )
    print(f"CoCo Percentage: {gong_cha_percentage * 100}%")


#
#
def main():
    pass


if __name__ == "__main__":
    main()


def vote_open_choice():
    """Keeps track dynamically of user's choice.
    Note: choices must match text exactly (case is not sensitive)"""

    votes = {}  # holds vote information    key     -> value
    #                           place   -> num votes

    for _ in range(NUM_VOTERS):
        # Ask the user what their fave
        os.system("clear")
        cur_vote = (
            input("What's your favourite local bubbble tea cafe? ")
            .lower()
            .strip(",.?! ")
        )

        # Checks if current place is in the votes dictionary
        # If it doesn't exist, initialize the key-value pair
        if cur_vote not in votes:
            votes[cur_vote] = 1
        else:
            votes[cur_vote] += 1

    # Print the results
    print("-------------------------------------")
    print("Results:")

    # By default, iterating over a dictionary gives you the keys
    for place in votes:
        # Print the raw score and percentage for each key in the dictionary
        percentage = votes[place] / NUM_VOTERS * 100

        print(
            f"{place.capitalize()} votes: {votes[place]} | percentage: {percentage}% of the vote"
        )

    print("-------------------------------------")
