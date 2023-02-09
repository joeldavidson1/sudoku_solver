# import libraries here. Use the following ones only.
import random
import time


class SudokuBoard:
    """A class containing all the related attributes and methods pertaining to the layout and functions
     required for a sudoku board.

    Attributes:
        guesses: If not entered then a list of guesses from 1 - 9 in string format is created.
        sudoku_game: Allows user to change the sudoku board, but if not entered then the original sudoku game in
        if __name__ == '__main__': is used.
    """

    def __init__(self, guesses=None, sudoku_game=None):
        """Initialises SudokuBoard with the user guesses and the sudoku game."""
        if guesses is None:
            self.guesses = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        if sudoku_game is None:
            self.sudoku_game = sudoku

    def original_board(self):
        """Returns board back to the initial layout."""
        self.sudoku_game = [
            [' ', ' ', ' ', '3', ' ', ' ', ' ', '7', ' '],
            ['7', '3', '4', ' ', '8', ' ', '1', '6', '2'],
            ['2', ' ', ' ', ' ', ' ', ' ', ' ', '3', '8'],
            ['5', '6', '8', ' ', ' ', '4', ' ', '1', ' '],
            [' ', ' ', '2', '1', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', '7', '8', ' ', ' ', '2', '5', '4'],
            [' ', '7', ' ', ' ', ' ', '2', '8', '9', ' '],
            [' ', '5', '1', '4', ' ', ' ', '7', '2', '6'],
            ['9', ' ', '6', ' ', ' ', ' ', ' ', '4', '5'],
        ]

    def get_hint(self):
        """Uses a completed board layout to return hints to the user."""
        completed_board = [
            ['6', '8', '5', '3', '2', '1', '4', '7', '9'],
            ['7', '3', '4', '9', '8', '5', '1', '6', '2'],
            ['2', '1', '9', '6', '4', '7', '5', '3', '8'],
            ['5', '6', '8', '2', '7', '4', '9', '1', '3'],
            ['3', '4', '2', '1', '5', '9', '6', '8', '7'],
            ['1', '9', '7', '8', '3', '6', '2', '5', '4'],
            ['4', '7', '3', '5', '6', '2', '8', '9', '1'],
            ['8', '5', '1', '4', '9', '3', '7', '2', '6'],
            ['9', '2', '6', '7', '1', '8', '3', '4', '5'],
        ]
        for row in range(9):
            for column in range(9):
                if self.sudoku_game[row][column] != completed_board[row][column]:
                    return f"Fill position {row, column} with {completed_board[row][column]}."

    def equal_boards(self):
        """Checks to see if the user completed board is equal to the correct completed board and returns True or False.
        """
        completed_board = [
            ['6', '8', '5', '3', '2', '1', '4', '7', '9'],
            ['7', '3', '4', '9', '8', '5', '1', '6', '2'],
            ['2', '1', '9', '6', '4', '7', '5', '3', '8'],
            ['5', '6', '8', '2', '7', '4', '9', '1', '3'],
            ['3', '4', '2', '1', '5', '9', '6', '8', '7'],
            ['1', '9', '7', '8', '3', '6', '2', '5', '4'],
            ['4', '7', '3', '5', '6', '2', '8', '9', '1'],
            ['8', '5', '1', '4', '9', '3', '7', '2', '6'],
            ['9', '2', '6', '7', '1', '8', '3', '4', '5'],
        ]
        for row in range(9):
            for column in range(9):
                if self.sudoku_game[row][column] != completed_board[row][column]:
                    return False
        return True

    def is_board_full(self):
        """Checks to see if the board is full and returns True or False."""
        for row in self.sudoku_game:
            for number in row:
                if ' ' == number:
                    return False
        return True

    def fill_board(self):
        """Randomly fills the board with numbers."""
        for row in range(9):
            for column in range(9):
                for _ in self.guesses:
                    if self.sudoku_game[row][column] == ' ':
                        self.sudoku_game[row][column] = random.choice(
                            self.guesses)

    def get_game_state(self):
        """Prints one of three different strings to the user depending on the game state."""
        if not self.is_board_full():
            print("No outcome, game continues.")
        if self.is_board_full() and self.equal_boards():
            print("Congratulations, you have solved the sudoku.")
        elif self.is_board_full() and not self.equal_boards():
            print("This sudoku has failed to be solved, better luck next time.")

    def update_board(self, row, column, user_guess):
        """Prints out an updated version of the board.

        Args:
            row: integer row of the board.
            column: integer column of the board.
            user_guess: the user entered guess.

        Returns:
            Prints out an updated version of the board with the latest user input, calling the print_board
            function to display the board layout correctly.
        """
        if self.sudoku_game[row][column] == ' ':
            # Enters users guess at the location.
            self.sudoku_game[row][column] = str(user_guess)
        elif self.sudoku_game[row][column] != ' ':
            # Finds the latest user guess.
            self.sudoku_game[row][column] = str(user_guess)
        print("****************** Updated Board ******************")
        self.print_board()

    def print_board(self):
        """Prints out a formatted, easily readable sudoku board."""
        print("-" * 49)
        for i in range(9):
            print("|", str(self.sudoku_game[i][0:3]).strip("[]").replace(",", " "), "|",
                  str(self.sudoku_game[i][3:6]).strip(
                      "[]").replace(",", " "), "|",
                  str(self.sudoku_game[i][6:9]).strip("[]").replace(",", " "), "|")
            if i == 5 or i == 2:
                print("-" * 49)

        print("-" * 49)


class SudokuSolver(SudokuBoard):
    """A subclass inherited from SudokuBoard allowing the sudoku board to be solved via a backtracking algorithm."""

    def locate_empty(self):
        """Finds an empty space on the board and returns the location as a tuple or None if not found."""
        for row in range(9):
            for column in range(9):
                if self.sudoku_game[row][column] == ' ':
                    return row, column
        return None

    def is_valid(self, number, position):
        """Checks to see if the number entered at a position on the board is valid according to sudoku rules.

        Args:
            number: the number to be entered on the board.
            position: the tuple position of a row then column (y, x coordinates.)

        Returns:
            Only returns true if the number at that position is valid, false otherwise.
        """
        for i in range(9):
            # Checks row validity.
            if self.sudoku_game[position[0]][i] == number and position[1] != i:
                return False

        for i in range(9):
            # Checks column validity.
            if self.sudoku_game[i][position[1]] == number and position[0] != i:
                return False

        # Finds the box using integer division, each box is either 0, 1 or 2. Loops through all elements in the
        # box and checks the validity.
        x_box_position = position[1] // 3
        y_box_position = position[0] // 3
        for i in range(y_box_position * 3, y_box_position * 3 + 3):
            for j in range(x_box_position * 3, x_box_position * 3 + 3):
                if self.sudoku_game[i][j] == number and (i, j) != position:
                    return False

        return True

    def solve_sudoku(self):
        """Solves the sudoku board via a backtracking algorithm."""
        # Base case for recursion.
        located = self.locate_empty()
        if not located:
            return True
        else:
            row, column = located

        # If there is a position to a fill then it makes a guess between 1 - 9 and checks to see if valid, then adds
        # it to the board.
        for guess in self.guesses:
            if self.is_valid(guess, (row, column)):
                self.sudoku_game[row][column] = guess

                if self.solve_sudoku():  # Recursively calls the function until solved.
                    return True

                # Backtracks and resets the last element if not correct.
                self.sudoku_game[row][column] = ' '

        return False


class HumanPlay(SudokuSolver):
    """A subclass inherited from SudokuSolver allowing the user to play a game of sudoku."""

    def human_play(self):
        """Allows the user to play the game of sudoku from start to finish with the guesses they enter.

        Returns:
            Prints the users guess to the board using exception handling on each iteration of the while loop
            ensuring only valid guesses are used.
        """
        start_time = time.time()  # Initialises the start time for the CPU runtime.
        valid_moves = 0
        invalid_moves = 0
        print("Welcome to Human Mode. Please follow the instructions to play.")
        print("***************** Original Board *****************")
        self.print_board()

        while True:
            # Ask for the user's row.
            try:
                row_position = int(input("Enter a row from 0-8: "))
            except ValueError:
                print("Row must be an integer between 0-8. Please enter valid input.")
                continue
            if row_position < 0 or row_position > 8:
                print("Row must be an integer between 0-8. Please enter valid input.")
                continue

            # Ask for the user's column.
            try:
                column_position = int(input("Enter a column from 0-8: "))
            except ValueError:
                print("Column must be an integer between 0-8. Please enter valid input.")
                continue
            if column_position < 0 or column_position > 8:
                print("Column must be an integer between 0-8. Please enter valid input.")
                continue

            # Ask for the user's guess.
            try:
                user_guess = int(
                    input("Enter a number to guess between 1-9: "))
            except ValueError:
                print("Your guess must be between 1-9.")
                continue
            if user_guess < 1 or user_guess > 9:
                print("Your guess must be between 1-9.")
                continue

            # Places the guess on the board.
            user_guess = str(user_guess)
            if user_guess in self.guesses and self.is_valid(user_guess, (row_position, column_position)) and \
                    (self.sudoku_game[row_position][column_position] == ' '):
                self.update_board(row_position, column_position, user_guess)
                valid_moves += 1
            else:
                print("Your guess is not valid.")
                invalid_moves += 1
                continue

            # Checks whether the board is full and gets the game state.
            if self.is_board_full():
                self.get_game_state()
                print("Thank you for playing. Sending you back to the main menu... ")
                start_game(human, computer)

            self.get_game_state()

            options = input("Enter 'q' to quit, 'h' if you'd like a hint, and 'w' to withdraw your last move."
                            " Enter anything else to continue playing. ").lower()
            if options == "h":
                print(self.get_hint())
                withdraw_move = input("Would you like to withdraw the move now you've seen the hint? Enter 'y' for yes"
                                      " or enter anything else to continue playing. ").lower()
                if withdraw_move == "y":
                    if self.sudoku_game[row_position][column_position] == user_guess:
                        # Withdraws user's guess.
                        self.update_board(
                            row_position, column_position, user_guess=' ')
                        continue
                    else:
                        break
            elif options == "q":
                self.fill_board()
                self.print_board()
                print(f"Thank you for playing, your number of valid moves was {valid_moves}, and the number of invalid"
                      f" moves was {invalid_moves}. The board has been randomly filled.")
                # Subtracts the current time from the start time to obtain total CPU runtime, rounded to 3 d.p.
                print(
                    f"Total CPU runtime taken for this game: {round(time.time() - start_time, 3)} seconds.")
                break
            elif options == "w":
                if self.sudoku_game[row_position][column_position] == user_guess:
                    self.update_board(
                        row_position, column_position, user_guess=' ')
                    continue
            else:
                continue


class ComputerPlay(SudokuSolver):
    """A subclass inherited from SudokuSolver allowing the computer to solve the sudoku via the
     solve_sudoku function.
    """

    def computer_play(self):
        start_time = time.time()
        print("Welcome to Computer Mode. The computer will now solve the sudoku puzzle for you.")
        print("***************** Original Board *****************")
        self.print_board()
        self.solve_sudoku()
        print("****************** Solved Board ******************")
        self.print_board()
        print("This sudoku has been solved by the computer.")
        print(
            f"Total CPU runtime taken to solve the sudoku: {round(time.time() - start_time, 3)} seconds.")


def start_game(human, computer):
    """Starts the game of sudoku and displays options to the user.

    Args:
        human: Uses the human class.
        computer: Uses the computer class.

    Returns:
        Prints original welcome message and allows the user to play the game by calling different classes and
        functions depending on their choices.
    """
    human.original_board()  # Resets the board back to the original state.
    computer.original_board()
    print(r"""
            ____ _  _ ___  ____ _  _ _  _ 
            [__  |  | |  \ |  | |_/  |  | 
            ___] |__| |__/ |__| | \_ |__| 
            """)
    print("----------------------- Main Menu -----------------------")
    print("The usual sudoku rules apply except the columns and rows start at 0 and end at 8.")
    while True:
        begin_game = input(
            "- Enter 'p' to play yourself.\n- Enter 's' to see the sudoku solved by the computer."
            "\n- Enter 'q' to exit.\n").lower()
        if begin_game == "p":
            human.human_play()
            carry_on = input(
                "If you'd like to play again, enter 'r'. Enter anything else to exit. ").lower()
            if carry_on == "r":
                # Calls start_game function to restart the game.
                start_game(human, computer)
            else:
                break
            break
        elif begin_game == "s":
            computer.computer_play()
            carry_on = input(
                "If you'd like to play again, enter 'r'. Enter anything else to exit. ").lower()
            if carry_on == "r":
                start_game(human, computer)
            else:
                break
            break
        elif begin_game == "q":
            break
        else:
            print("Please enter either 'p', 'c' or 'q'.")


if __name__ == '__main__':

    # Don't change the layout of the following sudoku examples
    sudoku1 = [
        [' ', '1', '5', '4', '7', ' ', '2', '6', '9'],
        [' ', '4', '2', '3', '5', '6', '7', ' ', '8'],
        [' ', '8', '6', ' ', ' ', ' ', ' ', '3', ' '],
        ['2', ' ', '3', '7', '8', ' ', ' ', ' ', ' '],
        [' ', ' ', '7', ' ', ' ', ' ', ' ', '9', ' '],
        ['4', ' ', ' ', ' ', '6', '1', ' ', ' ', '2'],
        ['6', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '4', ' ', ' ', ' ', '1', ' ', '7'],
        [' ', ' ', ' ', ' ', '3', '7', '9', '4', ' '],
    ]
    sudoku2 = [
        [' ', ' ', ' ', '3', ' ', ' ', ' ', '7', ' '],
        ['7', '3', '4', ' ', '8', ' ', '1', '6', '2'],
        ['2', ' ', ' ', ' ', ' ', ' ', ' ', '3', '8'],
        ['5', '6', '8', ' ', ' ', '4', ' ', '1', ' '],
        [' ', ' ', '2', '1', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '7', '8', ' ', ' ', '2', '5', '4'],
        [' ', '7', ' ', ' ', ' ', '2', '8', '9', ' '],
        [' ', '5', '1', '4', ' ', ' ', '7', '2', '6'],
        ['9', ' ', '6', ' ', ' ', ' ', ' ', '4', '5'],
    ]
    sudoku3 = [
        ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '3', '6', ' ', ' ', ' ', ' ', ' '],
        [' ', '7', ' ', ' ', '9', ' ', '2', ' ', ' '],
        [' ', '5', ' ', ' ', ' ', '7', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '4', '5', '7', ' ', ' '],
        [' ', ' ', ' ', '1', ' ', ' ', ' ', '3', ' '],
        [' ', ' ', '1', ' ', ' ', ' ', ' ', '6', '8'],
        [' ', ' ', '8', '5', ' ', ' ', ' ', '1', ' '],
        [' ', '9', ' ', ' ', ' ', ' ', '4', ' ', ' '],
    ]
    sudoku4 = [
        [' ', '4', '1', ' ', ' ', '8', ' ', ' ', ' '],
        ['3', ' ', '6', '2', '4', '9', ' ', '8', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '7', ' '],
        [' ', ' ', ' ', '4', '7', ' ', '2', '1', ' '],
        ['7', ' ', ' ', '3', ' ', ' ', '4', ' ', '6'],
        [' ', '2', ' ', ' ', ' ', ' ', ' ', '5', '3'],
        [' ', ' ', '7', ' ', '9', ' ', '5', ' ', ' '],
        [' ', ' ', '3', ' ', '2', ' ', ' ', ' ', ' '],
        [' ', '5', '4', ' ', '6', '3', ' ', ' ', ' '],
    ]

    # make sure 'option=2' is used in your submission
    option = 2

    if option == 1:
        sudoku = sudoku1
    elif option == 2:
        sudoku = sudoku2
    elif option == 3:
        sudoku = sudoku3
    elif option == 4:
        sudoku = sudoku4
    else:
        raise ValueError('Invalid choice!')

    human = HumanPlay()
    computer = ComputerPlay()

    start_game(human, computer)
