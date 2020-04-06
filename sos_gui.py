""" Interface """


def draw_board(window, board, number, cases, pygame):
    """
    Draw the board
    :param window: Pygame window
    :type window: pygame.blit
    :param board: Board
    :type board: list
    :param number: Number of lines / columns
    :type number: int
    :param cases: Cases of board
    :type cases: list
    :param pygame: Pygame
    :type pygame: pygame
    """

    for line in range(0, number):
        for item in range(0, number):
            if board[line][item] == 0:
                case = pygame.image.load('./images/case.png')
            elif board[line][item] == 1:
                case = pygame.image.load('./images/caseS.png')
            else:
                case = pygame.image.load('./images/caseO.png')
            case_width = case.get_size()[0] - 1
            width = pygame.display.get_surface().get_size()[0]
            height = pygame.display.get_surface().get_size()[1]
            window.blit(case, ((width / 2 - (case_width * number) / 2) + case_width * item,
                               (height / 2 - (case_width * number) / 2) + case_width * line))
            cases.append([((width / 2 - (case_width * number) / 2) + case_width * item),
                          ((height / 2 - (case_width * number) / 2) + case_width * line)])


def display_score(window, scores, colors, artificial_intelligence, pygame):
    """
    Display players scores
    :param window: Pygame window
    :type window: pygame.blit
    :param scores: Scores of players
    :type scores: list
    :param colors: Colors
    :type colors: list
    :param artificial_intelligence: Computer
    :type artificial_intelligence: int
    :param pygame: Pygame
    :type pygame: pygame
    """
    for index, score in enumerate(scores):
        font = pygame.font.Font('./fonts/Roboto/Roboto-Light.ttf', 19)
        color = colors[index] if len(colors) > index else (0, 0, 0)
        score_text = ''
        if artificial_intelligence:
            if index == 0:
                score_text = font.render('Joueur' +
                                         ' » ' + str(score) + ' points', False, color)
            elif index == 1:
                score_text = font.render('Ordinateur' +
                                         ' » ' + str(score) + ' points', False, color)
        else:
            score_text = font.render('Joueur ' + str(index + 1) +
                                     ' » ' + str(score) + ' points', False, color)

        window.blit(score_text, (1070, 150 + index * 30))


def draw_lines(window, number, lines, colors, pygame):
    """
    Draw lines for SOS's
    :param window: Pygame window
    :type window: pygame.blit
    :param number: Extreme coordinates of lines
    :type number: int
    :param lines: Extreme coordinates of lines
    :type lines: list
    :param colors: Colors
    :type colors: list
    :param pygame: Pygame
    :type pygame: pygame
    """
    if lines:
        for line in lines:

            case_width = 39

            left = (pygame.display.get_surface().get_size()[0] / 2 -
                    (case_width * number) / 2) - number

            top = (pygame.display.get_surface().get_size()[1] / 2 -
                   (case_width * number) / 2) - number

            pygame.draw.line(window, colors[line[2]],
                             (left + (case_width / 2) +
                              (case_width * line[0][1] + int(line[0][1]) * 2),

                              top + (case_width / 2) +
                              (case_width * line[0][0]) + int(line[0][0]) * 2),

                             (left + (case_width / 2) +
                              (case_width * line[1][1] + int(line[1][1]) * 2),

                              top + (case_width / 2) +
                              (case_width * line[1][0]) + int(line[1][0]) * 2), 2)


def display_winner(scores, players_count):
    """
    Display the winner
    :param scores: Player's scores
    :type scores: list
    :param players_count: Players' count
    :type players_count: int
    :return: bool
    """
    winner = max(scores)
    egality = 0
    for i in range(0, players_count):
        if scores[i] == winner:
            egality += 1
    if egality > 1:
        return 0
    return scores.index(winner) + 1


def draw_menu(pygame, window):
    pygame.draw.line(window, (187, 187, 187), (250, 40), (250, 660))


def draw_score(pygame, window):
    pygame.draw.line(window, (187, 187, 187), (1030, 40), (1030, 660))
