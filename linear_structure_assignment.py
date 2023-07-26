#1. Delete the elements in a linked list whose sum is equal to zero
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_zero_sum_sublists(head):
    dummy = ListNode(0)
    dummy.next = head
    prefix_sum = {0: dummy}
    curr = dummy

    while curr:
        curr_sum = 0
        curr = curr.next

        while curr:
            curr_sum += curr.val
            if curr_sum in prefix_sum:
                prefix_sum[curr_sum].next = curr.next
                break
            else:
                prefix_sum[curr_sum] = curr

            curr = curr.next

    return dummy.next

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

if __name__ == "__main__":
    # Create a linked list: 3 -> 4 -> -7 -> 5 -> -6 -> 6
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(-7)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(-6)
    head.next.next.next.next.next = ListNode(6)

    print("Original Linked List:")
    print_linked_list(head)

    head = delete_zero_sum_sublists(head)

    print("Linked List after Deletion:")
    print_linked_list(head)


 #2. Reverse a linked list in groups of given size
def reverse_linked_list_in_groups(head, k):
    def reverse_group(head, k):
        prev, curr = None, head
        for _ in range(k):
            if not curr:
                return None
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy
    while prev_group_end:
        start = prev_group_end.next
        end = reverse_group(start, k)
        if not end:
            break
        prev_group_end.next = end
        prev_group_end = start
    return dummy.next

if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)
    head.next.next.next.next.next.next.next = ListNode(8)

    print("\nOriginal Linked List:")
    print_linked_list(head)

    k = 5  # Group size
    head = reverse_linked_list_in_groups(head, k)

    print("Linked List after Reversing in Groups of", k, ":")
    print_linked_list(head)


 #3. Merge a linked list into another linked list at alternate positions.
def merge_alternate_positions(head1, head2):
    curr1, curr2 = head1, head2
    while curr1 and curr2:
        temp1, temp2 = curr1.next, curr2.next
        curr1.next = curr2
        curr2.next = temp1
        curr1, curr2 = temp1, temp2

    return head1

if __name__ == "__main__":
    # Create the first linked list: 1 -> 3 -> 5 -> 7 -> 9
    head1 = ListNode(1)
    head1.next = ListNode(3)
    head1.next.next = ListNode(5)
    head1.next.next.next = ListNode(7)
    head1.next.next.next.next = ListNode(9)
    # Create the second linked list: 2 -> 4 -> 6 -> 8
    head2 = ListNode(2)
    head2.next = ListNode(4)
    head2.next.next = ListNode(6)
    head2.next.next.next = ListNode(8)

    print("\nFirst Linked List:")
    print_linked_list(head1)

    print("Second Linked List:")
    print_linked_list(head2)

    merged_head = merge_alternate_positions(head1, head2)

    print("Linked List after Merging at Alternate Positions:")
    print_linked_list(merged_head)

#4. In an array, Count Pairs with given sum
def count_pairs_with_sum(arr, target_sum):
    seen = set()
    count = 0
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            count += 1
        seen.add(num)
    return count

if __name__ == "__main__":
    arr = [1, 5, 7, -1, 5]
    target_sum = 6
    result = count_pairs_with_sum(arr, target_sum)
    print("\nNumber of pairs with the sum", target_sum, "in the array:", result)

#5. to find duplicates in an array:
def find_duplicates(arr):
    seen = set()
    duplicates = []
    for num in arr:
        if num in seen:
            duplicates.append(num)
        seen.add(num)
    return duplicates
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 2, 6, 3, 7, 8, 1, 4]
    result = find_duplicates(arr)
    print("\nDuplicates in the array:", result)
