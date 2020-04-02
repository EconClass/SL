
def read_text(_path):
    _file = open(_path, 'r').readlines()
    new_file = open('parsed.txt', 'w')

    for line in _file:
        l_line = line.split()
        new_file.write(f"{l_line[1]} {l_line[3]}\n")

    new_file.close()

if __name__ == "__main__":
    read_text('names.txt')
