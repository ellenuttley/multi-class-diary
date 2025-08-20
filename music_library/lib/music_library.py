class MusicLibrary:
    def __init__(self):
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)

    def search(self, keyword):
        return [track for track in self.tracks if track.matches(keyword)]

