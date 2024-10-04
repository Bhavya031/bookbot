def words(string):
    return len(string.split())


def duplicate(string):
    track = {}
    for index, i in enumerate(string):
        i = i.lower()
        if i in track:
            track[i] += 1
        else:
            track[i] = 1
    return track


def report(string):
    print(f"""--- Begin report of books/frankenstein.txt ---
{words(string)} words found in the document \n""")
    dis = duplicate(string)
    sort = dict(sorted(dis.items(), key=lambda iteam: iteam[1], reverse=True))
    for i in sort:
        if i.isalpha():
            print(f"The '{i}' character was found {dis[i]} times")
    print("--- End report ---")


def main():
    with open('books/frankenstein.txt') as f:
        string = f.read()
        report(string)


if __name__ == '__main__':
    main()
