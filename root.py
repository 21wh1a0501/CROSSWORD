#to generate copy matrix
def copymatrix1(r, c, puzzle):
    copy = [[0 for _ in range(c)] for _ in range(r)]
    start = 0
    for i in range(r):
        for j in range(c):
            if puzzle[i][j] != '*' and (i == 0 or j == 0 or puzzle[i][j - 1] == '*' or puzzle[i - 1][j] == '*'):
                copy[i][j] = start + 1
                start += 1
    return copy
#to generate across words
def across1(r, c, puzzle, copy):
    across_clues = []
    for i in range(r):
        j = 0
        while j < c:
            if puzzle[i][j] == '*':
                j += 1
                continue
            if j < c:
                clue_number = copy[i][j]
                clue_text = ''
                while j < c and puzzle[i][j] != '*':
                    clue_text += puzzle[i][j]
                    j += 1
                across_clues.append((clue_number, clue_text))
    return across_clues
#to generate down words
def down1(r, c, puzzle, copy):
    down_clues = []
    for i in range(r):
        for j in range(c):
            if puzzle[i][j] == '*' or copy[i][j] == 0:
                continue
            clue_number = copy[i][j]
            clue_text = ''
            k = i
            while k < r and puzzle[k][j] != '*':
                clue_text += puzzle[k][j]
                copy[k][j] = 0
                k += 1
            down_clues.append((clue_number, clue_text))
    return down_clues