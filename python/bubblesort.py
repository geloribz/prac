#Arranges from lowest to highest
def bubble_sort(nums):
    for setup in range(len(nums)-1,0,-1):
        for index in range(setup):
            if nums[index] > nums[index+1]:
                #changing the comparison operator here to '<' from '>' will arrange it from highest to lowest
                temp_nums = nums[index]
                nums[index] = nums[index+1]
                nums[index+1] = temp_nums

numset = [32, 142, 6, 54, 222, 31, 87, 33, 21, 8, 1002, 2, 1, 88, 56, 66, 999, 82]
bubble_sort(numset)

print(numset)
