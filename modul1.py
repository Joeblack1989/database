


def sort(data,a):
    file=open(data, 'r')
    for line in file:
        arr = line.split()
        if arr[3]==a:
            print(arr)
          

print(sort('base.txt','9'))