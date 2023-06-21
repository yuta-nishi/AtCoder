import bisect


def main() -> None:
    N, M, D = map(int, input().split())
    A = sorted(map(int, input().split()))
    B = map(int, input().split())

    res = -1

    for b in B:
        i = bisect.bisect_right(A, b + D) - 1
        if i >= 0 and A[i] >= b - D:
            res = max(res, A[i] + b)
    print(res)


if __name__ == "__main__":
    main()
