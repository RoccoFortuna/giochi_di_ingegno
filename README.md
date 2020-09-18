# Giochi di ingegno: cubi magici
A wooden puzzle that is surprisingly difficult, so much so that it haunted me throughout my childhood. I am now a few years older and more experienced, and am determined to defeat it with facts and logic!

Through the thorough use of Science, I wrote a Python program to solve the wicked puzzle (by means of a simple backtracking algorithm).

### Problem
The game rules are rather simple: there is a board of size 7x7, and 10 pieces. The first 9 pieces are all shapes that can be constructed by placing 5 squares of size 1 next to each other (that is, each 1x1-square must share a side with another 1x1 square). Note two shapes are considered the same if by rotating and/or mirroring one shape one can obtain the other. The 10th piece is a 2x2-square. Note that while each of the first 9 pieces is formed by 5 1x1-squares, the last 10th piece is formed by 4 1x1-squares. The total number of 1x1-squares is thus 49 and fits exactly in the 7x7-board.

%%% Will attach a figure later.
