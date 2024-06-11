

def parse_input(input_string):
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)
        # exits the app with a SystemExit exception and a status code of 1 to signal that something went wrong

#  ~~~ App's main code block ~~~

num_dice_input = input("How many dice do you want to roll? [1-6] ")
num_dice = parse_input(num_dice_input)