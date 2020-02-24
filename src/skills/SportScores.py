from sportsreference.ncaab.schedule import Schedule as NCAAB_Sched


def load_api():
    return (main, ['ku', 'score'])


def print_game(team, game):
    print("%s --- %s - %s vs %s - %s" %
          (game.result, team, game.points_for, game.opponent_name, game.points_against,))


def get_last_game(team):
    schedule = NCAAB_Sched(team)
    sched_df = schedule.dataframe
    last_index = sched_df.index.values.nonzero()[0].tolist()[-1]
    game = sched_df.iloc[last_index, :]

    return game


def main(state, request_tokens):
    print_game("Kansas", get_last_game('Kansas'))
    return("WIN")
