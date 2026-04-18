"""
we are today writing a program, that does the following:
1. Takes the date from the user, creates a file with that name
2. then asks the user how he/she feels out of 10
3. finally asks for freetext to write the thought
4. adds both 2 and 3 in the file
"""
# 1. Takes the date from the user, creates a file with that name
date_today = input("Please enter today's date: ")

# create a file with the above name:

with open(f"{date_today}.txt", 'w') as file:
    mood_meter = int(input("Out of 10, please rate your mood: "))
    today_thought = input("Let your thoughts flow: ").capitalize()
    file.write(f"Out of 10, today's rating is {mood_meter}.\n")
    file.write(today_thought)
