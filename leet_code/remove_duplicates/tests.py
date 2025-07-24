from algorithm import Solution, ListNode


def create_linked_list(values: list[int]) -> ListNode:
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def main():
    sol = Solution()
    cases = [
        # (create_linked_list([1, 1, 1, 2, 3]), create_linked_list([2, 3])),
        (create_linked_list([1, 2, 2]), create_linked_list([1])),
    ]
    for case in cases:
        answer = sol.deleteDuplicates(head=case[0])
        print(f"Resposta: {answer}\nEsperado: {case[1]}\n{answer==case[1]}")


if __name__ == "__main__":
    main()
