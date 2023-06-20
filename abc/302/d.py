import bisect


def main() -> None:
    N, M, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    res = -1

    for b in B:
        i = bisect.bisect_right(A, b + D) - 1
        if i >= 0 and A[i] >= b - D:
            res = max(res, A[i] + D)

    print(res)


if __name__ == "__main__":
    main()
