def count_words(txt):
    wc = len(txt.split())
    return wc


def count_chars(txt):
    char_count = dict()
    for ch in txt:
        ch = ch.lower()
        char_count[ch] = char_count.get(ch, 0) + 1
    return char_count

def sorted_counts(dcounts):
    lst = [{'char':k, 'count':v} for k, v in dcounts.items()]
    lst.sort(key=lambda item: item['count'], reverse=True)
    return lst
