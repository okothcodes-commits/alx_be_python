# daily_reminder.py

# --- 1. Prompt for Inputs ---

# Get the task description
task = input("Enter your task: ").strip()

# Loop to get a valid priority
priority = ""
while priority not in ["high", "medium", "low"]:
    priority = input("Priority (high/medium/low): ").lower().strip()
    if priority not in ["high", "medium", "low"]:
        print("   Invalid input. Please enter 'high', 'medium', or 'low'.")

# Loop to get a valid time-bound status
time_bound = ""
while time_bound not in ["yes", "no"]:
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    if time_bound not in ["yes", "no"]:
        print("   Invalid input. Please enter 'yes' or 'no'.")

print() # Add a blank line for readability

# --- 2. Process and Provide Reminder ---

# Use Match Case to check the priority
match priority:
    case "high":
        # Use an if statement to check if it's time-bound
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Make sure to complete it today.")
    
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Try to complete it soon.")

    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task, but it is time-bound. Complete it when you can.")
        else:
            # This matches the user's example output for low/no
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")