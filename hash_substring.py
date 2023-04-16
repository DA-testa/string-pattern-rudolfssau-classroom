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


def get_occurrences(paterna, teksts, q, w):
    paradibas = []
    lenTeksts = len(teksts)
    lenPaterna = len(paterna)
    a = pow(q, lenPaterna - 1) % w
    b = t = 0
    for i in range(lenPaterna):
        b = (q * b + ord(paterna[i])) % w
        t = (q * t + ord(teksts[i])) % w
    for s in range(lenTeksts - lenPaterna + 1):
        if b == t:
            match = True
            for i in range(lenPaterna):
                if paterna[i] != teksts[s + i]:
                    match = False
                    break
            if match:
                paradibas.append(s)
        if s < lenTeksts - lenPaterna:
            t = (t - a * ord(teksts[s])) % w
            t = (t * q + ord(teksts[s + lenPaterna])) % w
            t = (t + w) % w
    return paradibas

if __name__ == "__main__":
    q, w = 256, 13
    paterna, teksts = read_input()
    paradibas = get_occurrences(paterna, teksts, q, w)
    print_occurrences(paradibas)
