m=int(input())
nums=list(map(int,input().split()))

def performInsertionSort(nums):
    n = len(nums)
    for index in range(1, n):
        temp = nums[index]
        position = index - 1 
        while position >= 0 and nums[position] > temp:
            nums[position + 1] = nums[position]
            position -= 1 
 
        nums[position + 1] = temp 

#nums = [12, 2, 34, 20, 56, 43, 45, 100, 89, 50]
performInsertionSort(nums)
print(*nums)
