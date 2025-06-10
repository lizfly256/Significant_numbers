def all_the_same(the_num):
    """ Returns True if all digits in a number are the same, otherwise returns False """
    digits = []
    # creates list of digits in number
    for digit in str(the_num):
        if len(digits) > 1:
            if digits.count(digit) < 1 : return False
        digits.append(digit)
    return True

def make_highest_num(num_digits):
    """ Returns the highest number with the given number of digits """
    i = 1
    highest_num = 9
    while i < num_digits:
        highest_num += 9 * (10 ** i)
        i += 1
    return highest_num



    
i = 10
num_digits = 6
tally_all_the_same = 0
while len(str(i)) < num_digits:
    if all_the_same(i):
        tally_all_the_same += 1 
    i += 1 
# check 3 repeats for numbers over 3 digits long
# check for numbers that are symetrical
# add up all "notable" number types (account for repeats within the categories???)
### add them up in a way that it is tallied and only once (if any where true ex. overall_tally += 1)

highest_num = make_highest_num(num_digits)

print(str( round((tally_all_the_same / highest_num * 100), 2) ), '% have all digits the same')
print('highest: ', highest_num)
print('tall all the same: ', tally_all_the_same)
