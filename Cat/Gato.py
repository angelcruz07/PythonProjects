import PySimpleGUI as sg

PLAYER_ONE = "X"
PLAYER_TWO = "O"


def print_board():
    button_size = (7, 3)

    deck = [0, 0, 0,
            0, 0, 0,
            0, 0, 0]
    layout = [
        [
            sg.Button("", key="0", size=button_size),
            sg.Button("", key="1", size=button_size),
            sg.Button("", key="2", size=button_size)
        ],
        [
            sg.Button("", key="3", size=button_size),
            sg.Button("", key="4", size=button_size),
            sg.Button("", key="5", size=button_size)
        ],
        [
            sg.Button("", key="6", size=button_size),
            sg.Button("", key="7", size=button_size),
            sg.Button("", key="8", size=button_size)
        ],
        [sg.Button("Salir", key="ok"),
         sg.Button("Reiniciar", key="reset")
         ]
    ]

    return deck, layout


def reset_game(window, deck):
    for i in range(9):
        window[str(i)].update(text="")
    deck = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    return deck


def winner_plays():
    possible_plays = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    return possible_plays


def main_bucle(layout, deck, possible_plays):
    current_player = PLAYER_ONE
    window = sg.Window("Gato", layout)
    end_game = False

    while True:
        event, value = window.read()

        if event == sg.WIN_CLOSED or event == "ok":
            break

        if window.Element(event).ButtonText == "" and not end_game:
            index = int(event)
            deck[index] = current_player
            window.Element(event).Update(text=current_player)

            for possible_play in possible_plays:
                if deck[possible_play[0]] == deck[possible_play[1]] == deck[possible_play[2]] != 0:
                    if deck[possible_play[0]] == PLAYER_ONE:
                        sg.popup("El jugador 1 ha ganado")
                        end_game = True
                        break
                    else:
                        sg.popup("El jugador 2 ha ganado !!")
                        end_game = True
                        break

            if 0 not in deck:
                sg.popup("Juego empatado")
                end_game = True

            if not end_game:
                current_player = PLAYER_TWO if current_player == PLAYER_ONE else PLAYER_ONE
        elif event == "reset":
            deck = reset_game(window, deck)
            current_player = PLAYER_ONE
            end_game = False


def main():
    deck, layout = print_board()
    possible_plays = winner_plays()
    main_bucle(layout, deck, possible_plays)


if __name__ == "__main__":
    main()
