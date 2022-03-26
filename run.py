"""
The start of something healthy
"""

goals_diary = {
    "number_of_meals": 3,
    "resting_heartbeat": 89,
    "calorie_goal": 2000,
    "miles_walked": 4,
    "hours_slept": 7,
    "weight": 140
}


def start_diary():
    """
    We want you input the values that are true to yourself. Make sure you
    are accurate for the best results. This will take you to the first input
    for the diary you create.
    """

    print("Welcome to HEXAHEALTH your personal health diary\n")
    print("Input your own figures to see how you stack up\n")
    print("We supply you a guidance diary for you to compare to\n")
    print("Ready? Start now\n")

    name = input("Please type your name and hit the enter key:\n")

    while not name:
        print("Please enter your name to begin the entries\n")
    else:
        print("Please enter your name\n")

    restart_diary = True

    while restart_diary:
        diary_enteries = input("Are you ready to begin? y/n\n")

        if diary_enteries.lower() == "y":
            print("Lets go\n")
            break
        elif diary_enteries.lower() == "n":
            print("Type 'y' when you are ready to begin\n")
        else:
            print("That is not a valid option\n")


while True:
    number = int(input("Please enter the amount of meals you had today:"))

    if number >= goals_diary['number_of_meals']:
        print(f"{number} is not a great number for today\n")
    else:
        print(f"{number} is what you should be having daily, nice!\n")

    resting_heartbeat = int(input("Please enter your heartbeat figure:"))

    if resting_heartbeat >= goals_diary['resting_heartbeat']:
        print(f"{resting_heartbeat} is above your daily target\n")
        print("Please consider exercising more to improve this\n")
    else:
        print(f"{resting_heartbeat} is not exactly what you want to see!\n")

    calories = int(input("Please enter your calorie intake for today:"))

    if calories <= goals_diary['calorie_goal']:
        print(f"{calories} is exactly what you want to see!\n")
    else:
        print(f"{calories} is going towards something too high for you\n")

    miles_walked = int(
        input("Please enter the amount of miles walked for today:"))

    if miles_walked >= goals_diary['miles_walked']:
        print(f"{miles_walked} is exactly what you want to see!\n")
    else:
        print(f"{miles_walked} has not reached your goal, walk a bit more\n")

    hours_slept = int(
        input("Please enter the amount of hours slept last night:"))

    if hours_slept <= goals_diary['hours_slept']:
        print(f"{hours_slept} is not exactly what you want to see!\n")
        print("Get some more rest tonight!\n")
    else:
        print(f"{hours_slept} has exceeded your daily target, nice one!\n")

    weight = int(input("Please enter the daily end weight:"))

    if weight <= goals_diary['weight']:
        print(f"{weight} means you are on track, \n")
        print("But remember, you shouldnt over do it\n")
    else:
        print(f"{weight} means you need to stick to your diary better\n")

    LEAVE_DIARY = True

    while True:
        print("Well done on completing todays diary, go again tomorrow\n")
        exit_diary = input("Are you sure you want to leave? y/n\n")

        if exit_diary.lower() == "y":
            print("Ok remember to come back tomorrow\n")
            break
        elif exit_diary.lower() == "n":
            print("Type 'y' to enter another diary entry\n")
        else:
            print("That is not a valid option\n")
