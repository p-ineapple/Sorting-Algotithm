def bubble_sort(array):
    
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            swapped = False
            if array[j] > array[j+1] and not swapped:
                array[j],array[j+1] = array[j+1],array[j]
                swapped = True
                
    return array
    


def insertion_sort(array):
    newarr = [array.pop(0)]
    for i in range(len(array)):
        el = array.pop(0)
        print(i, newarr, el)
        if el <= newarr[0]:
            newarr.insert(0, el)
        elif el >= newarr[-1]:
            newarr.append(el)
        else:
            j = 0
            swapped = False
            while not swapped:
                if newarr[j] < el <= newarr[j+1]:
                    newarr.insert(j+1, el)
                    swapped = True
                else:
                    j += 1
    return newarr



def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    l_arr = array[:mid]
    r_arr = array[mid:]
    def merge(l,r):
        arr = []
        while len(l) > 0 and len(r) > 0:
            if l[0] < r[0]:
                el = l.pop(0)
            else:
                el= r.pop(0)
            arr.append(el)
        arr += l
        arr += r
        return arr
    l = merge_sort(l_arr)
    r = merge_sort(r_arr)
    sortedarr = merge(l,r)
    return sortedarr
    
    

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    l_pivot = []
    r_pivot = []
    for i in range(1, len(array)):
        el = array[i]
        if el < pivot:
            l_pivot.append(el)
        else:
            r_pivot.append(el)
    return quick_sort(l_pivot) + [pivot] + quick_sort(r_pivot)
