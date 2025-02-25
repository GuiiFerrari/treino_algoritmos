def main():
    num = 123
    exp = 10
    while True:
        q, r = divmod(num, exp)
        print(q, r, exp)
        if q == 0:
            break
        exp *= 10


if __name__ == "__main__":
    main()
