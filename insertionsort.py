def insertion(arr):
    for j in range(1, len(arr)):
        main=arr[j]
        i=j-1
        while i >= 0 and arr[i] > main:
            arr[i+1]=arr[i]
            i-=1
        arr[i+1]=main
    return arr
def display(arr):
    for i in range(len(arr)):
        print(arr[i],end=' ')
if __name__=="__main__":
    
    arr=[110, 2200, 3487,8934, 237, 4508, 4378, 403, 236, 3498, 34, 349, 3409]
    print("Input array is: ", end=' ')
    for i in range(len(arr)):
        print(arr[i], end=' ')
    response=insertion(arr)
    print()
    print("sorted array is: ", end=' ')
    display(response)
    