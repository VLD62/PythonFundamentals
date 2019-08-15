class Player:
    def __init__(self, name, result, score, games_count):
        self.name = name
        self.result = result
        self.score = score
        self.games_count = games_count

if __name__ == "__main__":
    players = []
    input_player = input().split(" -> ")

    while not input_player[0] == 'report':
        _name = input_player[0]
        _result = list(map(int,input_player[1].split(", ")))
        _score = sum(_result)
        _count = len(_result)

        new_player = Player(name = _name, result = _result, score = _score, games_count = _count  )
        players.append(new_player)
        input_player = input().split(" -> ")

    report = input()

    while not report == 'end':

        if report == 'score descending':
            for player in sorted(players, key=lambda x: (-x.score, x.name)):
                print(f'{player.name}: {player.score}')

        if report == 'score ascending':
            sorted_players = sorted(players,key=lambda x: (x.score, x.name))
            for player in sorted_players:
                print(f'{player.name}: {player.score}')

        if report == 'numberOfGames descending':
            for player in sorted(players,key=lambda x: (-x.games_count, x.name)):
                print(f'{player.name}: {player.games_count}')

        if report == 'numberOfGames ascending':
            for player in sorted(players,key=lambda x: (x.games_count, x.name)):
                print(f'{player.name}: {player.games_count}')

        report = input()
