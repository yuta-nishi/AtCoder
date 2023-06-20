import itertools


def main() -> None:
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]

    def check(a: str, b: str) -> bool:
        diff = sum([1 if a[i] != b[i] else 0 for i in range(M)])
        return diff == 1

    for perm in itertools.permutations(S):
        if all([check(perm[i], perm[i + 1]) for i in range(N - 1)]):
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
