def main() -> None:
    X, Y, Z = map(int, input().split())
    S = input()

    dp_on = [Z] + [float("inf")] * len(S)
    dp_off = [0] + [float("inf")] * len(S)

    for i in range(len(S)):
        if S[i] == "a":
            dp_on[i + 1] = min(dp_on[i] + Y, dp_off[i] + Z + Y)
            dp_off[i + 1] = min(dp_off[i] + X, dp_on[i] + Z + X)
        elif S[i] == "A":
            dp_on[i + 1] = min(dp_on[i] + X, dp_off[i] + Z + X)
            dp_off[i + 1] = min(dp_off[i] + Y, dp_on[i] + Z + Y)

    res = min(dp_on[-1], dp_off[-1])
    print(res)


if __name__ == "__main__":
    main()
