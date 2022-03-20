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

if number in goals_diary >= 4:
    print(f"{number} is not a great number for today")
else:
    print(f"{number} is what you should be having daily, nice!")

resting_heartbeat = int(input("Please enter your heartbeat figure:"))

if resting_heartbeat in goals_diary >= 89:
    print(f"{resting_heartbeat} is going towards something too high for you")
else:
    print(f"{resting_heartbeat} is not exactly what you want to see!")

calories = int(input("Please enter your calorie intake for today:"))

if calories in goals_diary >= 2001:
    print(f"{calories} is exactly what you want to see!")
else:
    print(f"{calories} is going towards something too high for you")

miles_walked = int(input("Please enter the aount of miles walked for today:"))

if miles_walked in goals_diary > 4:
    print(f"{miles_walked} is exactly what you want to see!")
else:
    print(f"{miles_walked} has not reached your goal, walk a bit more")


hours_slept = int(input("Please enter the amount of slept last night:"))

if hours_slept in goals_diary <= 6:
    print(f"{hours_slept} is not exactly what you want to see!")
else:
    print(f"{hours_slept} has exceeded your daily target, nice one!")

weight = int(input("Please enter the daily end weight:"))

if weight in goals_diary <= 140:
    print(f"{weight} means you are on track, but remember dont over do it")
else:
    print(f"{weight} means you need to stick to your diary better")
