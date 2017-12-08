MAJORS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
SOLFEGES = {'Do':0, 'Re':2, 'Mi':4, 'Fa':5, 'So':7, 'La':9, 'Ti':11}

def note(major, solfege):
    return MAJORS[(MAJORS.index(major) + SOLFEGES[solfege]) % 12]
