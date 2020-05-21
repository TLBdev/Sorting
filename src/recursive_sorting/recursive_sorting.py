# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    #elements = len( arrA ) + len( arrB )
    #merged_arr = [0] * elements
    merged_arr =[]
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] <= arrB[0]:
            merged_arr.append(arrA[0])
            if len(arrA) >= 1:
                arrA = arrA[1:]
            else:
                arrA = []
        else:
            merged_arr.append(arrB[0])
            if len(arrB) >= 1:
                arrB = arrB[1:]
            else:
                arrB = []
    while len(arrA) > 0:
        merged_arr.append(arrA[0])
        if len(arrA) >= 1:
                arrA = arrA[1:]
        else:
            arrA = []
    while len(arrB) > 0:
        merged_arr.append(arrB[0])
        if len(arrB) >= 1:
                arrB = arrB[1:]
        else:
            arrB = []
    return merged_arr

# # MERGESORT
# ​
# [2, 0, 1, 3, 6, 9, 8, 5, 7, 4]
# ​
# # (base case) If the array is empty or length 1, return
# ​
# # Split the arrays into half
# arr1 = [2, 0, 1, 3, 6]
# arr2 = [9, 8, 5, 7, 4]
# ​
# # Sort each half
# arr1 = [0,1,2,3,6]
# arr2 = [4,5,7,8,9]
# ​
# # Merge them back together
# # Compare the first values of each array, add smaller of the 2 to result
# merged = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) <= 1:
        return arr
    arr1 = arr[:len(arr)// 2]
    arr2 = arr[len(arr)// 2:]
    
    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)
    return merge(arr1, arr2)
    


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
