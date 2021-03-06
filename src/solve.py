"""
Solve the puzzle with a backtracking algorithm.
The algorithm's pseudocode follows:

- keep track of possible positions to insert a piece,
- keep track of possible pieces to insert,
- keep track of the game's board state
- for each possible piece:
    - if it is not the first piece (tetroid) check if there are empty
        islands of n squares, with n not divisible by 5
    - get number of possible placements n_placements of given piece
    - for placement_state in range(n_placements):
        - for each possible position:
            - if piece can be inserted:
                - insert piece at position,
                - recurse with
                    - new possible positions,
                    - new list of pieces,
                    - new board state
                - once the branch is exhausted remove inserted
                    piece and try with next position
            - once all positions have been tried, try with next piece
        if placement_state is 3:
            transpose piece
        else:
            rotate piece clockwise
- if there are no pieces to be placed, all have been placed:
    return solution.
- else no solution was found:
    return
"""

from pieces import pieces, rotate_clockwise, transpose
from board import Game


def recurse(named_pieces, state, positions):
    for piece_idx in range(len(named_pieces)):
        piece_name, piece = named_pieces[piece_idx]
        if piece_name > 0 and not state.is_solvable():
            return
        n_placements = specific_n_placements[piece_name]
        for placement_state in range(n_placements):
            for position_idx, position in enumerate(positions):
                # print(f'piece: {piece_name}\tplacement: {placement_state}\tposition: {position}')
                # check if the piece can be inserted at the current position,
                # if it cannot, do nothing.
                # if it can,
                if state.is_insertable(piece, position[0], position[1]):
                    # MAKE CHANGE
                    # insert piece in board
                    state.insert_piece(piece, position[0], position[1], piece_name)
                    # make new list of pieces, excluding placed piece
                    new_pieces = named_pieces[:piece_idx] + named_pieces[piece_idx+1:]
                    # make new list of positions, excluding used positionSS
                    new_positions = positions[:position_idx] + positions[position_idx+1:]

                    # recurse with new pieces, state and positions
                    recurse(new_pieces, state, new_positions)

                    # REVERT CHANGE in state
                    state.remove_piece(piece, position[0], position[1], piece_name)
            if placement_state == 3: # time to mirror
                piece = transpose(piece)
            else: # otherwise rotate
                piece = rotate_clockwise(piece)
            # if all positions have been tried with this piece, keep going to next piece
        # if all placements have been tried, just keep going to next position/piece
    # if all pieces have been tried/placed:
    if len(named_pieces) == 0:  # if they have all been placed
        print(state)            # show end result
        with open('solutions.txt', 'a+') as f:
            f.write(str(state))
        return
    else:                       # otherwise
        print(f'Unsuccessful attempt:')
        print(state)
        return                  # return to previous recursion state

if __name__ == "__main__":
    named_pieces = list(zip([i for i in range(len(pieces))], pieces))
    state = Game()
    positions = [(y, x) for y in range(state.board_size) for x in range(state.board_size)]

    # some pieces should not be rotated (p0, p5),
    # some can be rotated, but should not be mirrored (p4, p6)
    # finally, p9 should only be rotated and once.
    # all other pieces should be rotated (4 states), then mirrored (5th state)
    # and rotated three more times: 4+4=8 states
    specific_n_placements = [1, 8, 8, 8, 4, 1, 4, 8, 8, 2]
    # initialise start state: all pieces, empty board, all possible positions
    named_pieces = list(zip([i for i in range(len(pieces))], pieces))
    state = Game()
    positions = [(y, x) for y in range(state.board_size) for x in range(state.board_size)]

    # begin recursion
    recurse(named_pieces, state, positions)
