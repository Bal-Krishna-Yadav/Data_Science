import phonenumbers
from phonenumbers import geocoder

# Input: Mobile number with country code
number = input("Enter mobile number with country code (e.g. +919876543210): ")

# Parse the number
parsed_number = phonenumbers.parse(number)

# Get location
location = geocoder.description_for_number(parsed_number, "en")

# Display result
print("Location:", location)
