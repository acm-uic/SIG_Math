import time
start_time = time.time()
# convert sum of abundant numbers from list to set
abundant_number_list = []


def abundant_number(input_number):  # bool, return type true for abundant numbers. order of dvisibility irrelevant
    divisor_sum = 1
    for i in range(2, int(input_number ** .5) + 1):
        if input_number % i == 0:
            converse_number = input_number / i
            divisor_sum += i
            if converse_number != i:
                divisor_sum += converse_number
    return input_number < divisor_sum


for i in range(1, 20161):
    if abundant_number(i):
        abundant_number_list.append(i)

def is_a_sum(input_number):
    for abundant_number in abundant_number_list:
        if input_number > abundant_number:
            if input_number - abundant_number in abundant_number_list:
                return True
    return False

sum = 0
for i in range(0, 20161):
    if not is_a_sum(i):
        sum += i

print(sum)

end_time = time.time()
print(end_time - start_time)
