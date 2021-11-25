def pri_ext():
    file = input('file: ')
    ext = ''
    pos = 0
    if '.' in file:
        for x, y in enumerate(file):
            if y == '.':
                pos = x + 1
    else:
        print('no es un archivo')
        ext = None

    while pos < len(file):
        if ext != None:
            ext += file[pos]
            pos += 1
        else:
            break
    return ext

pri_ext()