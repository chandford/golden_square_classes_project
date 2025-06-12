from lib.design_and_test_drive_complex_function import check_age, dob_format_checker

import pytest 
from datetime import datetime

def test_dob_format_checker():
    assert dob_format_checker("1993-10-21") == True
    assert dob_format_checker("1993") == False
    assert dob_format_checker("21-10-1993") == False


def test_check_age_returns_access_granted_message_when_user_is_over_16():
    assert check_age("1993-10-21") == "Access granted!"
    assert check_age("2005-01-13") == "Access granted!"


def test_check_age_returns_access_denied_message_when_user_is_under_16():
    assert check_age("2014-01-01") == "Access denied! Current age: 11. The required age is 16."
    assert check_age("2010-01-01") == "Access denied! Current age: 15. The required age is 16."

def test_check_age_raises_exception_when_dob_of_wrong_type():
    with pytest.raises(Exception) as err:
        check_age(18) # int
    error_message = str(err.value)
    assert error_message == "Date of birth in incorrect format. Provide a string in the format `YYYY-MM-DD`"

    with pytest.raises(Exception) as err:
        check_age(datetime.today()) #datetime object
    error_message = str(err.value)
    assert error_message == "Date of birth in incorrect format. Provide a string in the format `YYYY-MM-DD`"

def test_check_age_raises_exception_when_in_wrong_format():
    with pytest.raises(Exception) as err:
        check_age("2001")
    error_message = str(err.value)
    assert error_message == "Date of birth in incorrect format. Provide a string in the format `YYYY-MM-DD`"

    with pytest.raises(Exception) as err:
        check_age("01-02-2001")
    error_message = str(err.value)
    assert error_message == "Date of birth in incorrect format. Provide a string in the format `YYYY-MM-DD`"
