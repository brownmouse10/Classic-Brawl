from Utils.Writer import Writer

class FriendListMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20105
        self.player = player

    def encode(self):
        self.writeVint(0)
        self.writeVint(0)

        self.writeInt(0) # HighID
        self.writeInt(323426908) # LowID
        
        self.writeString("Gaby")
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)