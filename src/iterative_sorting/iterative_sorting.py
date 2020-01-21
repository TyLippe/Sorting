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
                print(f'Smallest: {smallest_index}')
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


# # TO-DO:  implement the Bubble Sort function below
# def bubble_sort( arr ):
#     #loop through elements
#     for i in range(0, len(arr) -1):
#         #iterate over value next to the current value
#         for j in range(0, len(arr)-1 -i):
#             #check if current value is greater than the value to the right
#             if arr[j] > arr[j+1]:
#                 print(arr)
#                 #if value is greater, swap them around 
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr


#https://www.youtube.com/watch?v=YHm_4bVOe1s Used this video to show example of Bubble Sort/ tried a couple things, did not work out and compared their code to mine.

# Trying to find a cleaner way to do a bubble sort

def bubble_sort( arr ): 
    #Loop through elements
    for i in range(0, len(arr) - 1):
        #Check the current element compared to the element to the right
        for j in range(i, len(arr) - 1):
            print(arr)
            #If element to right is lower, swap
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
            #If element to right is higher, move onto the next element
    #Return sorted arr when complete
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr