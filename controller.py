import model


class Controller(object):
    def __init__(self):
        self.albums_list = []

    def register_album(self, inputs: dict):
        model.register_album(self.albums_list, inputs)

    def search_album(self, search_option: int):
        return model.search_album(self.albums_list, search_option)

    def search_music(self, search_option: int):
        return model.search_music(self.albums_list, search_option)

    def generate_playlist(self):
        return model.generate_playlist(self.albums_list)
