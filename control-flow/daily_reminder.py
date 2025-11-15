# daily_reminder.py

# Prompt the user for the task description
task = input("Enter your task: ")

# Prompt for the task's priority level (high, medium, low)
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound (yes or no)
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using match-case statement
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print("\nReminder:", reminder)

# Congratulations message after the task reminder
print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
