from datetime import date


def age(birthdate):
    today = date.today()

    # check if today's m/d comes before birth m/d
    md_check = ((today.month, today.day) < (birthdate.month, birthdate.day))

    # calculate the difference in years
    year_difference = today.year - birthdate.year

    age = year_difference - md_check

    return age;


# check Security Clearance Level
def sc_level():
    print("Security Clearance Levels: \n 1.High \n 2.Medium \n 3.Low \n")
    print("Enter your Security Clearance Level: ")
    scl_numb = int(input())

    if (scl_numb == 1):
        return True
    else:
        return False


# check user's qualification
def qualification():
    print("\nQualification: \n 1.Bachelors \n 2.Masters \n 3.Doctoral")
    print("Enter your qualification: ")
    qual = int(input())

    if (qual == 2 or qual == 3):
        return True
    else:
        return False


# check user's experience
def experience():
    print("\nEnter your experience in security domain: ")
    exp = int(input())

    if (exp >= 5):
        return True
    else:
        return False


# check user's level of position
def position_level():
    print(
        "\nPosition levels: \n 1.Assistant \n 2.Analyst \n 3.Associate \n 4.Deputy Manager \n 5.Manager \n 6.Sr Manager \n 7.Partner")
    print("Enter your position level choice: ")
    pos = int(input())

    if (pos >= 5):
        return True
    else:
        return False


# ---------------------------------------------------

# driver
user_age = age(date(2001, 11, 16))

# calling functions
bool1 = sc_level()
bool2 = qualification()
bool3 = experience()
bool4 = position_level()

if (user_age >= 18 and bool1 == True and bool2 == True and bool3 == True and bool4 == True):
    print("\nAccess Granted.")
else:
    print("\nAccess not granted.")










