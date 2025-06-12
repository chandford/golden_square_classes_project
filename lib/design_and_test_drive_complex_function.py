from datetime import datetime, timedelta
# import dateutil 

def check_age(date_of_birth):
    today_dt = datetime.today()
    dob_dt = datetime.strptime(date_of_birth, "%Y-%m-%d")

    age_dt = today_dt - dob_dt
    total_days = age_dt.days

    user_age = total_days // 365

    if user_age > 16:
        return "Access granted!"
    return f"Access denied! Current age: {user_age}. The required age is 16."

    # generates an exception when the date of birth isn't the right type/format
