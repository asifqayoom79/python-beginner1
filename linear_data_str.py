#1. Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)

    return pairs

if __name__ == "__main__":
    input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 10
    result_pairs = find_pairs_with_sum(input_array, target)
    print(f"Pairs in the array with sum {target}: {result_pairs}")


#2.Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array?
def reverse_array_in_place(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

if __name__ == "__main__":
    input_array = [1, 2, 3, 4, 5]
    print("\nOriginal array:", input_array)

    reverse_array_in_place(input_array)
    print("Reversed array:", input_array)


#3. Q3. Write a program to check if two strings are a rotation of each other?
def are_strings_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    doubled_s1 = s1 + s1
    return s2 in doubled_s1

if __name__ == "__main__":
    str1 = "entertainment"
    str2 = "ainmententert"

    if are_strings_rotation(str1, str2):
        print("\n" f"'{str1}' and '{str2}' are rotations of each other.")
    else:
        print(f"'{str1}' and '{str2}' are not rotations of each other.")
