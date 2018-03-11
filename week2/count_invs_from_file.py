import count_inv as c

def get_list_from_file():
    theFile = open("IntegerArray.txt", "r")
    theInts = []
    for val in theFile.read().split():
        theInts.append(int(val))
    theFile.close()
    return theInts

def main():
    l = get_list_from_file()
    print(len(l))
    (l,i) = c.mergeSort(l)
    print i

if __name__ == '__main__':
  main()
