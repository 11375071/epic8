class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0,0]
        self.ties = 0
        self.hp1 = 2500
        self.hp2 = 2500
        self.leveluppoint=40

    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def up(self, player):
        if player == 0:
            self.hp1 *= 1.01
        if player == 1:
            self.hp2 *= 1.01

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):

        return -3

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False