# daily_reminder.py

# Prompt the user for the task description
task = input("What is the task for today? ")

# Prompt for the priority level (high, medium, low)
priority = input("What is the priority level of the task? (high/medium/low): ").lower()

# Ask if the task is time-sensitive (yes/no)
time_bound = input("Is this task time-sensitive? (yes/no): ").lower()

# Process the task based on priority using match-case statement
match priority:
    case "high":
        reminder = f"Your task '{task}' is a HIGH priority."
    case "medium":
        reminder = f"Your task '{task}' is a MEDIUM priority."
    case "low":
        reminder = f"Your task '{task}' is a LOW priority."
    case _:
        reminder = f"Your task '{task}' has an unknown priority."

# Add time-sensitivity message if the task is time-sensitive
if time_bound == "yes":
    reminder += " This requires immediate attention today!"

# Print the customized reminder
print(reminder)
