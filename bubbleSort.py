# Time complexity O(n^2)
# Space omplexity O(1)

a = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def bubble_Sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                flag = True
                arr[i -1], arr[i] = arr[i], arr[i-1]
    return arr, n
print(bubble_Sort(a))


'''
optimized solution for if it is already sorted before checking
def bubble_Sort(arr):
    n = len(arr)
    for j in range(n):
        swapped = False
        for i in range(1, n - j):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True
        if not swapped:
            break
    return arr
'''