def quicksort(array):
    '''
    #This is our quicksort algorithm. Go Cool Kidz!
    '''
    l = len(array)
    #starting number for comparisson
    pivot = array[l-1] 
    #iterator from the left in order to find the values that need sorted
    i = 0
    #iterator from the right in order to move the pivot element
    j = len(array)
    #in the case that i is less than j, you will place numbers left of the pivot because they are smaller
    while i < j:
        num = array[i]
        placeholder = array[j-2]  

        #print('i:',i, 'pivot:',pivot,'num:', num,'placeholder:',placeholder)
        
        #in the case num is greater than the pivot, you will place the numbers to the right of the pivot because they are larger
        if num > pivot:
            l = len(array)
            array[j-1] = num
            array[i] = placeholder
            array[j-2] = pivot
            
            #index is changing because the placeholder needs to be compared with the same index number 
            i = i - 1
            j -= 1
          
        i += 1
    #this is our recursive function that finishes the quicksort algorithm for n set of data
    if len(array[:i]) > 1:
        array[:i-1] = quicksort(array[:i-1])
    if len(array[i:]) > 1:
        array[i:] = quicksort (array[i:])
    return array

arr = [2,1,3,7,8,5,9,5,4]
quicksort(arr)