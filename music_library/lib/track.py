class Track:
    def __init__(self, artist, title):
        self.title = title.title()
        self.artist = artist.title()

    def matches(self, keyword):
        return keyword.title() == self.title or keyword.title() == self.artist
