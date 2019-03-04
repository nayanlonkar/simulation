import matplotlib.pyplot as plt

def histogram():
    filename = input('Enter the file name > ')
    noOfIntervals = int(input('Number of intervals > '))
    fd = open(filename,'r')
    data_array = [float(i.rstrip('\n')) for i in fd]
    intervalsize = (max(data_array) - min(data_array))/noOfIntervals 
    temp = min(data_array)
    range_array = [temp]
    max1 = max(data_array)
    while(temp < max1):
        temp += intervalsize
        range_array.append(temp)

    plt.hist(data_array, range_array)
    plt.title(filename)
    plt.show()

histogram()
