from Utils.Writer import Writer

class AddableFriendsMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20199
        self.player = player

    def encode(self):
        self.writeVint(1)

        self.writeInt(1)                                # High Id
        self.writeInt(1)                      # Low Id
        self.writeVint(23)                    # trophies
        self.writeVint(0)
        self.writeVint(0)
        self.writeString("blah")
        self.writeVint(1)
        self.writeVint(28000000)
        self.writeVint(43000000)