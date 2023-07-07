import re

# # Search Phone Number in string (Phone Number Format: xxxx-xxxxxxx)
# phone_number_regex = r'\d{4}-\d{7}'
# phone_number = input("Enter a Phone Number: ")
# match = re.search(phone_number_regex, phone_number)
# if match:
#     print("Phone number:", match.group(0))
# else:
#     print("No Phone Number found or Phone Number invalid")


# # Extracting all email addresses from a given string
# email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
# text = input('Enter a string: ')
# matches = re.findall(email_regex, text)
# if matches:
#     print("Email addresses:", matches)
# else:
#     print("No email foind")


# # Validating a password with specific requirements
# password_regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$'
# password = input("Enter Password: ")
# if re.match(password_regex, password):
#     print("Valid password")
# else:
#     print("Invalid password")

# # Splitting a string into words and removing punctuation
# sentence = input("Enter a string: ")
# words = re.findall(r'\b\w+\b', sentence)
# print("Words:", words)


# # Matching a date in the format YYYY-MM-DD
# date_regex = r'\d{2}-\d{2}-\d{4}'
# date = input("Enter date: ")
# match = re.match(date_regex, date)
# if match:
#     print("Date:", match.group(0))
# else:
#     print("No match")


# Extracting hashtags from a sentence
hashtag_regex = r'#\w+'
sentence = input("Enter a string: ")
hashtags = re.findall(hashtag_regex, sentence)
if hashtags:
    print("Hashtags:", hashtags)
else:
    print("No Hashtags found")