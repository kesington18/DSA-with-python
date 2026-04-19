a = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    left = quick_sort(left)
    right = quick_sort(right)

    print(f"Left: {left}")
    print(f"Right: {right}")
    return left + [pivot] + right

print(quick_sort(a))