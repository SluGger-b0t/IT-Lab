list = [2,5,7,9,12,23]
m = int(input("Enter the number you want to search for: "))
length = len(list)
print(length)


def binarySearch(list, key, length):
    start = 0
    end = length-1

    mid = start + (end-start)//2

    while start <= end:
        if list[mid] == key:
            print("Element found")
            return
        elif list[mid] > key:
            end = mid - 1
        elif list[mid] < key:
            start = mid+1
       
        mid = start + (end-start)//2

binarySearch(list,m,length)