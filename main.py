from stats import count_words, count_chars, sorted_counts

def get_book_text(fpath):
    with open(fpath) as f:
        txt = f.read()
    return txt

def print_report(fpath):
    txt = get_book_text(fpath)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {fpath}')
    print('----------- Word Count ----------')
    print(f'Found {count_words(txt)} total words')
    print('--------- Character Count -------')
    cc = count_chars(txt)
    for d in sorted_counts(cc):
        if d['char'].isalpha():
            print(f"{d['char']}: {d['count']}")
    print('============= END ===============')

def main():
    import sys
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        print_report(sys.argv[1])

main()


