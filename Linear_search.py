# linear search
def linear(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
        return -1