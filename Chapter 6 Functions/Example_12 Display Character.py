print(ord('1'), ord('Z'))
def displayCharacter(ch1, ch2, perline):
    count = 0
    i = ord(ch1)
    while i <= ord(ch2):
        print(chr(i), end='')
        i += 1
        count += 1
        if count % perline == 0:
            print()

displayCharacter('1', 'Z', 10)