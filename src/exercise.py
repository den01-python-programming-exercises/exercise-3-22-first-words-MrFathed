def main():
    #write your code below this line
    while True:
        line = input()

        if line == '':
            break

        words = line.split()
        print(words[0])

if __name__ == '__main__':
    main()
