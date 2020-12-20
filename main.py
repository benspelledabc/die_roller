import random


def custom_roll(die_count, die_sides):
    # xDy (discard ones, so we are going 2-y for the rolls
    loop_counter = 1
    return_value = 0
    roll_values = []
    while loop_counter <= die_count:
        roll = random.randint(2, die_sides)
        roll_values.append(roll)
        return_value += roll
        loop_counter += 1

    return return_value


number_of_rolls_needed = 6
number_of_rolls_obtained = 0
final_rolls = []

while number_of_rolls_needed > number_of_rolls_obtained:
    # custom_roll(3, 6)  # 3d6
    final_rolls.append(custom_roll(3, 6))
    # print(final_rolls[number_of_rolls_obtained])
    number_of_rolls_obtained += 1

# printing the list using loop
print("Rolling 3d6, ignoring 1s, {0} times.".format(number_of_rolls_needed))
print(*final_rolls, sep=", ")
