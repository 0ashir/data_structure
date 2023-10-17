#function for sorting the array
def sort(arr):
    for i in range(len(arr)): #outer loop for repeating inner loop 
        for j in range(len(arr)-1):  #loop from first to third last element
            if arr[j] > arr[j+1]:  #checking if the current element is greater then the next one 
                arr[j], arr[j+1]= arr[j+1], arr[j] # replacing elements
    return arr  #return array as sorted_array

#binary search function
def binary_search(arr, input_element):
    mid=len(arr)//2  #finding the mid-point of list/array
    left_arr=arr[0:mid]  #array before the mid-point
    right_arr=arr[mid:len(arr)] #array after the mid-point
    
    try:
        if input_element == arr[mid]:  #if mid element is the user-input element 
            print("Element found in the array at index")
        elif input_element > arr[mid]: #if user-input element is greater then the element at mid-point 
            binary_search(right_arr, input_element) #then find element on the right side of array/list
        elif input_element < arr[mid]:  #if user-input element is less then the element at mid-point
            binary_search(left_arr, input_element) #then find element on the left side of array/list
    except:
        print("Element not found in the array")
    
if __name__=="__main__":
    arr=[89, 34, 343, 3445, 563, 63, 0, 63, 76,76, 87, 61,9] #input array
    
    input_element=int(input("Enter number want to search: ", )) #number input by user
    

    sorted_arr=sort(arr) #sorting the array by passing it to the sorting functions
    
     #searching number in the array, using binary-searhc
    print(binary_search(sorted_arr, input_element))
    