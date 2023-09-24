"""
https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm
The Smith-Waterman algorithm is a dynamic programming algorithm used for sequence
alignment.It is particularly useful for finding similarities between two sequences,
such as DNA or protein sequences. In this implementation, gaps are penalized
linearly,meaning that the scoreis reduced by a fixed amount for each gap introduced
in the alignment. It's important to notethat the Smith-Waterman algorithm supports
other gap penalty methods as well, but in thisspecific implementation, linear gap
penalties are used.
"""
# Score constants: matches are given a positive score while mismatches are given a
# negative score. Gaps are also penalized linearly.
MATCH = 1
MISMATCH = -1
GAP = -2


def score_function(source_char: str, target_char: str) -> int:
    """
    Calculate the score for a character pair based on whether they match or mismatch.
    Returns 1 if the characters match, -1 if they mismatch, and -2 if either of the
    characters is a gap.
    >>> score_function('A', 'A')
    1
    >>> score_function('A', 'C')
    -1
    >>> score_function('-', 'A')
    -2
    >>> score_function('A', '-')
    -2
    >>> score_function('-', '-')
    -2
    """
    if "-" in (source_char, target_char):
        return GAP
    return MATCH if source_char == target_char else MISMATCH


def smith_waterman(query: str, subject: str) -> list[list[int]]:
    """
    Perform the Smith-Waterman local sequence alignment algorithm.
    Returns a 2D list representing the score matrix. Each value in the matrix
    corresponds to the score of the best local alignment ending at that point.
    >>> smith_waterman('ACAC', 'CA')
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]]
    >>> smith_waterman('acac', 'ca')
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]]
    >>> smith_waterman('ACAC', 'ca')
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]]
    >>> smith_waterman('acac', 'CA')
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]]
    >>> smith_waterman('ACAC', '')
    [[0], [0], [0], [0], [0]]
    >>> smith_waterman('', 'CA')
    [[0, 0, 0]]
    """
    # make both query and subject uppercase
    query = query.upper()
    subject = subject.upper()

    # Initialize score matrix
    m = len(query)
    n = len(subject)
    score = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calculate scores for each cell
            match = score[i - 1][j - 1] + score_function(query[i - 1], subject[j - 1])
            delete = score[i - 1][j] + GAP
            insert = score[i][j - 1] + GAP

            # Take maximum score
            score[i][j] = max(0, match, delete, insert)

    return score


def traceback(score: list[list[int]], query: str, subject: str) -> str:
    r"""
    Perform traceback to find the optimal local alignment.
    Starts from the highest scoring cell in the matrix and traces back recursively
    until a 0 score is found. Returns the alignment strings.
    >>> traceback([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]], 'ACAC', 'CA')
    'CA\nCA'
    >>> traceback([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]], 'acac', 'ca')
    'CA\nCA'
    >>> traceback([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]], 'ACAC', 'ca')
    'CA\nCA'
    >>> traceback([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]], 'acac', 'CA')
    'CA\nCA'
    >>> traceback([[0, 0, 0]], 'ACAC', '')
    ''
    """
    # make both query and subject uppercase
    query = query.upper()
    subject = subject.upper()
    # find the indices of the maximum value in the score matrix
    max_value = float("-inf")
    i_max = j_max = 0
    for i, row in enumerate(score):
        for j, value in enumerate(row):
            if value > max_value:
                max_value = value
                i_max, j_max = i, j
    # Traceback logic to find optimal alignment
    i = i_max
    j = j_max
    align1 = ""
    align2 = ""
    # guard against empty query or subject
    if i == 0 or j == 0:
        return ""
    while i > 0 and j > 0:
        if score[i][j] == score[i - 1][j - 1] + score_function(
            query[i - 1], subject[j - 1]
        ):
            # optimal path is a diagonal take both letters
            align1 = query[i - 1] + align1
            align2 = subject[j - 1] + align2
            i -= 1
            j -= 1
        elif score[i][j] == score[i - 1][j] + GAP:
            # optimal path is a vertical
            align1 = query[i - 1] + align1
            align2 = f"-{align2}"
            i -= 1
        else:
            # optimal path is a horizontal
            align1 = f"-{align1}"
            align2 = subject[j - 1] + align2
            j -= 1

    return f"{align1}\n{align2}"


if __name__ == "__main__":
    query = "HEAGAWGHEE"
    subject = "PAWHEAE"

    score = smith_waterman(query, subject)
    print(traceback(score, query, subject))
