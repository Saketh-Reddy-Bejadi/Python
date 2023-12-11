# def miniMaxSum(arr):
#     n=len(arr)
#     minsum=0
#     maxsum=0
#     for i in range(0,n):
#         if(i>0) :
#             maxsum+=arr[i]
#         if (i<n-1) :
#             minsum+=arr[i]
#     print(minsum,maxsum)
    
# arr=list(map(int,input().split()))
# miniMaxSum(arr)

def find_min_max_sum(arr):
    arr.sort()

    min_sum = sum(arr[:4])

    max_sum = sum(arr[1:])

    return min_sum, max_sum

arr = [7,69,2,221,8974]

result = find_min_max_sum(arr)

# Print the results
print("Minimum Sum:", result[0])
print("Maximum Sum:", result[1])
