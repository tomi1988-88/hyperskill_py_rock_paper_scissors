from random import choice

STANDARD_OPTIONS = "rock,paper,scissors"
POINTS = {None: 50, True: 100, False: 0}


class Options:
    def __init__(self, str_opts):
        self.options = str_opts.split(",")

    def who_wins(self, players_choice, computer):

        if players_choice == computer:
            return None

        temp_list = self.options.copy()
        index = self.options.index(players_choice)      # we need to find player's choice ofc
        center_point = len(self.options) // 2       # reference "point"

        # if our choice is on "the right" side of the center
        # it is enough to catch what it beats (what lies on its left)
        if index >= center_point:
            wins_to = temp_list[index - center_point:index]

        # if the choice lies on "the left" we can simply delete what is unnecessary
        # (players choice and what beats it)
        else:
            del temp_list[index:index + center_point + 1]
            wins_to = temp_list

        return True if computer in wins_to else False


curr_player = input()
print(f"Hello, {curr_player}")

with open("rating.txt", "r") as file:
    rating = [x.strip("\n").split() for x in file.readlines()]
    rating = {x[0]: int(x[1]) for x in rating}
    rating = rating.get(curr_player, 0)

custom_opts = input("Custom options (if empty standard rock, paper, scissors):")
print("Okay, let's start")

options = Options(custom_opts if custom_opts else STANDARD_OPTIONS)

while True:
    user_choice = input("Enter your choice:")

    if user_choice == "!exit":
        print("Bye!")
        break

    elif user_choice == "!rating":
        print(f"Your rating: {rating}")
        continue

    elif user_choice not in options.options:
        print("Invalid input")
        continue

    comp_choice = choice(options.options)

    winner = options.who_wins(user_choice, comp_choice)

    if winner is None:
        print(f"There is a draw ({comp_choice})")
        rating += POINTS.get(winner)
    elif winner:
        print(f"Well done. The computer chose {comp_choice} and failed")
        rating += POINTS.get(winner)
    else:
        print(f"Sorry, but the computer chose {comp_choice}")
