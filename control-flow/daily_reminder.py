# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Create the reminder message
reminder = f"'{task}' is a {priority} priority task."

# Use Match Case for priority handling
match priority:
    case "high":
        reminder += " This task requires immediate attention today!"
    case "medium":
        reminder += " Consider completing it soon."
    case "low":
        reminder += " Note: You can complete it when you have free time."
    case _:
        reminder = "Invalid priority."

# Modify reminder based on time sensitivity
if time_bound.lower() == "yes":
    reminder = reminder.replace("This task requires immediate attention today!", "This task requires immediate attention today!")

# Provide the customized reminder
print(f"Reminder: {reminder}")
