# Exercise 1: Filter and Count
# 
# You are given a list of temperatures in Celsius:
temperatures = [22, 18, 30, 15, 25, 19, 28, 16]
#
# Task:
# 1. Create a new list called 'warm_days' containing only temperatures >= 20
warm_days = []

for i in range(len(temperatures)):
    if temperatures[i] >= 20: 
        warm_days.append(temperatures[i])

# 2. Print how many warm days there were
print(f"Number of warm days: {len(warm_days)}")

# 3. Print the warm_days list
print(f"Warm days: {warm_days}")
#
# Expected output:
# Number of warm days: 5
# Warm days: [22, 30, 25, 19, 28]
