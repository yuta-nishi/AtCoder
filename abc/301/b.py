def main() -> None:
    N = int(input())
    A = list(map(int, input().split()))

    res = [A[0]]
    for i in range(N - 1):
        if abs(A[i] - A[i + 1]) > 1:
            if A[i] < A[i + 1]:
                res += list(range(A[i] + 1, A[i + 1]))
            else:
                res += list(range(A[i] - 1, A[i + 1], -1))
        res.append(A[i + 1])

    print(*res)


if __name__ == "__main__":
    main()
