
# Python_Repo

- _This repo contains python assignments._


## Project_Structure

 - **src**
 
     - `driver.py` contains function call.
     - `utils.py` contains function declaration and definition.
 - **test**

     - `test.py` contains test cases for the function.
 - **.gitignore**

     - ignore unwanted files/directory like `.idea` when committing project to the GitHub repository.
 - **README.md**

    - *Overview of the project*

## Q1: calendar_module

**_Functions used:_**

- `import calendar`: Imports the calendar module for calendar-related functions.
- `map()`: Applies the `int` function to each element of the input and returns an iterator.
- `input()`: Reads input from the user.
- `calendar.weekday()`: Calculates the day of the week (as an integer) for a given date.
- `split()`: Splits a string into a list of substrings based on a delimiter.
- list indexing: Accesses elements of a list using an index.

**_Summary:_**

- The code takes user input for a date and calculates the day of the week.
- It returns the name of the day corresponding to the input date.

##  Q2: collections_named_tuple
**_Functions used:_**

- `from collections import namedtuple`: Imports the namedtuple class from the collections module.

**_Summary:_**

- The code defines a function `collections_named_tuple()` that calculates the average marks of students.
- It utilizes namedtuple to create a structured representation of student data and calculates the average marks.

## Q3: email_validation_using_filter

**_Functions used:_**

- `import re`: Imports the regular expression module for pattern matching.

**_Summary:_**

- The code defines a function `fun(s)` to validate emails using regular expressions.
- It then defines a function `filter_mail(emails)` to filter valid emails from a list.
- Finally, the function `email_validation_using_filter()` takes user input for a list of emails, filters valid ones using `filter_mail()`, sorts them, and logs the result.

## Q4: finding_the_percentage


**_Functions used:_**

- `import logging`: Imports the logging module for logging messages.

**_Summary:_**

- The code defines a function `finding_the_percentage()` to calculate the average percentage of a student's scores.
- It takes input for the number of students, their names, and their scores.
- It then calculates the average percentage for a specific student.

## Q5: floor_ceil_rint

**_Functions used:_**

- `import numpy`: Imports the numpy module for numerical computations.

**_Summary:_**

- **_Functions used:_**

- `import numpy`: Imports the numpy module for numerical computations.

**_Summary:_**

- The code defines a function `floor_ceil_rint()` to perform floor, ceil, and rint operations on a numpy array using the numpy functions `numpy.floor()`, `numpy.ceil()`, and `numpy.rint()`, respectively.
- It takes input for an array, performs the following operations:
  - `numpy.floor()`: Rounds down each element of the array to the nearest integer.
  - `numpy.ceil()`: Rounds up each element of the array to the nearest integer.
  - `numpy.rint()`: Rounds each element of the array to the nearest integer.
- The results of each operation are logged.
## Q6: iterables_and_iterators
**_Functions used:_**

- `from itertools import combinations`: Imports the combinations function from the itertools module.

**_Summary:_**

- The code defines a function `iterables_and_iterators()` to calculate the probability of selecting a combination containing a specific element.
- It takes input for a list length, a list of elements, and the combination length.
- It calculates the total number of combinations using `combinations()` from itertools.
- It iterates through all combinations, counts those containing a specific element, and calculates the probability.
## Q7: linear_algebra
**_Functions used:_**

- `import numpy`: Imports the numpy module for numerical computations.

**_Summary:_**

- The code defines a function `linear_algebra()` to calculate the determinant of a square matrix using numpy.
- It takes input for the size of the square matrix and its elements.
- It creates a numpy array representing the matrix.
- It calculates the determinant using `numpy.linalg.det()`.
- The determinant is rounded to two decimal places and logged.
## Q8: mean_var_std
**_Functions used:_**

- `import numpy as np`: Imports the numpy module for numerical computations.

**_Summary:_**

- The code defines a function `mean_var_std()` to calculate the mean, variance, and standard deviation of an array using numpy.

