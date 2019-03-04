
def readfile(filename):
    fd = open(filename,'r')
    data_array = [float(i.rstrip('\n')) for i in fd]
    return data_array

def max1(data_array):
    temp = data_array[0]
    for i in data_array:
        if i > temp:
            temp = i
    return temp

def min1(data_array):
    temp = data_array[0]
    for i in data_array:
        if i < temp:
            temp = i
    return temp

def frequency_count(data_array,interval_list):
    #this function will accept two arguments (two dimensional array of intervals and data array) and 
    #will return the array containing the frequency of each interval
    frequency_list = []
    for i in range(len(interval_list)):
        count = 0
        for j in data_array:
            if (j >= interval_list[i][0]) and (j < interval_list[i][1]):
                count += 1
        frequency_list.append(count)
    return frequency_list

