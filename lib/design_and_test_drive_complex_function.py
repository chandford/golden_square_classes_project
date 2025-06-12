from datetime import datetime

def dob_format_checker(date_of_birth):
    if len(date_of_birth) == 10 and date_of_birth[4] == '-':
        year = date_of_birth[0:4]
        month = date_of_birth[5:7]
        day = date_of_birth[8:10]
        return year.isnumeric() and month.isnumeric() and day.isnumeric()

    return False

def check_age(date_of_birth):
    if type(date_of_birth) == str:
            if dob_format_checker(date_of_birth) == True:
        
                today_dt = datetime.today()
                dob_dt = datetime.strptime(date_of_birth, "%Y-%m-%d")

                age_dt = today_dt - dob_dt
                total_days = age_dt.days

                user_age = total_days // 365

                if user_age > 16:
                    return "Access granted!"
                return f"Access denied! Current age: {user_age}. The required age is 16."
            
    raise Exception("Date of birth in incorrect format. Provide a string in the format `YYYY-MM-DD`")