- `Mean:` Calculates the average value of the array along the rows.
- `Variance:` Computes the variance of the array along the columns.
- `Standard Deviation:` Computes the standard deviation of the array, rounded to 11 decimal places.
## Q9: merge_the_tools

**_Summary:_**

- The code defines a function `merge_the_tools()` to split a string into substrings of length k and remove duplicates from each substring.
- It takes input for the string and the length of the substrings (k).
- It splits the string into substrings of length k.
- It iterates through each substring, removes duplicates, and logs the result.

## Q10: min_and_max

**_Functions used:_**

- `import numpy`: Imports the numpy module for numerical computations.

**_Summary:_**

- The code defines a function `min_and_max()` to find the maximum of the minimum values along rows in a numpy array.
- It takes input for the dimensions of the array and its elements.
- It creates a numpy array representing the matrix.
- It calculates the minimum along the rows using `numpy.min()` and then finds the maximum of these minimum values.
## Q11: mutate_string
**_Summary:_**

- The code defines a function `mutate_string()` to replace a character at a specific position in a string.
- It takes input for the original string, the position, and the character to be replaced.
- It converts the position to an integer and constructs the mutated string by replacing the character at the specified position.
- The mutated string is logged and returned.





## Q12: no_idea
**_Summary:_**

- The code defines a function `no_idea()` to calculate happiness based on set membership.
- It takes input for the number of elements, the number of elements in set A, the elements, and the elements in sets A and B.
- It initializes happiness to 0.
- It iterates through the elements, incrementing happiness if an element is in set A, decrementing if in set B.
- The total happiness is logged and returned.
## Q13: piling_up
**_Summary:_**

- The code defines a function `piling_up()` to check if it's possible to pile up blocks according to given conditions.
- It takes input for the number of test cases and block sizes for each test case.
- It initializes an empty list `ANS` to store the results.
- It iterates through each test case:
  - For each test case, it checks if blocks can be piled up according to the given conditions.
  - If it's possible, "Yes" is appended to `ANS`, otherwise "No" is appended.
- The results are logged and returned as a string joined by newline characters.
## Q14: runnerup_score
**_Summary:_**

- The code defines a function `runnerup_score()` to find the second largest element in an array.
- It takes input for the size of the array and the elements of the array.
- It sorts the array in ascending order.
- It iterates through the sorted array to find the largest and second largest elements.
- The second largest element is logged and returned.
## Q15: string_formatting
**_Summary:_**

- The code defines a function `string_formatted()` to format integers in various representations.
- It takes input for an integer `n`.
- It calculates the spacing required for formatting based on the binary representation of `n`.
- It iterates through integers from 1 to `n` and formats each integer in decimal, octal, hexadecimal, and binary representations with appropriate spacing.
- The formatted strings are logged and returned as a single string.





## Q16: text_alignment
**_Summary:_**

- The code defines a function `text_alignment()` to generate a text-based pattern.
- It takes input for the thickness of the pattern.
- It constructs various parts of the pattern using string manipulation methods.
- The constructed parts are logged and returned as a single string representing the entire pattern.
## Q17: time_delta
**_Functions used:_**

- `from datetime import datetime`: Imports the datetime class from the datetime module.
- `import os`: Imports the os module for operating system-related functions.

**_Summary:_**

- The code defines a function `time_delta()` to calculate the time difference between two datetime objects.
- It reads input from the user for the number of test cases.
- It reads input for two timestamps in string format.
- It parses the timestamps into datetime objects using the specified format.
- It calculates the absolute difference in seconds between the two datetime objects.
- The result is written to the output file.
## Q18: word_order
**_Functions used:_**

- `from collections import Counter`: Imports the Counter class from the collections module.

**_Summary:_**

- The code defines a function `word_order()` to count the frequency of words and their order of occurrence.
- It takes input for the number of words.
- It reads the words and stores them in a list.
- It uses the Counter class to count the frequency of each word.
- It constructs a list containing the count of unique words and their frequencies.
- The constructed list is returned as a string.