def main() -> None:
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    # 上、右、下、左、右上、右下、左下、左上
    direction_x = [-1, 0, 1, 0, -1, 1, 1, -1]
    direction_y = [0, 1, 0, -1, 1, 1, -1, -1]

    pattern = ["s", "n", "u", "k", "e"]

    for i in range(H):
        for j in range(W):
            if S[i][j] == "s":
                for k in range(8):
                    flag = True
                    coords = [(i + 1, j + 1)]
                    for l in range(1, 5):
                        next_i = i + l * direction_x[k]
                        next_j = j + l * direction_y[k]
                        if (
                            next_i < 0
                            or next_i >= H
                            or next_j < 0
                            or next_j >= W
                            or S[next_i][next_j] != pattern[l]
                        ):
                            flag = False
                            break

                        coords.append((next_i + 1, next_j + 1))

                    if flag:
                        for coord in coords:
                            print(*coord)
                        return


if __name__ == "__main__":
    main()
