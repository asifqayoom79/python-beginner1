#1.write a python program to Implement Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

sorted_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 14

result = binary_search(sorted_list, target)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")


#2.write a python program Implement Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

unsorted_list = [38, 27, 43, 3, 9, 82, 10]
print("\nOriginal List:", unsorted_list)

merge_sort(unsorted_list)
print("Sorted List:", unsorted_list)

#3 write a program to  Implement Quick Sort 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("\nOriginal List:", unsorted_list)

sorted_list = quick_sort(unsorted_list)
print("Sorted List:", sorted_list)


