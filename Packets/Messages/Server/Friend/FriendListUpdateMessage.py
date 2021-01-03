from Utils.Writer import Writer

class FriendListUpdateMessage(Writer):

    def __init__(self, client, player, friendLowID):
        super().__init__(client)
        self.id = 20106
        self.player = player
        self.friendID = friendLowID

    def encode(self):
        self.writeInt(0) # HighID
        self.writeInt(323426908) # LowID