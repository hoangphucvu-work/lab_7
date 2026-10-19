# debug_log.md
# Author: Hoang Phuc Vu

## Bug 1
Error type: KeyError
File + line: week8_buggy.py line 11
What the error means: try to access the key 'amount' in a dictionary, but the key does not exist
What I told the duck: Inside get_total, Python loops over each dictionary in records and tries to add rec['amount'] to total. The first dictionary in line 4 has 'amout' instead of 'amount'
What I tried: Look back to see any possible errors come before line 11. I also add the DEBUG print from the lab instructions.
How I fixed it: Corrected the typo on line 4

## Bug 2
Error type: TypeError
File + line: week9_buggy.py, line 21
What the error means: Cannot compare to a string ('1000')
How I fixed it: Changed '1000' (string) to 1000 (int)

## Bug 3
Error type: Logic Bug
File + line: week9_buggy.py, at the end
What the error means: Rather than comparing for each customer, it adds up all the customers and only compared if the total is over the limit.
How I fixed it: I add a for loop command so that it compares for each customer and then report back whether each customer is over the limit or not.


## After Fixing Both Bugs
Final output: Total: $5150.00 across 3 records
True
Did pytest pass? Yes 

## AI Literacy Reflection
Did I use AI? Yes
If yes -- exact prompt I used: I noticed 2 bugs. One is a typo on line 4 that corresponds to the error on line 12, and the other is the wrong data type when using the comparison operator >, which should be an integer rather than a string. What are those 2 error types? I already knew the third one 
What AI explained: You found them. Here are the specific Python error types those bugs will trigger:

    KeyError: The typo on line 4 ('amout') causes this on line 12 when the loop tries to access rec['amount'], which does not exist in that first dictionary.

    TypeError: Comparing a number to a string on line 16 (amount > '1000') causes this because Python does not allow relational comparisons (>) between integers and strings.
What I changed myself: I changed it to the correct spelling and
Can I explain every fixed line? Yes

## What I learned
I learned how to read tracebacks from the terminals to identify error types (I also learnt different error types) so that I can identify the errors quickly.

I learned to use print statements inside for loops to isolate error dictionary keys and changing data types fitting with comparisons.