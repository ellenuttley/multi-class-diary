from lib.track import *

def test_track_functional():
    track = Track('Slipknot', 'Duality')
    assert(track)

def test_track_title_case():
    track = Track('green day', 'warning')
    assert track.artist == 'Green Day'
    assert track.title == 'Warning'

def test_track_matches_artist():
    track = Track('Limp Bizkit', 'Break Stuff')
    assert track.matches('limp bizkit') == True

def test_track_matches_title():
    track = Track('Paramore', 'Misery Business')
    assert track.matches('misery business') == True

def test_track_matches_title_false_no_match():
    track = Track('Fall Out Boy', 'Dance, Dance')
    assert track.matches('dance') == False

# def test_track_():
#     track = Track()
