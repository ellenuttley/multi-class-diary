from lib.music_library import *
from lib.track import *
from unittest.mock import Mock

'''
Add multiple tracks to music library
'''
def test_integration_add_tracks_to_music_library():
    music_library = MusicLibrary()
    track_1 = Track('Sum 41', 'Fat Lip')
    track_2 = Track('Jimmy Eat World', 'Sweetness')
    track_3 = Track('Linkin Park', 'In The End')

    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)

    assert music_library.tracks ==[track_1, track_2, track_3]

'''
Add tracks to music library
Search music library for a track
'''
def test_integration_add_tracks_then_search():
    music_library = MusicLibrary()
    track_1 = Track('Lamb of God', 'Redneck')
    track_2 = Track('KoRn', 'Freak on a Leash')
    track_3 = Track('My Hero', 'Foo Fighters')

    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)

    assert music_library.search('my hero') == [track_3]

'''
Add tracks to music library
Search music library for a track it doesnt have
'''