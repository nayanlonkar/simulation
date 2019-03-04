import matplotlib.pyplot as plt

def frequency_count(data_array,interval_list):
    frequency_list = []
    for i in range(len(interval_list)):
        count = 0
        for j in data_array:
            if (j >= interval_list[i][0]) and (j < interval_list[i][1]):
                count += 1
        frequency_list.append(count)
    return frequency_list

def bar_plot():
    filename = input('Enter the file name > ')
    noOfIntervals = int(input('No of intervals > '))
    #filename = 'normal.txt'
    #noOfIntervals = 15
    fd = open(filename,'r')
    data_array = [float(i.rstrip('\n')) for i in fd]
    intervalSize = (max(data_array) - min(data_array))/noOfIntervals
    range_array = []
    temp = min(data_array)

    for _ in range(noOfIntervals):
        temp2 = temp + intervalSize
        range_array.append([temp,temp2])
        temp = temp2
    range_array[noOfIntervals-1][1] += 1
    freq_array = frequency_count(data_array, range_array)
    temp_array = [i for i in range(1,noOfIntervals+1)]
    plt.bar(temp_array, freq_array)
    plt.show()

bar_plot()
