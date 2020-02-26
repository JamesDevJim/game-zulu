class QuitGame(Exception):
    """Custom exception class to signal that the game must be quit"""

    pass


class ChangeGame(Exception):
    def __init__(self, message="", *, new_game):
        super().__init__(message)
        self.new_game = new_game
