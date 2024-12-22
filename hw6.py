def bubble_sort(arr):
    n = len(arr)
    for i in range(n):

        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break
    return arr

def selection_sort(arr):
    n = len(arr)

    for i in range(n):

        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            print(f"Элемент {target} найден на индексе {mid}")
            return mid

        elif arr[mid] > target:
            high = mid - 1

        else:
            low = mid + 1

    print(f"Элемент {target} не найден в списке.")
    return -1

arr = [29, 10, 14, 37, 13]

sorted_arr = bubble_sort(arr)

print(f"Отсортированный список: {sorted_arr}")

target = 10
binary_search(sorted_arr, target)

