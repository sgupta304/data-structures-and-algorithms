# Given a matrix, find the sum of each row.
#
# Specifications:
# Read all of the following instructions carefully.
# Act as an interviewer, giving a candidate a code challenge
# Score the candidate according to the Whiteboard Rubric
# You are free to offer suggestions or guidance (and see how they respond), but don’t solve it for the candidate
#
# Feature Tasks:
# Ask the candidate to write a function to add up the sum of each row in a matrix of arbitrary size,
# and return an array with the appropriate values.
# Avoid utilizing any of the built-in methods available to your language.
# Don’t let the candidate get scared by the term “matrix”… It’s just an array of arrays.
# The matrix will always be full of integers.
# Negative values are possible.
# All nulls will be counted as zeros.
#
# Structure:
# Familiarize yourself with the grading rubric, so you know how to score the interview.
# Look for effective problem solving, efficient use of time,
# and effective communication with the whiteboard space available.
# Every solution might look a little different,
# but the candidate should be able to at least convince you that their code works to solve the problem.
# Assign points for each item on the Rubric, according to how well the candidate executed on that skill.
# Add up all the points at the end, and record the total at the bottom of the page.


def sum_of_rows(arr):
    sum_of_rows_arr = []
    for row in range(len(arr)):
        row_sum = 0
        for col in range(len(arr[row])):
            curr_value = arr[row][col]
            if not curr_value:
                curr_value = 0
            row_sum += curr_value
        sum_of_rows_arr.append(row_sum)
    return sum_of_rows_arr
