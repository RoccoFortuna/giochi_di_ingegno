"""
Store and handle pieces.
There are 10 pieces, each represented as a 2D binary array (Piece = List[List[int]]).
"""

from typing import List

# define type Piece that is a 2D array (list of lists of ints)
Piece = List[List[int]]

p0 = [[1, 1],
      [1, 1]]

p1 = [[1, 1, 1, 1],
      [0, 0, 0, 1]]

p2 = [[1, 1, 1, 1],
      [0, 0, 1, 0]]

p3 = [[1, 0, 0],
      [1, 1, 1],
      [0, 1, 0]]

p4 = [[1, 1, 1],
      [0, 0, 1],
      [0, 0, 1]]

p5 = [[0, 1, 0],
      [1, 1, 1],
      [0, 1, 0]]

p6 = [[1, 1],
      [0, 1],
      [1, 1]]

p7 = [[1, 1, 1],
      [0, 1, 1]]

p8 = [[1, 1, 0],
      [0, 1, 0],
      [0, 1, 1]]

p9 = [[1, 1, 1, 1, 1]]

pieces = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9]

def display_2Dlist(p):
    """Prints a piece, or each Piece in a list, to output.

    Args:
        p (Union[Piece, List[Piece]]): Piece, or list of Pieces, to print to output
    """
    # helper function to display a piece
    def dis(p):
        for row in p:
            print(row)

    def is_piece(p):
        return type(p[0][0]) == int


    if is_piece(p): # if input is a single piece
        dis(p)              # diaplay the piece
        print()
    else:                   # if input is a list of pieces
        for piece in p:     # display every piece in the list
            dis(piece)
            print()


def display_all(pieces):
    """Displays all pieces (from p0 to p9).

    Args:
        pieces (List[Piece]): list containing all Pieces
    """
    for i, p in enumerate(pieces):
        print()             # print new line to separate Pieces visually
        print(f'p{i}')      # log what piece is being printed
        display_piece(p)    # display piece


def rotate_clockwise(p: Piece) -> Piece:
    """Returns piece rotated clockwise

    Args:
        p (Piece): piece to rotate

    Returns:
        (Piece): piece rotated clockwise
    """
    return [list(l) for l in zip(*p[::-1])]


def transpose(p: Piece) -> Piece:
    """
    Transpose given Piece p.

    e.g.
    Piece p2:
    [[1, 1, 1, 1],
     [0, 0, 1, 0]]

    will become:
    [[1, 0],
     [1, 0],
     [1, 1],
     [1, 0]]

    Args:
        p (Piece): Piece to transpose

    Returns:
        Piece: transposed pieece
    """
    return [list(l) for l in zip(*p)]


def to_be_transposed(p) -> bool:
    """Returns True if transposing is not equivalent to rotating, False otherwise

    If transposing is equivalent to rotating twice, it is not necessary to
    transpose and branch the recursion for the additional move. Instead three
    rotations will be equivalent.

    Args:
        p (Piece): piece to be checked for whether transposing is necessary.

    Returns:
        bool: True if transposing is necessary, False otherwise.
    """
    q = p[:]
    d = transpose(p[:])
    for i in range(2):
        q = rotate_clockwise(q)
        if q == d:
            return False
    return True
