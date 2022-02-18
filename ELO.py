# This module defines the function that updates players'
# ELOs based on who won. For an explanation of the formulas
# and intermediary functions (ie the 'expected score' functions), see
# the wiki section below:
# https://en.wikipedia.org/wiki/Elo_rating_system#Mathematical_details


def expectedscorewhite(white, black):
    """
    Calculates the expected score for the white player, which is
    the probability of white winning.
    :param white: white's ELO
    :param black: black's ELO
    :return: a float between 0 and 1.
    """
    D = 1 + 10**((black-white)/400.0)
    E = 1.0/D
    return E


def expectedscoreblack(white, black):
    """
    Calculates the expected score for the black player, which is
    the probability of black winning.
    :param white: white's ELO
    :param black: black's ELO
    :return: a float between 0 and 1.
    """
    return expectedscorewhite(white=black, black=white)


def update(whiterating, blackrating, winner):
    EW = expectedscorewhite(whiterating, blackrating)
    EB = expectedscoreblack(whiterating, blackrating)
    K = 40.0
    if winner == 'white':
        S = 0.5
    elif winner == 'black':
        S = -0.5
    else:
        S = 0.0
    updatewhite = whiterating + K*(S + 0.5 - EW)
    updateblack = blackrating + K*(- (S - 0.5) - EB)
    return updatewhite, updateblack





