"""
The start of something healthy
"""

goals_diary = {
    "Number of Meals": 3,
    "Resting Heartbeat": 89,
    "Calorie Goal": 2000,
    "Miles Walked": 4,
    "Hours Slept": 7,
    "Weight": 140
}

# results()
# main()


number = int(input("Please enter the amount of meals you had today:"))

if number in goals_diary >= 3:
    print(f"{number} is not a great number for today\n")
else:
    print(f"{number} is what you should be having daily, nice!\n")

    resting_heartbeat = int(input("Please enter your heartbeat figure:"))

if resting_heartbeat in goals_diary >= 89:
    print(f"{resting_heartbeat} is above your daily target\n")
    print("Please consider exercising more to improve this\n")
else:
    print(f"{resting_heartbeat} is not exactly what you want to see!\n")

calories = int(input("Please enter your calorie intake for today:"))

if calories in goals_diary <= 2001:
    print(f"{calories} is exactly what you want to see!\n")
else:
    print(f"{calories} is going towards something too high for you\n")

miles_walked = int(
    input("Please enter the aount of miles walked for today:"))

if miles_walked in goals_diary:
    print(f"{miles_walked} is exactly what you want to see!\n")
else:
    print(f"{miles_walked} has not reached your goal, walk a bit more\n")

hours_slept = int(input("Please enter the amount of slept last night:"))

if hours_slept in goals_diary <= 6:
    print(f"{hours_slept} is not exactly what you want to see!\n")
else:
    print(f"{hours_slept} has exceeded your daily target, nice one!\n")

weight = int(input("Please enter the daily end weight:"))

if weight in goals_diary <= 140:
    print(f"{weight} means you are on track, \n")
    print("But remember, you shouldnt over do it")
else:
    print(f"{weight} means you need to stick to your diary better\n")
