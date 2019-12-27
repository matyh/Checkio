#!/usr/bin/env checkio --domain=py run restricted-sum

# Our new calculator is censored and as such it does not accept certain words.    You should try to trick by writing a program to calculate the sum of numbers.
# 
# Given a list of numbers, you should find the sum of these numbers.    Your solution should not contain any of the banned words, even as a part of another word.
# 
# The list of banned words are as follows:
# 
# sum
# import
# for
# while
# reduce
#
# Input:A list of numbers.
# 
# Output:The sum of numbers.
# 
# Precondition:The small amount of data. Let's creativity win!
# 
# 
# END_DESC


def checkio(data, result=0):
    # global result
    result += data.pop(0)
    if data:
        return checkio(data, result)
    else:
        return result

print(checkio([1, 2, 3]))
print(checkio([2, 2, 2, 2, 2]))
print(checkio([-2, 2]))
