from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Database.DatabaseManager import DataBase

from Utils.Reader import BSMessageReader


class TeamUseGadgetMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.useGadget = self.read_Vint()
        self.boolean = self.read_Vint()
        DataBase.replaceGameroomValue(self, 'useGadget', self.boolean, "room") 
        self.boolean = self.read_Vint()
        print(self.boolean)
        DataBase.replaceGameroomValue(self, 'useGadget', self.boolean, "room")

    def process(self):
        TeamGameroomDataMessage(self.client, self.player).send()