a = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] + right

print(quick_sort(a))


# for proper visualization and understanding run this code below
'''
a = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def quick_sort(arr, depth=0):
    indent = "   " * depth

    print(f"{indent}quick_sort({arr})")

    if len(arr) <= 1:
        print(f"{indent}Return {arr}")
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    print(f"{indent}Pivot: {pivot}")
    print(f"{indent}Left : {left}")
    print(f"{indent}Right: {right}")

    sorted_left = quick_sort(left, depth + 1)
    sorted_right = quick_sort(right, depth + 1)

    result = sorted_left + [pivot] + sorted_right

    print(f"{indent}Merged: {result}")
    return result


print("\nFinal:", quick_sort(a))
'''