""" This module contains the controller of the player."""
import utility as utls
import models.player as m_player


class PlayerController:
    """ Class of the controller player.

    Set the inputs to create a player and store the user answers in the model player variables.

    """
    def __init__(self):
        self.utils = utls.Utils()

        self.last_name = None
        self.first_name = None
        self.birthdate = None
        self.rank = None

        self.m_player = None

    def get_player_info(self):
        """ Get the answers of the user.

        Set the input of the last_name, first_name, birthdate and rank of a player and calls
        the ModelPlayer class to store the user answers.

        """

        self.m_player = m_player.Player(self.last_name, self.first_name, self.birthdate,
                                        self.rank)
