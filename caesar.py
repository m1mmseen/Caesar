import sys


def main():
    args = sys.argv
    print(encode_text(args[1], int(args[2])))





print(encode_text("Das geht", 3))

if __name__ == '__main__':
    main()
