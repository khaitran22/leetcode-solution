
def findClosestElements(arr, k, x):
    if x < arr[0]:
        return arr[:k]
    elif x > arr[-1]:
        return arr[len(arr)-k:]

    for i in range(len(arr)):
        if arr[i] == x:
            left = i - 1
            right = i + 1
            result = [arr[i]]
            break
        elif arr[i] > x:
            left = i - 1
            right = i
            result = []
            break

    stop_right = right == len(arr)
    stop_left = left < 0
    while len(result) < k:
        if not stop_right and not stop_left:
            if abs(arr[left]-x) > abs(arr[right]-x):
                result.append(arr[right])
                right += 1
            else:
                result.insert(0, arr[left])
                left -= 1
        elif stop_right and not stop_left:
            result.insert(0, arr[left])
            left -= 1
        elif not stop_right and stop_left:
            result.append(arr[right])
            right += 1
        else:
            break
        stop_right = right == len(arr)
        stop_left = left < 0
    return result
