#################
# quick sort #
################# 

def partition(array, low, high):
    if low > high:
        return
    
    pivot_val   = array[high]
    pivot_index = high
    right_index = high - 1
    left_index  = low
    
    while True:
        while (array[left_index] < pivot_val):
            left_index = left_index + 1
    
        while (array[right_index] > pivot_val):
            right_index = right_index - 1
        #print("right/left check - right " + str(right_index) + " left - " + str(left_index)) 
        if left_index >= right_index:
            break
        else:
            array[left_index],array[right_index] = array[right_index],array[left_index]
        
    array[left_index],array[pivot_index] = array[pivot_index],array[left_index]
    #print ("array pertition - " + str(array))
    #print ("array index - " + str(left_index))
    return left_index

def quick_sort(array, low, high):
    #print("start - low - " + str(low))
    #print("start - high - " + str(high))
    if low >= high:
        return
    
    index = partition(array,low, high)
    #print("index - " + str(index))

    #print("###")
    quick_sort(array, low, index-1)
    quick_sort(array,index+1, high)
    return array

def find_missing_ele(array):
    for i in range(len(array)):
        if array[i] != i:
            return i
    return -1       
###############   
## MAIN
###############

#c = [12,4,53,67,233,67,89,99]
#d = [2, 93, 100, 65, 83, 25, 47, 14 ]
#e = [43, 3, 9, 67, 66, 98, 49, 23, 35]
#a = [1,2,3,4,5,6,7,8,9]
#b = [9,8,7,6,5,4,3,2,1]

#sorted_array  = quick_sort(c, 0 , len(c)-1)
#print (str(sorted_array))

###############################################################3
'''
test_a = [5,2,4,1,0]
test_b = [9,3,2,5,6,7,1,0,4]

sorted_a = quick_sort(test_a,0, len(test_a)-1)
result = find_missing_ele(sorted_a)

if result != -1 :
    print("missing element - " + str(result))
else:
    print("no element is missing")



sorted_b = quick_sort(test_b,0, len(test_b)-1)
result = find_missing_ele(sorted_b)

if result != -1 :
    print("missing element - " + str(result))
else:
    print("no element is missing")
'''

# find three ways fid greatest number

test_e = [1,3,4,23, 78, 5,2,9,13, 15]

# O n^2
great_num = 0;
for i in range(len(test_e)):
    great_num = test_e[i]
    for j in range(len(test_e)):
        if test_e[j] > great_num:
            great = test_e[j]

print("find great " + str(great))

# O(NlogN)
sorted_array = quick_sort(test_e, 0 , len(test_e)-1)
print ("find great #2 " + str(sorted_array[-1]))

# O(N)
great_num = 0
for i in range(len(test_e)):
    if great_num < test_e[i]:
        great_num = test_e[i]
    
print ("find great #3 " + str(great_num))

