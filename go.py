def go():
    print("Enter a set of notes in lower case separated by spaces & I'll tell you if they are a ø")
    print("E.g. D# Ds Cb a bb g#")
    print("")
    while True:
        check_chord()

def check_chord():
    line = input() 
    input_notes = line.split()
    for chord in _half_diminished_chords:
        is_half_dim = True        
        for note in chord:
            if not is_half_dim:
                continue
            if not does_x_contain_y(input_notes, note):
                is_half_dim = False
        if is_half_dim:
            print("YES - " + ' '.join(chord) + " is half diminished")
            print()
            return
    print('No, not half dimished')
    print()

def does_x_contain_y(input_notes, note):
    for input_note in input_notes:
        if normalise(input_note) == normalise(note):
            return True
    return False

def normalise(note):
    result = note.upper()
    if result == 'A#': result = 'Bb'
    if result == 'B#': result = 'C'
    if result == 'C#': result = 'Db'
    if result == 'D#': result = 'Eb'
    if result == 'E#': result = 'F'
    if result == 'F#': result = 'Gb'
    if result == 'G#': result = 'Ab'
    if result == 'AS': result = 'Bb'
    if result == 'BS': result = 'C'
    if result == 'CS': result = 'Db'
    if result == 'DS': result = 'Eb'
    if result == 'ES': result = 'F'
    if result == 'FS': result = 'Gb'
    if result == 'GS': result = 'Ab'
    if result == 'CB': result = 'B'
    if result == 'FB': result = 'E'
    result = result.upper()
    return result

_half_diminished_chords = [
    ['A','C','Eb','G'],
    ['Bb','Db','E','Ab'],
    ['B','D','F','A'],
    ['C','Eb','Gb','Bb'],
    ['Db','E','G','B'],
    ['D','F','Ab','C'],
    ['Eb','Gb','A','Db'],
    ['E','G','Bb','D'],
    ['F','Ab','B','Eb'],
    ['Gb','A','C','E'],
    ['G','Bb','Db','F'],
    ['Ab','B','D','Gb'],
]
go()    