import re

valid_contact_numbers = re.compile(r"(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}")
phone_number_list = ["2124567890",
                     "212-456-7890",
                     "(212)456-7890",
                     "(212)-456-7890",
                     "212.456.7890",
                     "212 456 7890",
                     "+12124567890",
                     "+12124567890",
                     "+1 212.456.7890",
                     "+212-456-7890",
                     "1-212-456-7890",
                     "+91 8208484027",
                     "+00 abc 91"]
result = [x for x in phone_number_list if re.findall(valid_contact_numbers, x)]

# It will print only valid contact numbers
print("Valid Contact Numbers are", result)
