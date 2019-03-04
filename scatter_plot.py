import matplotlib.pyplot as plt

def scatter_plot():
    filename = input('Enter the file name > ')
    noOfIntervals = int(input('Number of intervals > '))
    fd = open(filename,'r')
    data_array = [float(i.rstrip('\n')) for i in fd]
    array1 = data_array[:len(data_array)-1]
    array2 = data_array[1:]
    plt.scatter(array1, array2)
    plt.title(filename)
    plt.show()

scatter_plot()
