# In the following lines we got some standart sort algoryhtmes. Nothing special about. When u want it easy just do
# yourlist.sort(), hint u can also sort strings or chars or build a key to sort the list by your own demands.


def bubblesort(unsortedlist):
    n = len(unsortedlist)
    for i in range( n -1):
        for j in range(0 , n - i -1):
            if unsortedlist[j] > unsortedlist[ j +1]:
                unsortedlist[j] ,unsortedlist[ j +1 ] =unsortedlist[ j +1] ,unsortedlist[j]

def insertionsort(unsortedlist):
    for i in range(1, len(unsortedlist)):
        key = unsortedlist[i]
        j = i - 1
        while j >= 0 and key < unsortedlist[j]:
            unsortedlist[j + 1] = unsortedlist[j]
            j -= 1
        unsortedlist[j + 1] = key

def selectionsort(unsortedlist):
    for i in range(len(unsortedlist)):
        min_idx = i
        for j in range(i + 1, len(unsortedlist)):
            if unsortedlist[min_idx] > unsortedlist[j]:
                min_idx = j
        unsortedlist[i], unsortedlist[min_idx] = unsortedlist[min_idx], unsortedlist[i]
