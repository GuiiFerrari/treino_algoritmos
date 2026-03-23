from algorithm import Solution


def main():
    sol = Solution()
    cases = [
        ([1, 1, 2, 2, 3, 3, 4, 4, 5], 5),
        # ([1], 1),
        # ([1, 2, 2], 1),
        # ([1, 1, 2], 2),
        # ([1, 2, 3, 3], 2),
        # ([1, 2, 3], 3),
        # ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
    ]
    for case in cases:
        answer = sol.singleNonDuplicate(nums=case[0])
        print(f"Resposta: {answer}\nEsperado: {case[1]}\n{answer == case[1]}")


if __name__ == "__main__":
    main()
