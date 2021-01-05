from Utils.Writer import Writer
from Database.DatabaseManager import DataBase
import random

class TeamGameroomDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player
        self.playerCount = 2

    def encode(self):
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        if (self.player.roomID == 0):
            self.player.roomID = random.randint(0, 2147483647)
            self.writeInt(self.player.roomID)
            DataBase.replaceValue(self, 'roomID', self.player.roomID)

        else:
           self.writeInt(self.player.roomID)

        self.writeVint(1557129593)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeScId(15, self.player.mapID)               # MapID

        for i in range(1, self.playerCount + 1):
            # Player
            self.writeVint(self.playerCount)                    # Player count


            self.writeVint(1)                               # Gameroom owner boolean
            self.writeInt(self.player.HighID)               # HighID
            self.writeInt(self.player.LowID)                # LowID

            self.writeScId(16, self.player.brawlerID)           # BrawlerID

            self.writeVint(0)                                   #
            self.writeVint(0)                                   # Unknown
            self.writeVint(0)                                   # Unknown
            self.writeVint(0)                                   #

            self.writeVint(3)                                  # Player State | 11: Events, 10: Brawlers, 9: Writing..., 8: Training, 7: Spectactor, 6: Offline, 5: End Combat Screen, 4: Searching, 3: Not Ready, 2: AFK, 1: In Combat, 0: OffLine
            self.writeBoolean(False)                            # Is ready
            self.writeBoolean(False)                            # Team | 0: Blue, 1: Red

            self.writeVint(0)
            self.writeVint(0)

            self.writeString(self.player.name)                  # Player name
            self.writeVint(100)
            self.writeVint(28000000 + self.player.profileIcon)  # Player icon
            self.writeVint(43000000 + self.player.namecolor)    # Player name color

            if self.player.useGadget == 1:
                self.writeScId(23, self.player.starpower)       # Starpower
                self.writeScId(23, self.player.gadget)          # Gadget
            else:
                self.writeScId(23, self.player.starpower)       # Starpower
                self.writeScId(0, 0)                            # Gadget

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(6)
