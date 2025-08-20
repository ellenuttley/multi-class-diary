from lib.music_library import *
from unittest.mock import Mock

def test_music_library_functional():
    music_library = MusicLibrary()
    assert(music_library)

def test_music_library_add_adds_track():
    music_library = MusicLibrary()
    track_mock = Mock()
    music_library.add(track_mock)
    assert track_mock in music_library.tracks

def test_music_library_search_returns_track_full_match():
    music_library = MusicLibrary()
    track_mock = Mock()
    track_mock.artist = 'My Chemical Romance'
    track_mock.title = 'Teenagers'
    music_library.add(track_mock)
    assert music_library.search('Teenagers') == [track_mock]

def test_music_library_search_returns_track_partial_match():
    music_library = MusicLibrary()
    track_mock = Mock()
    track_mock.artist = 'My Chemical Romance'
    track_mock.title = 'Teenagers'
    music_library.add(track_mock)
    assert music_library.search('chemical') == [track_mock]

# def test_music_library_():
#     music_library = MusicLibrary()

# def test_music_library_():
#     music_library = MusicLibrary()