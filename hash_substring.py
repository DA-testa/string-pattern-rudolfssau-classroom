# python 3

def read_input():
    ievade = input().strip()
    if "I" in ievade:
        paterna= input().strip()
        teksts = input().strip()
    else:
        with open("tests/06") as file:
            paterna = file.readline().strip()
            teksts = file.readline().strip()
    return (paterna, teksts)

def print_occurrences(izvade):
    print(" ".join(map(str, izvade)))

def get_occurrences(paterna, teksts):
    paradibas = []
    if len(paterna) > len(teksts):
        return paradibas
    pat_hash = hash(paterna)
    teksta_h = [hash(teksts[i:i + len(paterna)]) for i in range(len(teksts) - len(paterna) + 1)]
    for i in range(len(teksta_h)):
        if pat_hash == teksta_h[i] and teksts[i:i + len(paterna)] == paterna:
            paradibas.append(i)
    return paradibas

if __name__ == "__main__":
    paterna, teksts = read_input()
    paradibas = get_occurrences(paterna, teksts)
    print_occurrences(paradibas)
