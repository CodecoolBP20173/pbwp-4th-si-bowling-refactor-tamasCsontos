ALL_PINS = 10
NORMAL_FRAMES = 10


def score(game):
    result = 0
    frame = 1
    first_ball_of_frame = True
    for i in range(len(game)):

        result += get_value(game, i)

        if frame < NORMAL_FRAMES and (is_spare(game[i]) or is_strike(game[i])):
            result += get_bonus(game, i)

        if not first_ball_of_frame:
            frame += 1
        
        first_ball_of_frame = not first_ball_of_frame

        if is_strike(game[i]):
            first_ball_of_frame = True
            frame += 1

    return result


def get_value(game, ball_index):
    ball = game[ball_index]
    if ball == '1' or ball == '2' or ball == '3' or \
       ball == '4' or ball == '5' or ball == '6' or \
       ball == '7' or ball == '8' or ball == '9':
        return int(ball)
    elif is_strike(ball):
        return ALL_PINS
    elif is_spare(ball):
        return ALL_PINS - get_value(game, ball_index - 1)
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
        bonus += get_value(game, ball_index+1)
    elif is_strike(game[ball_index]):
        bonus += get_value(game, ball_index+1)
        bonus += get_value(game, ball_index+2)
    return bonus

