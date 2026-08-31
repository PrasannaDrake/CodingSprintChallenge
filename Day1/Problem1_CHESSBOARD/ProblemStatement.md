# CHESSBOARD

![Chessboard]('https://media.istockphoto.com/id/1394093629/vector/chess-board-in-black-and-white-gameboard-for-leisure-or-sport-game-of-chess-vector.jpg?s=612x612&w=0&k=20&c=XhYECWO27u79m9MYwKjR3bprHCo4EDtSOwdqMe6RDWM=')

### Problem Statement: To determine whether a given chessboard square is Black or White

### Core Logic
      - Map letters to number
            - 'a' to 'h' --> 1 to 8.
      - Check Sum
            - Add column number and row number.
            - On standard chessboard bottom-left square a1 (1+1=2) is black.
            - Squares a2 (1+2=3) and b1 (2+1=3) are white.
      - Conclusion
            - If (column + row) is even, square is black.
            - If (column + row) is even, square is white.
