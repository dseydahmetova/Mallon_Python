

def main():
    userInput = input("Enter your input: ")
    # ------------Writing file-----------
    f = open('myPythonFile', 'a')
    if userInput == "end":
        f.write(f"\n {userInput}")
        f.close()
        f = open('myPythonFile', 'r')
        print('-----------Reading file------------')
        try:
            i = 0
            for line in f:
                print(i, ":", line, end='')
                i = i + 1
        finally:
            f.close()



if __name__ == '__main__':
    main()

