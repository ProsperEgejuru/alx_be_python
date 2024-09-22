# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder_message = f"Note: '{task}' is a {priority} priority task."

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder_message = f"Reminder: '{task}' is a high priority task"
        if time_bound == "yes":
            reminder_message += " that requires immediate attention today!"
    case "medium":
        reminder_message = f"Note: '{task}' is a medium priority task."
        if time_bound == "yes":
            reminder_message += " Please try to complete it soon."
    case "low":
        reminder_message += " Consider completing it when you have free time."
        if time_bound == "yes":
            reminder_message = f"Reminder: '{task}' is a low priority task, but it is time-bound. Please find time to do it."
    case _:
        reminder_message = "Invalid priority level entered."

# Output the customized reminder
print(reminder_message)
