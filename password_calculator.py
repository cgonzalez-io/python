import math
# Given values
total_characters = 10 + 26 + 26 + 10  # Total possible characters for each position
password_length = 16  # Length of the password

# Total number of valid passwords
total_passwords = total_characters ** password_length

# Testing rate
passwords_per_second = 1e12  # 1 trillion

# Time in seconds to test all passwords
time_seconds = total_passwords / passwords_per_second

# Convert time to years
seconds_per_year = 365 * 24 * 60 * 60  # 1 year in seconds
time_years = time_seconds / seconds_per_year
print(time_years)

# Round to the nearest power of 10
rounded_time_years = 10 ** round(math.log10(time_years))
print(rounded_time_years)
