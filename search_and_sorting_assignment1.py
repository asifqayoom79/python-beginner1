def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Original List:", unsorted_list)

insertion_sort(unsorted_list)
print("Sorted List:", unsorted_list)

#5.Write a program to sort list of strings (similar to that of dictionary)
def dictionary_sort(strings_list):
    return sorted(strings_list)

if __name__ == "__main__":
    input_list = ["apple", "orange", "banana", "grape", "cherry", "pear"]
    sorted_list = dictionary_sort(input_list)
    print("\n",sorted_list)

