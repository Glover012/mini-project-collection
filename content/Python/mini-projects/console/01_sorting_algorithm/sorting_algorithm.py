import time, random

def listSorting(unorderedList):
    testList = unorderedList
    newList = []
    i = 0
    ok = 0

    while True:

        #print(f"Iteration - {i}")
        #print(f"Test list: {testList}")
        #print(f"New list: {newList}")

        if len(testList) == 1:
            newList.append(testList[0])
            testList = newList #

            for x in range(len(testList)-1): # Sorting check
                if testList[x] <= testList[x+1]:
                    ok+=1

            if ok == (len(testList)-1):
                #print(f"Sorting ended, result: {newList}")
                break
            else:
                newList = []
                ok = 0

        if testList[0] > testList[1]:
            newList.append(testList[1])
            del testList[1]
        else:
            newList.append(testList[0])
            del testList[0]
        i+=1

    return newList

unorderedList = [random.randint(-1000, 1000) for value in range(0, 1000)]
print(unorderedList[0], unorderedList[-1])

start = time.perf_counter()
sortedList1 = listSorting(unorderedList)
end = time.perf_counter()
print(f"Sorting time: {end-start}")
print(sortedList1[0], sortedList1[-1])
