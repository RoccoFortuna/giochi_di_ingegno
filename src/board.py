"""
Define Game object containing a board to insert Pieces and solve the game.
"""
import copy

from typing import List
from pieces import display_2Dlist

# define type Piece that is a 2D array (list of lists of ints)
Piece = List[List[int]]

class PositionException(Exception):
    pass

class RemovalException(Exception):
    pass

class Game():
    """
    The game object holds the bord state,
    allows for insertion and removal of pieces.
    """
    def __init__(self, size: int = 7):
        self.board_size = size
        # initialize square board
        self.board = [[-1 for _ in range(size)] for _ in range(size)]


    def __str__(self):
        s = '\n '+'--'*self.board_size+'\n'
        for row in self.board:
            printed_row = '|'
            for element in row:
                printed_row += ' ' + str(element) if int(element) >= 0 else ' ' + '-'
            s += (str(printed_row) + '|\n')
        return s + ' ' + '--'*self.board_size


    def is_solvable(self) -> bool:
        """Check whether self.board does not contain empty islads of a number of blocks
        that is not divisible by 5.

        This method is used to prune the hopeless branches where <5 empty spaces have
        been surrounded by other pieces and can therefore not be filled by any 5-squares
        pieces, or empty islands of for example 9, which cannot be filled by any number
        of 5-squares pieces. This works with the assumption that the first positioned piece
        is the only 4-squares piece.

        Returns:
            bool: True if the board does not contain empty islands of 4 or less spaces
        """
        def get_surrounding_coors(board, y: int, x: int):
            return [(y+i, x+j) for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]\
                        if y+i >= 0 and y+i < self.board_size and x+j >= 0 and x+j < self.board_size]

        tmp = copy.deepcopy(self.board) # copy the board not to modify it
        for i in range(len(tmp)):
            row = tmp[i]
            for j in range(len(row)):
                element = row[j]
                if element == -1:       # if empty space is found
                    tmp[i][j] = -2      # mark as seen
                    count = 1           # initialize counter to 1
                    # list of following coordinates to check
                    to_discover = get_surrounding_coors(tmp, i, j)
                    while to_discover:
                        curr_y, curr_x = to_discover.pop()
                        if tmp[curr_y][curr_x] == -1: # if island extends, mark as seen and expand to surroundings
                            tmp[curr_y][curr_x] = -2 # set entry to -2 and expand to_discover
                            surr_coors = get_surrounding_coors(tmp, curr_y, curr_x)
                            to_discover.extend(surr_coors)
                            count += 1

                            # print(surr_coors)
                            # display_2Dlist(tmp)
                            # print(count)
                    if count % 5 != 0:
                        return False
        return True


    def is_insertable(self, piece: Piece, y: int, x: int) -> bool:
        """Check whether a piece can be inserted at a position (y, x)

        Check whether the given piece fits in the board boundaries
        at position (y, x), and whether it does not overlap with
        any previously inserted piece.


        Args:
            piece (Piece): the piece to be inserted
            y (int): the vertical position at which the piece would be inserted
            x (int): the horizontal position at which the piece would be inserted

        Returns:
            bool: True if the piece can be inserted at (y, x), False otherwise.
        """

        height = len(piece)
        width = len(piece[0])

        # Check if piece fits within board boundaries
        if x + width > self.board_size: # check if piece exceeds width of board
            return False
        if y + height > self.board_size: # check if piece exceeds height of board
            return False

        # Check if piece does not overlap with other pieces
        for i, row in enumerate(piece):
            for j, element in enumerate(row):
                if (not self.board[y+i][x+j] == -1) and (piece[i][j] == 1):
                    return False

        return True


    def insert_piece(self, piece: Piece, y: int, x: int, identifier: str):
        """Inserts piece in the game board at position (y, x)

        The shape of the piece is inserted in the board by changing
        the value of the board in the shape of the piece to the identifier

        Identifiers are strings of the form: 'p0'...'p9'

        Args:
            piece (Piece): the piece to insert on the board
            y (int): the vertical position at which the piece is inserted
            x (int): the horizontal position at which the piece is inserted
        """
        for i, row in enumerate(piece):
            for j, element in enumerate(row):
                if element == 1:
                    self.board[y+i][x+j] = identifier


    def remove_piece(self, piece: Piece, y: int, x: int, identifier: str):
        """[summary]

        Args:
            piece (Piece): the piece to remove from the board
            y (int): the vertical position from which the piece is removed
            x (int): the horizontal position from which the piece is removed
        """
        for i, row in enumerate(piece):
            for j, element in enumerate(row):
                if element == 1:
                    if self.board[y+i][x+j] != identifier:
                        raise RemovalException(\
                            f'Removing inexistent piece:\n{piece}\nfrom \
(y, x) = ({y}, {x}) in board:\n{self}')
                    self.board[y+i][x+j] = -1 # reset board value to empty



if __name__ == "__main__":
    from pieces import pieces, display_2Dlist

    # instantiate game
    g = Game()

    # display current board state
    print(g)

    # insert a piece
    piece_id = 2
    display_2Dlist(pieces[piece_id])
    g.insert_piece(pieces[piece_id], 2, 3, f'{piece_id}')

    # display new board state
    print(g)

    # try to remove piece from wrong position, then remove at right one
    try:
        g.remove_piece(pieces[piece_id], 3, 3, f'{piece_id}')
    except RemovalException as e:
        print(f'Exception occurred: {e}')
        print(g)
        g.remove_piece(pieces[piece_id], 2, 3, f'{piece_id}')
        print(g)
