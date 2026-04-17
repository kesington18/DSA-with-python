a = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr

    m = n // 2
    Left = arr[:m]
    Right = arr[m:]

    Left = merge_sort(Left)
    Right = merge_sort(Right)
    l, r = 0, 0
    Left_len = len(Left)
    Right_len = len(Right)

    sorted_arr = [0] * n
    i = 0

    while l < Left_len and r < Right_len:
        if Left[l] < Right[r]:
            sorted_arr[i] = Left[l]
            l += 1
        else:
            sorted_arr[i] = Right[r]
            r += 1
        i += 1

    while l < Left_len:
        sorted_arr[i] = Left[l]
        l += 1
        i += 1

    while r < Right_len:
        sorted_arr[i] = Right[r]
        r += 1
        i += 1

    return sorted_arr

print(merge_sort(a))