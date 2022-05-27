def translate(text):
    pl = 'ĄąĆćĘęŁłŃńÓóŚśŹźŻż'
    ascii_pl = 'AaCcEeLlNnOoSsZzZz'
    mapping = str.maketrans(pl, ascii_pl)
    return text.translate(mapping)


