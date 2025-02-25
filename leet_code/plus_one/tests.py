from plus_one import Solution


def main():
    sol = Solution()
    cases = [
        ([1, 2, 3], [1, 2, 4]),
    ]
    for case in cases:
        answer = sol.plusOne(digits=case[0])
        print(f"Resposta: {answer}\nEsperado: {case[1]}\n{answer==case[1]}")


if __name__ == "__main__":
    main()
