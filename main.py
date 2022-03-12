from datetype import Date

# Initial Score

date1_score = 0
date2_score = 0
date3_score = 0
date4_score = 0
date5_score = 0
date6_score = 0

# Data

date1 = Date("Chris", 23, True, True, True)
date2 = Date("Martin", 63, True, False, True)
date3 = Date("Jake", 43, False, True, True)
date4 = Date("Mo", 33, True, True, False)
date5 = Date("Ethan", 29, True, False, False)

# Age

if date1.age >= 40:
    date1_score = date1_score - 1
elif date1.age <= 30:
    date1_score = date1_score + 1
if date2.age >= 40:
    date2_score = date2_score - 1
elif date2.age <= 30:
    date2_score = date2_score + 1
if date3.age >= 40:
    date3_score = date3_score - 1
elif date3.age <= 30:
    date3_score = date3_score + 1
if date4.age >= 40:
    date4_score = date4_score - 1
elif date4.age <= 30:
    date4_score = date4_score + 1
if date5.age >= 40:
    date5_score = date5_score - 1
elif date5.age <= 30:
    date5_score = date5_score + 1

# Funny

if date1.funny:
    date1_score = date1_score + 1
if date2.funny:
    date2_Score = date2_score + 1
if date3.funny:
    date3_Score = date3_score + 1
if date4.funny:
    date4_Score = date4_score + 1
if date5.funny:
    date5_Score = date5_score + 1

# Attractive

if date1.attractive:
    date1_score = date1_score + 1
if date2.attractive:
    date2_Score = date2_score + 1
if date3.attractive:
    date3_Score = date3_score + 1
if date4.attractive:
    date4_Score = date4_score + 1
if date5.attractive:
    date5_Score = date5_score + 1

# Therapy

if date1.therapy:
    date1_score = date1_score + 1
if date2.therapy:
    date2_Score = date2_score + 1
if date3.therapy:
    date3_Score = date3_score + 1
if date4.therapy:
    date4_Score = date4_score + 1
if date5.therapy:
    date5_Score = date5_score + 1

# Question
Question = input("Would you like to input your own man?\n")
if Question == " no":
    print("Then here are your five options...\n")
    print(date1.name + "'s score was " + str(date1_score) + " out of 4")
    print(date2.name + "'s score was " + str(date2_score) + " out of 4")
    print(date3.name + "'s score was " + str(date3_score) + " out of 4")
    print(date4.name + "'s score was " + str(date4_score) + " out of 4")
    print(date5.name + "'s score was " + str(date5_score) + " out of 4")
else:
    date6_name = input("What is your mans name?\n")
    date6_age = input("What is your mans age?\n")
    date6_funny = input("Is your man funny?\n")
    date6_attractive = input("Is your man attractive?\n")
    date6_therapy = input("Does your man go to therapy?\n")

    if int(date6_age) >= 40:
        date6_score = date6_score - 1
    elif int(date6_age) <= 30:
        date6_score = date6_score + 1
    if date6_funny == "yes":
        date6_score = date6_score + 1
    if date6_attractive == "yes":
        date6_score = date6_score + 1
    if date6_therapy == "yes:":
        date6_score = date6_score + 1

    print(date6_name + "'s score was " + str(date6_score) + " out of 4")
