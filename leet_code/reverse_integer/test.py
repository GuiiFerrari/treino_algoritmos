from reverse import Solution


def main():
    sol = Solution()
    cases = [
        (123, 321),
        (100, 1),
    ]
    for case in cases:
        answer = sol.reverse(x=case[0])
        print(f"Resposta: {answer}\nEsperado: {case[1]}\n{answer==case[1]}")


if __name__ == "__main__":
    main()
