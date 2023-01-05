
def create_players_list():
    user_input = input('Enter player name, for exit enter "stop": ')
    list_of_players = []
    player_profile = {'player_name': '', 'player_age': 0, 'player_properties': ''}
    while user_input != 'stop':
        # user enter player name
        while not (user_input.islower() and not user_input.isdigit()):
            if not user_input.islower():
                print("The name you enter is not legal!!! please enter again a legal name.")
                user_input = input('Enter player name: ')
                continue
        player_profile['player_name'] = user_input
        # user enter player age
        while not user_input.isdigit():
            user_input = input('Enter player age here: ')
            if not user_input.isdigit():
                print("The age you enter is not legal!!! please enter again a legal age.")
                continue
        player_profile['player_age'] = int(user_input)
        # user enter player properties
        while not user_input.islower():
            user_input = input('Enter player properties here: ')
            if not user_input.islower():
                print("The properties you enter is not legal!!! please enter again a legal properties.")
                continue
        player_profile['player_properties'] = user_input
        # add the player profile to list of players
        list_of_players.append(player_profile)
        player_profile = {'player_name': '', 'player_age': 0, 'player_properties': ''}
        user_input = input('enter player name, for exit enter "stop": ')
    return list_of_players


def count_spoilt(tribe_list):
    spoilt_number = 0
    for player_profile in tribe_list:
        if 'spoilt' in player_profile['player_properties']:
            spoilt_number += 1
    return spoilt_number


def libolan_selection(player_profile, spoilt_number):
    if player_profile['player_age'] < 20:
        return False
    if not player_profile['player_name'].count('a') < 2:
        return False
    if ('spoilt' in player_profile['player_properties']) and (spoilt_number > 0):
        return False
    return True


def apolaki_selection(player_profile, spoilt_number):
    if player_profile['player_age'] < 20:
        return False
    if not player_profile['player_name'].count('a') > 1:
        return False
    if ('spoilt' in player_profile['player_properties']) and (spoilt_number > 0):
        return False
    return True


def print_tribe_players(tribe_list):
    for player in tribe_list:
        string = '%s : %s' % (player['player_name'], player['player_properties'])
        print(string)


def put_players_in_tribes():
    players_list = create_players_list()
    tribe_libolan = []
    tribe_apolaki = []
    for player in players_list:
        if apolaki_selection(player, count_spoilt(tribe_apolaki)):
            tribe_apolaki.append(player)
    for player in players_list:
        if libolan_selection(player, count_spoilt(tribe_libolan)):
            tribe_libolan.append(player)
    print('The players of libolan are:')
    print_tribe_players(tribe_libolan)
    print('The players of tribe apolaki are:')
    print_tribe_players(tribe_apolaki)


if __name__ == "__main__":
    put_players_in_tribes()
