"""
Boggle is a word game that involves constructing words
(as defined in a dictionary) from letters arranged on
a N x N board.

The game has the following rules:

- The dictionary defines all the potential words.

- Words are constructed by connecting letters together.
  A letter can only be connected with another letter next
  to it.

- You may not use any given letter coordinate more than
  once per word.

Your objective is to write a method that takes a board and
a dictionary as arguments, and returns all of the valid words
on the board. Duplicate words are permitted.

Your method should have the following signature:

  findWords(board, dictionary)

Here's an example of a boggle board, represented in this case
as a 3x3 matrix:

  [["p", "e", "a"],
   ["i", "n", "p"],
   ["e", "l", "p"]]

And an example of a dictionary, represented in this case as
an array of strings:

  ["app", "apple", "elk", "ent", "lan", "lei", "nap", "nil", "pane",
  "pea", "pen", "pie", "pin", "pine", "pineapple", "pip", "zilch"]

Some examples using the example board and dictionary above:

- "pane" is a valid word. We can construct it by starting at
  the "p" at (row 2, column 3) moving up to "a", moving
  diagonally to "n", and up to "e".

- "pip" is not a valid word. It could be constructed by
  starting at the "p" at (row 0, column 0), moving down
  to "i" and then back up to "p", but that reuses the
  (row 0, column 0) letter coordinate and is thus invalid.

- "lan" is not a valid word. The letters "l", "a", and "n"
  are on the board, but there is no way to move to them in
  a sequentially adjacent manner.

- "elk" is not a valid word. It is in the dictionary, but
  there is no "k" on the board and so can't be constructed.

If you decide to use the example board and dictionary above
to test your solution, here are words that a correct solution
would find:

  app, apple, lei, nap, nil, pane, pea, pen, pie, pin, pine, pineapple

And here are words that a correct solution would not find:

  elk, ent, lan, pip, zilch
"""
