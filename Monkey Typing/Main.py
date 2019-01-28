def count_words(text: str, words: set) -> int:
    count = 0
    counted = []
    words = tuple(words)
    for substr in text.split():
        for word in words:
            if word in substr.lower() and word not in counted:
                count += 1
                counted.append(word)
    print(count)
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")