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
                print(f'Updated: {arr}')
                smallest_index = j
        #create a temp to hold cur_index
        temp = arr[cur_index]
        #move smallest_index to the cur_index
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr
  

  #https://www.youtube.com/watch?v=mI3KgJy_d7Y&t=155s Used the video to understand the selection sort process, found my issue was no temp

        # TO-DO: swap

# Trying to find a cleaner way to do a bubble sort
def bubble_sort( arr ): 
    #Loop through elements
    sorted = False
    while not sorted:
        swaps = 0
        #Check the current element compared to the element to the right
        for i in range(0, len(arr) - 1):
            #If element to right is lower, swap
            if arr[i] > arr[i+1]:
                swaps += 1
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
        if swaps == 0:
            sorted = True
    #Return sorted arr when complete
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr