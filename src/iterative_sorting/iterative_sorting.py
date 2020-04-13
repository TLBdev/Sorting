# TO-DO: Complete the selection_sort() function below 
arr = [1, 5, 8, 4, 2, 9, 6, 10, 3, 7, 0]
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        smallest_index = i
        #print('i', i)
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(i , len(arr)):
            #print("x", x)
            if arr[x] < arr[smallest_index]:
                smallest_index = x
                #print(smallest_index)
                
                
        if smallest_index > 0:
            smaller = arr[smallest_index]
            larger = arr[i]

            arr[smallest_index] = larger
            arr[i] = smaller
            #print(arr)

        # TO-DO: swap




    return arr
print(selection_sort(arr))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swaps_performed = 1
    max_length = len(arr)
    while swaps_performed > 0:
        swaps = 0
        max_length -= 1
        for i in range(0, max_length):
            
            if i + 1 <= max_length:
                if arr[i] > arr[i+1]:
                    smaller = arr[i+1]
                    larger = arr[i]
                    arr[i+1] = larger
                    arr[i] = smaller
                    swaps += 1
        swaps_performed = swaps
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr