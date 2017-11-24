ALL_PINS = 10
NORMAL_FRAMES = 10


def score(game):
    result = 0
    frame = 1
    first_ball_of_frame = True
    for i in range(len(game)):

        result += get_pins_knocked_down(game, i)

        if frame < NORMAL_FRAMES:
            result += get_bonus(game, i)

        if first_ball_of_frame and not is_strike(game[i]):
            first_ball_of_frame = False
        else:
            first_ball_of_frame = True
            frame += 1

    return result


def get_pins_knocked_down(game, ball_index):
    ball = game[ball_index]
    if ball.isdigit():
        return int(ball)
    elif is_strike(ball):
        return ALL_PINS
    elif is_spare(ball):
        return ALL_PINS - get_pins_knocked_down(game, ball_index - 1)
    elif ball == '-':
        return 0
    else:
        raise ValueError()


def is_strike(ball):
    return ball == 'X' or ball == 'x'


def is_spare(ball):
    return ball == '/'


def get_bonus(game, ball_index):
    bonus = 0
    if is_spare(game[ball_index]):
        bonus += get_pins_knocked_down(game, ball_index+1)
    elif is_strike(game[ball_index]):
        bonus += get_pins_knocked_down(game, ball_index+1)
        bonus += get_pins_knocked_down(game, ball_index+2)
    return bonus

