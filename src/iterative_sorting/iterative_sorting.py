# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i 
        smallest_index = cur_index 
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        #iterate over all values to right of cur_index
        for j in range(i + 1, len(arr)):
            #determine if this value is lower than the current smallest_index
            if arr[j] < arr[smallest_index]:
                #if smaller, set smaller_index to j
                smallest_index = j
        #create a temp to hold cur_index
        temp = arr[cur_index]
        #move smallest_index to the cur_index
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr
  



        # TO-DO: swap


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr