from math import sqrt

def getNumbers()  
    nums = []   # start with an empty list
    #sentinel loop to get numbers
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = eval(xStr)
        nums.append(x)     #add this value to the list
        xStr = input(Enter a number (<Enter> to quit) >> ")
    return nums
    
 def mean(nums):
      num = 0.0
      for num in nums:
        sum = sum + num
      return sum / len(nums)
      
 def stdDev (nums, xbar):
    sumDevSq = 0.0
    for num in nums:
        dev = num - xbar
        sumDevSq = sumDevSq + dev * dev
    return sqrt(sumDevSq/(len(nums)-1))
    
 def median(nums):
    nums.sort()
    midPos = size // 2
    if size % 2 == 0:
        median = (nums[midPos] + num[midPos-1]) / 2.0
    else:
        median = num[midPos]
    return median

def main ():
            print("this program computes mean, median, and standart deviation.")
            data = getNumbers()
            xbar = mean(data)
            std = stdDev(data, xbar)
            med = median (data)
            
            print("\nThe mean is",xbar)
            print("The standard deviation is", std)
            print("The median is", med)
    if __ name __ == '__main__':main()
    