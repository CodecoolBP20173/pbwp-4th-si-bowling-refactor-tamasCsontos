ALL_PINS = 10
NORMAL_FRAMES = 10


def score(game):
    result = 0
    frame = 1
    first_ball_of_frame = True
    for i in range(len(game)):

        if is_spare(game[i]):
            result += ALL_PINS - last
        else:
            result += get_value(game[i])

        if frame < NORMAL_FRAMES and get_value(game[i]) == ALL_PINS:
            result += get_bonus(game, i)
            
        last = get_value(game[i])

        if not first_ball_of_frame:
            frame += 1
        
        first_ball_of_frame = not first_ball_of_frame

        if is_strike(game[i]):
            first_ball_of_frame = True
            frame += 1

    return result


def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif is_strike(char):
        return ALL_PINS
    elif is_spare(char):
        return ALL_PINS
    elif char == '-':
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
        bonus += get_value(game[ball_index+1])
    elif is_strike(game[ball_index]):
        bonus += get_value(game[ball_index+1])
        if is_spare(game[ball_index+2]):
            bonus += ALL_PINS - get_value(game[ball_index+1])
        else:
            bonus += get_value(game[ball_index+2])
    return bonus

