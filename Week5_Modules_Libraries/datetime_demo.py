import datetime

now = datetime.datetime.now()
print("Current date and time:", now)

print("Date only:", now.date())
print("Time only:", now.time())

# Formatting
print("Formatted:", now.strftime("%d-%m-%Y %H:%M:%S"))
