def main() -> None:
    N, M, H, K = map(int, input().split())
    S = input()
    items = set(tuple(map(int, input().split())) for _ in range(M))

    x = 0
    y = 0

    for i in range(N):
        if S[i] == "R":
            x += 1
        elif S[i] == "L":
            x -= 1
        elif S[i] == "U":
            y += 1
        elif S[i] == "D":
            y -= 1

        H -= 1

        if H < 0:
            print("No")
            return
        elif H < K and (x, y) in items:
            items.remove((x, y))
            H = K

    print("Yes" if H >= 0 else "No")


if __name__ == "__main__":
    main()
