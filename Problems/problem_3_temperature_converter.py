"""
Given a temperature in Fahrenheit, return the temperature in Celsius
"""
# Ask for a temperature in Fahrenheit
temp_f = int(input("what is the Temp is F "))
print(temp_f)

# Calculate it in Celsius
temp_c = (int(temp_f) - 32) * 5/9
# Tell the user what it is
print(" the temperature in c is " + str(temp_c))
