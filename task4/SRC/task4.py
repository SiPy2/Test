import sys

if __name__ == "__main__":
    string1 = sys.argv[1]
    string2 = sys.argv[2]

    for j in range(len(string2)):
        try:
            if string2[j]=='*':
                print('OK')
                break
            elif string1[j]==string2[j]: pass
            if j == len(string2) - 1 and len(string1) == len(string2): print('OK')
            else:
                print('KO')
                break
        except:
            print('KO')