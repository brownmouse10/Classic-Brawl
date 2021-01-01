from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage

from Utils.Reader import BSMessageReader


class OnPlay(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        pass

    def process(self):
        OutOfSyncMessage(self.client, self.player, "Multiplayer Isn't Sync Yet").send()
        