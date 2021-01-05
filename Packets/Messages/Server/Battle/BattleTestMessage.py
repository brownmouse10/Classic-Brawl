from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class BattleTestMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20559
        self.player = player

    def encode(self):
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(1)

        self.writeInt(0)
        self.writeInt(self.player.LowID)
        
        self.writeString("Bot")

        self.writeVint(1)
        self.writeVint(1)
        
        self.writeVint(30)

        self.writeHexa('''84 80 10 01''')

        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(0)

        self.writeHexa('''E9 6D F5 02''')

        self.writeVint(1)
        self.writeVint(1)

        self.writeVint(0)
        self.writeVint(15)
        self.writeVint(10)