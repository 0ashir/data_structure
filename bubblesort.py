#bubble sort function
def bubblesort(arr):
    for i in range(len(arr)): #outer loop for repeating the inner loop
        for j in range(i, len(arr)-1): #inner loop, starting point increase by 1, end-point is third last element
            if arr[j] > arr[j+1]:  #if current element is greater then the next one
                arr[j], arr[j+1] = arr[j+1], arr[j] #swap both elements
    return arr #return the sorted array

#displaying the sorted array
def display(arr):
    print("Sorted array is: ", end=' ')
    for i in range(len(arr)):
        print(arr[i], end=' ')
    
if __name__=="__main__":
    
    arr=[90,0,43,10,150, 100, 200] #given array
    print("Input array is: ", end=' ')
    
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()
    
    response=bubblesort(arr) #passing input-array to the bubble sort function
    display(arr)