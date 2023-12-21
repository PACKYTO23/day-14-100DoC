# / # / # PROJECT OF DAY 14 # / # / #

import random
from art import logo, vs
from game_data import data
from replit import clear


def compare_followers():
    most_followers = 0
    for i in selection_group:
        if i['follower_count'] > most_followers:
            most_followers = i['follower_count']
    return most_followers


def check_option():
    popular_index = ""
    for i in selection_group:
        if i['follower_count'] == compare_followers():
            popular_index = selection_group.index(i)
    return popular_index


def game_continue():
    if check_option() == 0 and option == "a":
        return True
    elif check_option() == 1 and option == "b":
        return True


score = 0
a = random.choice(data)
b = random.choice(data)
selection_group = [a, b]

print(logo)

higher_lower = True
while higher_lower:
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Compare B: {b['name']}, {b['description']}, from {b['country']}.")

    option = input("Who has more followers? Type 'A' or 'B': ").lower()

    compare_followers()

    check_option()

    if game_continue():
        clear()
        a = b
        b = random.choice(data)
        selection_group = [a, b]
        score += 1
    else:
        higher_lower = False
        clear()
        print(f"Sorry, that's wrong! Final score: {score}.")
        again = input("Do you want to play again? Type 'y' or 'n': ").lower()
        if again == "y":
            a = random.choice(data)
            b = random.choice(data)
            selection_group = [a, b]
            score = 0
            higher_lower = True
        else:
            print("Hope we can play again soon!")

# 1-. Print Logo

# 2-. Compare first name, description and country

# 3-. Print VS

# 4-. Compare second name, description and country

# 5-. Receive input of option "A" or "B" (Value to compare is their "follower_count")

# 6-. If correct say correct and show score (Don't erase anything)

# 7-. Second name becomes first name and new second name appears

# 8-. If incorrect say wrong and show final score (Erase all except Logo)

# 9-. Ask to play again
