"""
This module contains the Habit analysis class.
"""

# create an analysis class
# with primary key, name, description, and frequency.


# https://realpython.com/python-functional-programming/
# https://softwareengineering.stackexchange.com/questions/421948/database-access-with-functional-programming

# def sample(repeat):
#     for i in range(repeat):
#         print("sample func as 1st class citizen")
#
# test = sample
#
# test(3)


# Plan
# Take data as input
# Analise it
# Return output

# # --> logic with side effects
# data = load_data_from_external_resources()
#
# # --> pure logic without side effects
# result = business_logic.process(data)
#
# # --> logic with side effects based on result
# if result.has_records
#   save(result.records)
# end
#
# if result.should_notify_others
#   notify_others(result.message)
# end




# repeat = "monthly"
#
# def daily():
#     print("daily func")
#
# def monthly():
#     print("monthly func")
#
# def yearly():
#     print("yearly func")
#
# def analize(func):
#     func()
#
#
# if repeat == "daily":
#     analize(daily)
# elif repeat == "monthly":
#     analize(monthly)
# elif repeat == "yearly":
#     analize(yearly)


## gET dATA
## Create a list of habit completed dates
## Create a streak

# 1. All currently tracked habits : Habits that have data in the completed habits table
# 2. All habits with the same period - day, month
# 3. Which habit has the longest run streak
# 4. Longest run streak for a habit

# - return a list of all currently tracked habits,
# - return a list of all habits with the same periodicity,
# - return the longest run streak of all defined habits,
# - and return the longest run streak for a given habit.