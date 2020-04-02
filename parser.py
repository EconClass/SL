if __name__ == "__main__":
    text = open('hi.txt')
    for line in text:
        broken = line.split()
        parsed = open('parsed.txt', 'w')
        parsed.write(" ".join((broken[1], broken[3]))
        # parsed.close()
