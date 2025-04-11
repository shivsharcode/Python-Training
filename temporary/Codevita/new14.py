from typing import List

display_map = {
    92229: ['A', 'D'], 93339: ['B'], 92222: ['C', 'F'], 93333: ['E'], 92336: ['G'],
    91119: ['H', 'N', 'U'], 22322: ['I'], 62229: ['J'], 92226: ['K'], 91111: ['L'],
    91519: ['M', 'W'], 72227: ['O'], 92225: ['P'], 92339: ['Q'], 93336: ['R'],
    63336: ['S'], 11911: ['T'], 71117: ['V'], 22122: ['X'], 62226: ['Y'], 23332: ['Z']
}


def check_chr(s: int, line: List[str]) -> str:
    val_str = ""
    for i in range(5):
        t = 0
        for j in range(9):
            t += int(line[j][s + i])
        val_str += str(t)
    val = int(val_str)

    if val == 91519:
        return 'M' if line[0][s:s + 5] == "11111" else 'W'
    elif val == 91119:
        if line[8][s:s + 5] == "11111":
            return 'U'
        if line[4][s:s + 5] == "11111":
            return 'H'
        return 'N'
    elif val == 92222:
        return 'F' if line[4][s:s + 5] == "11111" else 'C'
    elif val == 92229:
        return 'D' if line[8][s:s + 5] == "11111" else 'A'
    else:
        return display_map[val][0]


def segment_display(line: List[str]) -> str:
    tb = len(line[0])
    merged = list(line[0])
    for i in range(1, 9):
        for j in range(tb):
            merged[j] = str(int(merged[j]) | int(line[i][j]))

    merged = "".join(merged)
    result = ""
    s = 0
    while s < tb:
        if merged[s] == '1':
            result += check_chr(s, line)
            s += 5
        else:
            s += 1
    return result


if __name__ == "__main__":
    t = 9
    line = [input() for _ in range(t)]
    ans = segment_display(line)
    print(ans, end="")
