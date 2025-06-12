# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.


## 2. Design the Function Signature

```python

import datetime
import dateutil 

def check_age(date_of_birth):

    # Checks user-inputed date-of-birth and provides informative message

    # Parameters:
    #     date_of_birth: a string in format `YYYY-MM-DD`

    # Returns:
    #     a message to under-age users to say their access is denied with current age and the required age (16)
    #     a message to users aged 16+ to say that access has been granted

    # Side effects: (state any side effects)
    #     generates an exception when the date of birth isn't the right type/format
    
    pass 
```

## 3. Create Examples as Tests

```python
# EXAMPLE

"""
Given a DOB when the user is old enough,
it returns a message saying access granted
"""
age_checker("1960-10-21") # => "Access granted!"


"""
Given a DOB when the user is not old enough,
it generates an exception"""
age_checker("2014-01-01") # => "Access denied! Current age: 11. The required age is 16."


"""
Given a DOB of the wrong type,
it returns an empty list
"""
age_checker(datetime.today()) # => "Date of birth in incorrect format. Provide a string in the format `YYYY-MM-DD`"


"""
Given a DOB in the wrong format,
it returns an empty list
"""
age_checker(datetime.today()) # => "Date of birth in incorrect format. Provide a string in the format `YYYY-MM-DD`"


```

## 4. Implement the Behaviour

