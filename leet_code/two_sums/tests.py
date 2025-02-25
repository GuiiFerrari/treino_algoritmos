from two_sums import Solution


def main():
    sol = Solution()
    cases = [
        ([3, 2, 4], 6, [1, 2]),
        ([2, 7, 11, 15], 9, [0, 1]),
    ]
    for case in cases:
        answer = sol.twoSum(nums=case[0], target=case[1])
        print(f"Resposta: {answer}\nEsperado: {case[2]}\n{answer==case[2]}")


if __name__ == "__main__":
    main()
