def binary_search(array , x, low, high):

    while low <= high:
        mid = low + (high - low) #middle index
        if array[mid] == x: #element found
            return mid
        elif array[mid] < x: #x is on the right side 
            low = mid + 1
        else : #x is on the left side 
            high = mid - 1 
        return -1 #element is not found 
array = [3,4,5,6,7,8,9]
x = int(input())

result = binary_search(array,x,0,len(array)-1)

if result != -1: #if element is found 
    print("Element is present at index " + str(result))
else: #if element is not found 
    print("not found")