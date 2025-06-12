from lib.design_and_test_drive_complex_function import check_age
import pytest 
import datetime

def test_check_age_returns_access_granted_message_when_user_is_over_16():
    assert check_age("1993-10-21") == "Access granted!"

def test_check_age_returns_access_denied_message_when_user_is_under_16():
    assert check_age("2014-01-01") == "Access denied! Current age: 11. The required age is 16."


"""
Given a DOB of the wrong type,
it returns an empty list
"""
# check_age(datetime.today()) 
# # => "Date of birth in incorrect format. Provide a string in the format `YYYY-MM-DD`"


"""
Given a DOB in the wrong format,
it returns an empty list
"""
# check_age("01-01-2024") 
# # => "Date of birth in incorrect format. Provide a string in the format `YYYY-MM-DD`"