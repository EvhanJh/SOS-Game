""" SOS """

import math
import pygame
from pygame.locals import *
import sos_algorithms
import sos_gui


def sos():
    """
    Game Function
    """
    board = 0
    number = 8
    players_count = 2
    player = 0
    scores = [0] * players_count
    artificial_intelligence = 0
    lines = []
    cases = []
    page = 0

    width = 1280
    height = 720

    pygame.init()

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('SOS')

    in_progress = True

    while in_progress:

        # Variables
        colors = [(15, 165, 50), (255, 165, 0), (200, 0, 255), (0, 130, 130), (40, 210, 0),
                  (255, 200, 0), (220, 60, 80), (110, 0, 105), (50, 175, 215), (0, 0, 0)]

        font_link = './fonts/Roboto/Roboto-Regular.ttf'
        font_jungle = './fonts/Jungle.otf'
        font_big = pygame.font.Font(font_jungle, 200)
        font_title = pygame.font.Font(font_link, 25)
        font = pygame.font.Font(font_link, 19)

        # Close Window
        for event in pygame.event.get():

            if event.type == QUIT:
                in_progress = False
                exit(0)

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                # Home Window
                if page == 0:

                    # Rules Button
                    if 50 < pos[0] < 50 + 148 and 120 < pos[1] < 120 + 53:
                        page = 1

                    # Solo Button
                    elif 50 < pos[0] < 50 + 148 and 220 < pos[1] < 220 + 53:
                        artificial_intelligence = 1
                        players_count = 2
                        scores = [0] * players_count
                        board = 0
                        player = 0
                        lines = []
                        cases = []
                        page = 2

                    # Multi Button
                    elif 50 < pos[0] < 50 + 148 and 320 < pos[1] < 320 + 53:
                        artificial_intelligence = 0
                        board = 0
                        player = 0
                        lines = []
                        cases = []
                        page = 2

                    # Last Game Button
                    elif 50 < pos[0] < 50 + 148 and 420 < pos[1] < 420 + 53:
                        data = sos_algorithms.load_save()
                        number = data['number']
                        players_count = data['players_count']
                        player = data['player']
                        artificial_intelligence = data['artificial_intelligence']
                        scores = data['scores']
                        board = data['board']
                        lines = data['lines']
                        page = 4

                # Rules Window
                elif page == 1:

                    # Solo Button
                    if 50 < pos[0] < 50 + 148 and 220 < pos[1] < 220 + 53:
                        artificial_intelligence = 1
                        players_count = 2
                        scores = [0] * players_count
                        board = 0
                        player = 0
                        lines = []
                        cases = []
                        page = 2

                    # Multi Button
                    elif 50 < pos[0] < 50 + 148 and 320 < pos[1] < 320 + 53:
                        artificial_intelligence = 0
                        board = 0
                        player = 0
                        lines = []
                        cases = []
                        page = 2

                    # Last Game Button
                    elif 50 < pos[0] < 50 + 148 and 420 < pos[1] < 420 + 53:
                        data = sos_algorithms.load_save()
                        number = data['number']
                        players_count = data['players_count']
                        player = data['player']
                        artificial_intelligence = data['artificial_intelligence']
                        scores = data['scores']
                        board = data['board']
                        lines = data['lines']
                        page = 4

                    # Back Button
                    elif 50 < pos[0] < 50 + 148 and 520 < pos[1] < 520 + 53:
                        page = 0

                # Select Board Length
                elif page == 2:

                    # Rules Button
                    if 50 < pos[0] < 50 + 148 and 120 < pos[1] < 120 + 53:
                        page = 1

                    # Last Game Button
                    elif 50 < pos[0] < 50 + 148 and 420 < pos[1] < 420 + 53:
                        data = sos_algorithms.load_save()
                        number = data['number']
                        players_count = data['players_count']
                        player = data['player']
                        artificial_intelligence = data['artificial_intelligence']
                        scores = data['scores']
                        board = data['board']
                        lines = data['lines']
                        page = 4

                    # Back Button
                    elif 50 < pos[0] < 50 + 148 and 520 < pos[1] < 520 + 53:
                        page = 0

                    # Board Length Buttons
                    if 365 < pos[0] < 365 + 148 and 250 < pos[1] < 250 + 53:
                        number = 3
                    elif 565 < pos[0] < 565 + 148 and 250 < pos[1] < 250 + 53:
                        number = 4
                    elif 765 < pos[0] < 765 + 148 and 250 < pos[1] < 250 + 53:
                        number = 5
                    elif 365 < pos[0] < 365 + 148 and 350 < pos[1] < 350 + 53:
                        number = 6
                    elif 565 < pos[0] < 565 + 148 and 350 < pos[1] < 350 + 53:
                        number = 7
                    elif 765 < pos[0] < 765 + 148 and 350 < pos[1] < 350 + 53:
                        number = 8
                    elif 365 < pos[0] < 365 + 148 and 450 < pos[1] < 450 + 53:
                        number = 9
                    elif 565 < pos[0] < 565 + 148 and 450 < pos[1] < 450 + 53:
                        number = 10
                    elif 765 < pos[0] < 765 + 148 and 450 < pos[1] < 450 + 53:
                        number = 11

                    # Check if click is in "Select length button"
                    if 365 < pos[0] < 365 + 148 and 250 < pos[1] < 250 + 53 or \
                            565 < pos[0] < 565 + 148 and 250 < pos[1] < 250 + 53 or \
                            765 < pos[0] < 765 + 148 and 250 < pos[1] < 250 + 53 or \
                            365 < pos[0] < 365 + 148 and 350 < pos[1] < 350 + 53 or \
                            565 < pos[0] < 565 + 148 and 350 < pos[1] < 350 + 53 or \
                            765 < pos[0] < 765 + 148 and 350 < pos[1] < 350 + 53 or \
                            365 < pos[0] < 365 + 148 and 450 < pos[1] < 450 + 53 or \
                            565 < pos[0] < 565 + 148 and 450 < pos[1] < 450 + 53 or \
                            765 < pos[0] < 765 + 148 and 450 < pos[1] < 450 + 53:
                                board = sos_algorithms.new_board(number)
                                if not artificial_intelligence:
                                    page = 3
                                else:
                                    page = 4

                # Select Players Count
                elif page == 3:

                    # Rules Button
                    if 50 < pos[0] < 50 + 148 and 120 < pos[1] < 120 + 53:
                        page = 1

                    # Multi Button
                    elif 50 < pos[0] < 50 + 148 and 220 < pos[1] < 220 + 53:
                        artificial_intelligence = 0
                        board = 0
                        player = 0
                        lines = []
                        cases = []
                        page = 2

                    # Last Game Button
                    elif 50 < pos[0] < 50 + 148 and 420 < pos[1] < 420 + 53:
                        data = sos_algorithms.load_save()
                        number = data['number']
                        players_count = data['players_count']
                        player = data['player']
                        artificial_intelligence = data['artificial_intelligence']
                        scores = data['scores']
                        board = data['board']
                        lines = data['lines']
                        page = 4

                    # Back Button
                    elif 50 < pos[0] < 50 + 148 and 520 < pos[1] < 520 + 53:
                        page = 0

                    # Players Count Button
                    if 365 < pos[0] < 365 + 148 and 250 < pos[1] < 250 + 53:
                        players_count = 2
                    elif 565 < pos[0] < 565 + 148 and 250 < pos[1] < 250 + 53:
                        players_count = 3
                    elif 765 < pos[0] < 765 + 148 and 250 < pos[1] < 250 + 53:
                        players_count = 4
                    elif 365 < pos[0] < 365 + 148 and 350 < pos[1] < 350 + 53:
                        players_count = 5
                    elif 565 < pos[0] < 565 + 148 and 350 < pos[1] < 350 + 53:
                        players_count = 6
                    elif 765 < pos[0] < 765 + 148 and 350 < pos[1] < 350 + 53:
                        players_count = 7
                    elif 365 < pos[0] < 365 + 148 and 450 < pos[1] < 450 + 53:
                        players_count = 8
                    elif 565 < pos[0] < 565 + 148 and 450 < pos[1] < 450 + 53:
                        players_count = 9
                    elif 765 < pos[0] < 765 + 148 and 450 < pos[1] < 450 + 53:
                        players_count = 10

                    # Check if click is in "Select players count button"
                    if 365 < pos[0] < 365 + 148 and 250 < pos[1] < 250 + 53 or \
                            565 < pos[0] < 565 + 148 and 250 < pos[1] < 250 + 53 or \
                            765 < pos[0] < 765 + 148 and 250 < pos[1] < 250 + 53 or \
                            365 < pos[0] < 365 + 148 and 350 < pos[1] < 350 + 53 or \
                            565 < pos[0] < 565 + 148 and 350 < pos[1] < 350 + 53 or \
                            765 < pos[0] < 765 + 148 and 350 < pos[1] < 350 + 53 or \
                            365 < pos[0] < 365 + 148 and 450 < pos[1] < 450 + 53 or \
                            565 < pos[0] < 565 + 148 and 450 < pos[1] < 450 + 53 or \
                            765 < pos[0] < 765 + 148 and 450 < pos[1] < 450 + 53:
                        scores = [0] * players_count
                        page = 4

                # Game Window
                elif page == 4:

                    if 50 < pos[0] < 50 + 148 and 120 < pos[1] < 120 + 53:
                        page = 1

                    elif 50 < pos[0] < 50 + 148 and 520 < pos[1] < 520 + 53:
                        page = 0

                    for case in cases:
                        if case[0] < pos[0] < case[0] + 41 and case[1] < pos[1] < case[1] + 41:
                            i = math.floor(cases.index(case) / number)
                            j = cases.index(case) % number
                            if not sos_algorithms.has_letter(board, i, j):
                                if event.button == 1:
                                    sos_algorithms.update(board, number, i, j, 1, scores,
                                                          player, lines, players_count)
                                else:
                                    sos_algorithms.update(board, number, i, j, 2, scores,
                                                          player, lines, players_count)
                                player += 1
                                if artificial_intelligence \
                                        and player == 1 \
                                        and not sos_algorithms.has_winner(board, number):
                                    sos_algorithms.random_ai(board, number, scores,
                                                             player, lines, players_count)
                                    player += 1
                                if player >= players_count:
                                    player = 0
                                sos_algorithms.create_save(board, number, scores, player, lines,
                                                           players_count - 1, artificial_intelligence)

        # Global Actions
        window.fill((255, 255, 255))

        # Home Window
        if page == 0:

            sos_title = font_big.render('S O S', False, (60, 140, 230))
            window.blit(sos_title, (window.get_width() / 2 - sos_title.get_width() / 2,
                                    window.get_height() / 2 - sos_title.get_height() / 2))

            rules = pygame.image.load('./images/rules.png')
            window.blit(rules, (50, 120))

            solo = pygame.image.load('./images/solo.png')
            window.blit(solo, (50, 220))

            multiplayers = pygame.image.load('./images/multiplayer.png')
            window.blit(multiplayers, (50, 320))

            last_game = pygame.image.load('./images/last_game.png')
            window.blit(last_game, (50, 420))

            back_none = pygame.image.load('./images/back_none.png')
            window.blit(back_none, (50, 520))

            sos_gui.draw_menu(pygame, window)

        # Rules Window
        if page == 1:

            rules_none = pygame.image.load('./images/rules_none.png')
            window.blit(rules_none, (50, 120))

            rules_page = pygame.image.load('./images/rules_page.png')
            window.blit(rules_page, (300, 180))

            solo = pygame.image.load('./images/solo.png')
            window.blit(solo, (50, 220))

            multiplayers = pygame.image.load('./images/multiplayer.png')
            window.blit(multiplayers, (50, 320))

            last_game = pygame.image.load('./images/last_game.png')
            window.blit(last_game, (50, 420))

            back = pygame.image.load('./images/back.png')
            window.blit(back, (50, 520))

            sos_gui.draw_menu(pygame, window)

            rules_title = pygame.image.load('./images/rules_title.png')
            window.blit(rules_title, (window.get_width() / 2 - rules_title.get_width() / 2, 20))

        # Select Board Length
        if page == 2:

            rules = pygame.image.load('./images/rules.png')
            window.blit(rules, (50, 120))

            solo_none = pygame.image.load('./images/solo_none.png')
            window.blit(solo_none, (50, 220))

            multiplayers = pygame.image.load('./images/multiplayer_none.png')
            window.blit(multiplayers, (50, 320))

            last_game = pygame.image.load('./images/last_game.png')
            window.blit(last_game, (50, 420))

            back = pygame.image.load('./images/back.png')
            window.blit(back, (50, 520))

            sos_gui.draw_menu(pygame, window)

            case_title = pygame.image.load('./images/case_title.png')
            window.blit(case_title, (window.get_width() / 2 - case_title.get_width() / 2, 20))

            board_3 = pygame.image.load('./images/board_3.png')
            window.blit(board_3, (365, 250))
            board_4 = pygame.image.load('./images/board_4.png')
            window.blit(board_4, (565, 250))
            board_5 = pygame.image.load('./images/board_5.png')
            window.blit(board_5, (765, 250))
            board_6 = pygame.image.load('./images/board_6.png')
            window.blit(board_6, (365, 350))
            board_7 = pygame.image.load('./images/board_7.png')
            window.blit(board_7, (565, 350))
            board_8 = pygame.image.load('./images/board_8.png')
            window.blit(board_8, (765, 350))
            board_9 = pygame.image.load('./images/board_9.png')
            window.blit(board_9, (365, 450))
            board_10 = pygame.image.load('./images/board_10.png')
            window.blit(board_10, (565, 450))
            board_11 = pygame.image.load('./images/board_11.png')
            window.blit(board_11, (765, 450))

        # Select Players Count
        if page == 3:

            rules = pygame.image.load('./images/rules.png')
            window.blit(rules, (50, 120))

            solo = pygame.image.load('./images/solo_none.png')
            window.blit(solo, (50, 220))

            multiplayers_none = pygame.image.load('./images/multiplayer_none.png')
            window.blit(multiplayers_none, (50, 320))

            last_game = pygame.image.load('./images/last_game.png')
            window.blit(last_game, (50, 420))

            back = pygame.image.load('./images/back.png')
            window.blit(back, (50, 520))

            sos_gui.draw_menu(pygame, window)

            player_title = pygame.image.load('./images/player_title.png')
            window.blit(player_title, (window.get_width() / 2 - player_title.get_width() / 2, 20))

            players_2 = pygame.image.load('./images/players_2.png')
            window.blit(players_2, (365, 250))
            players_3 = pygame.image.load('./images/players_3.png')
            window.blit(players_3, (565, 250))
            players_4 = pygame.image.load('./images/players_4.png')
            window.blit(players_4, (765, 250))
            players_5 = pygame.image.load('./images/players_5.png')
            window.blit(players_5, (365, 350))
            players_6 = pygame.image.load('./images/players_6.png')
            window.blit(players_6, (565, 350))
            players_7 = pygame.image.load('./images/players_7.png')
            window.blit(players_7, (765, 350))
            players_8 = pygame.image.load('./images/players_8.png')
            window.blit(players_8, (365, 450))
            players_9 = pygame.image.load('./images/players_9.png')
            window.blit(players_9, (565, 450))
            players_10 = pygame.image.load('./images/players_10.png')
            window.blit(players_10, (765, 450))

        # Game Window
        if page == 4:

            rules = pygame.image.load('./images/rules.png')
            window.blit(rules, (50, 120))

            solo_none = pygame.image.load('./images/solo_none.png')
            window.blit(solo_none, (50, 220))

            multiplayers_none = pygame.image.load('./images/multiplayer_none.png')
            window.blit(multiplayers_none, (50, 320))

            last_game_none = pygame.image.load('./images/last_game_none.png')
            window.blit(last_game_none, (50, 420))

            back = pygame.image.load('./images/back.png')
            window.blit(back, (50, 520))

            sos_title = pygame.image.load('./images/sos_title.png')
            window.blit(sos_title, (window.get_width() / 2 - sos_title.get_width() / 2, 20))

            sos_gui.draw_menu(pygame, window)
            sos_gui.draw_score(pygame, window)

            sos_gui.draw_board(window, board, number, cases, pygame)
            sos_gui.draw_lines(window, number, lines, colors, pygame)

            if sos_algorithms.has_winner(board, number):
                winner = sos_gui.display_winner(scores, players_count)
                if winner == 0:
                    end_game = font.render('Égalité', False, (255, 0, 0))
                else:
                    if artificial_intelligence:
                        if winner == 1:
                            end_game = font.render('Gagnant » Joueur', False, colors[winner - 1])
                        else:
                            end_game = font.render('Gagnant » Ordinateur', False, colors[winner - 1])
                    else:
                        end_game = font.render('Gagnant » Joueur ' +
                                               str(winner), False, colors[winner - 1])
                window.blit(end_game, (window.get_width() / 2 - end_game.get_width() / 2, 70))

            if artificial_intelligence and player == 0:
                turn_text = font.render('Tour » Joueur', False, colors[player])
            else:
                turn_text = font.render('Tour » Joueur ' + str(player + 1), False, colors[player])

            window.blit(turn_text, (window.get_width() / 2 - turn_text.get_width() / 2, 640))

            sos_gui.display_score(window, scores, colors, artificial_intelligence, pygame)

        pygame.display.update()

    pygame.quit()


sos()
