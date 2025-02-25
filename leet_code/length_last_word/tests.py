from algorithm import Solution


def main():
    sol = Solution()
    cases = [
        ("a", 1),
    ]
    for case in cases:
        answer = sol.lengthOfLastWord(s=case[0])
        print(f"Resposta: {answer}\nEsperado: {case[1]}\n{answer==case[1]}")


if __name__ == "__main__":
    main()
