def selection_sort(arr):
    for i in range(len(arr)):
        min=arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < min:
                current=arr[j]
                arr[j]=min
                min=current
        arr[i]=min
    return arr
                
                
def display(arr):
    print("Sorted array is: ", ' ')
    for i in range(len(arr)):
        print(arr[i], end=' ')
if __name__=="__main__":
    arr=[3,2,1,4]
    print("Input array is: ",'')
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()
    response=selection_sort(arr)
    display(arr)
    