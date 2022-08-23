#Adding the digits of a number (in this case an integer) without declaring strings
def digit_sum(nums):
    digits_val = 0
    init_num = nums
    while init_num != 0:
        digits_val += init_num%10
        init_num = int(init_num/10)
    return digits_val

num = int(input("What is the number you want to get the sum of its digits of?: "))
print(f"The sum of the digits of the number, {num} is equal to {digit_sum(num)}")
