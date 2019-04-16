# Write a function `is_leap_year` that takes a year as a parameter
#   -->**RETURNS**<-- True if the year is a leap year, False otherwise.
# The logic-chain is somewhat similar to the Sherlock problem.

# Don't forget to reach out for help after your own due diligence

def is_leap(year):
    if year % 4 != 0:
        result = False
    elif year % 400 == 0:
        result = True
    elif year % 100 == 0:
        result = False
    else:
        result = True
    
    return result
    
    
print(is_leap(2056))
