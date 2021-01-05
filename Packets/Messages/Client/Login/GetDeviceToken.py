from Utils.Reader import BSMessageReader


class GetDeviceToken(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)

    def decode(self):
        self.Password = self.read_string()
        print(self.Password)
    def process(self):
        pass