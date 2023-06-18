import collections


def main() -> None:
    s = input()
    t = input()
    s_count = collections.defaultdict(int)
    t_count = collections.defaultdict(int)
    for c in s:
        s_count[c] += 1
    for c in t:
        t_count[c] += 1

    for c in "atcoder":
        max_at_nums = max(s_count[c], t_count[c])
        if (
            s_count["@"] < max_at_nums - s_count[c]
            or t_count["@"] < max_at_nums - t_count[c]
        ):
            print("No")
            return

        s_count["@"] -= max_at_nums - s_count[c]
        s_count[c] = max_at_nums
        t_count["@"] -= max_at_nums - t_count[c]
        t_count[c] = max_at_nums

    print("Yes" if s_count == t_count else "No")


if __name__ == "__main__":
    main()
