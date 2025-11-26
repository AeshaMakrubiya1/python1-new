'''
WAP to perform addition of two 1D arrays and store it into another array.
'''

n = int(input("Enter number of array : "))
arr1 = []
arr2 = []
result = []

print("Enter elements of first array : ")
for i in range(n):
    arr1.append(int(input()))
    
print("Enter elements of second array : ")
for i in range(n):
    arr2.append(int(input()))
    
for i in range(n):
    result.append(arr1[i] + arr2[i])
    
print("result after addition : ", result)
    