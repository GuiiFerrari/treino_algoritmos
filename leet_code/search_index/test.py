from search_index import Solution


def main():
    sol = Solution()
    cases = [
        ([1, 3, 5, 6], 7, 4),
        ([1], 0, 0),
        ([1, 3], 0, 0),
        ([1, 2, 4, 6, 7], 3, 2),
        ([1, 3, 5, 6], 2, 1),
    ]
    for case in cases:
        answer = sol.searchInsert(nums=case[0], target=case[1])
        print(f"Resposta: {answer}\nEsperado: {case[2]}\n{answer==case[2]}")


if __name__ == "__main__":
    main()
