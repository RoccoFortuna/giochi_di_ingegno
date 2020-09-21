# Giochi di ingegno: cubi magici
"Giochi di ingegno: cubi magici" (in English "Ingenuity games: magic cubes") is a surprisingly difficult wooden puzzle we used to have at home, that haunted me throughout my childhood with its monstrous state-space. Now that I am a few years older and don't believe in monsters anymore, I am hopeful that with the couple of degrees and the determination I now have I'll be able to defeat it by means of Science.

Therefore, I wrote a Python program to solve the wicked puzzle.

## The Wicked Puzzle
The game rules are rather simple: there is a board of size 7x7, and 10 pieces. There is one piece of 4 squares (a 2x2 tetroid) and 9 pieces of 5 squares (pentoids). The total number of 1x1-squares is thus 49 and fits exactly in the 7x7-board. The goal of the puzzle is in fact to fill it by using every piece once. 

Following are the board and available pieces:
![](/images/board_and_pieces.png)

## State-space
The state space of this puzzle is simply huge. Each of the 10 pieces can be placed anywhere within the boundaries of the board. Pieces can also be rotated by 90 degrees any number of times and mirrored. Fortunately, the rotation or mirroring of some pieces yields the very same shape, and is therefore not necessary: piece `p0` is unmodified once rotated or mirrored, just like `p5`, due to their horizontal, vertical and diagonal symmetry and have thus only one possible placement. Piece `p9` only needs to be rotated once, as rotating it twice yields the same orientation as not rotating it at all and mirroring it yields itself again, and has thus 2 placements. Pieces `p4` and `p6` only need to be rotated at most thrice, as the mirrored shape can be achieved by rotation as well, which gives them 4 possible placements (non rotated or rotated once, twice or thrice). Finally pieces `p1`, `p2`, `p3`, `p7` and `p8` can be rotated thrice, then mirrored and rotated three more times, yielding 8 different placements.

## Methodology
The chosen approach involves a backtracking algorithm which recursively inserts pieces in an iterative fashion, tries all possible positions within the board boundaries that do not make the piece overlap with any other piece, rotates and mirrors them, and goes back to previous checkpoints when reaching an unsolvable board state.

### Pruning
Given the size of the state space, a pruning mechanism is essential to explore at least a meaningful subset of it.
Define an `empty island` in the board as an empty region of the board such that it is surrounded by pieces or the board's boundaries. By inserting the only tetroid `p0` first, all we are left with are pentoids (pieces formed with 5 1x1 squares: `p1`, ..., `p9`). This means that any empty island can only be filled if it has area `n`, such that `n` is a multiple of 5 (`n%5 == 0`). Every time a new piece is inserted in the board, the board is checked for empty islands, to make sure that no island is of incompatible area rendering the current board unsolvable by inserting the remaining pieces in any way. If the board results unsolvable, the branch is pruned, substantially speeding up the search.

### The Algorithm
Following is the complete pseudocode (somewhat pythonized) of the backtracking algorithm:

```
- keep track of possible positions to insert a piece,
- keep track of possible pieces to insert,
- keep track of the game's board state
- keep track of each piece's possible placements (rotation/mirroring)
- for each possible piece:
    - if it is not the first piece (tetroid) check if there are empty islands of n squares, with n not divisible by 5
    - get number of possible placements n_placements of given piece
    - for placement_state in range(n_placements):
        - for each possible position:
            - if piece can be inserted:
                - insert piece at position,
                - recurse with
                    - new possible positions (exclude used position),
                    - new list of pieces (exclude used pieces),
                    - new board state (including newly placed piece).
                - once the branch is exhausted remove inserted piece and try with next position
            - once all positions have been tried, try with next piece
        if placement_state is 3:
            transpose piece
        else:
            rotate piece clockwise
- if there are no pieces to be placed, all have been placed:
    - return solution
- else this branch did not produce a solution:
    return
```

## Results
Despite the state-space being too big and my resources not being able to store the entire recursion tree until the program's termination (not even close), the algorithm successfully identified a valid solution on the way:

![](/images/solution.png)

## Conclusions
The program worked to the extent that a solution was found, but many more are probably out there waiting for my recursion to dig deeper.
Future work could involve running the recursion with higher memory/processing resources, or split the search of the gigantic state-space throughout multiple random initializations in a Monte Carlo-like approach, to explore different regions of the state space on separate runs.
