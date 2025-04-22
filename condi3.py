import phonenumbers
from phonenumbers import geocoder

# Mobile number input (with country code)
number = input("Enter mobile number with country code (e.g. +919876543210): ")

# Parse the number
parsed_number = phonenumbers.parse(number)

# Get location (region)
location = geocoder.description_for_number(parsed_number, "en")

print("Approximate Location:", location)
