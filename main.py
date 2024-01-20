def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    words = get_word_count(text)
    letters = get_letters_count(text)

    print_report(book_path, words, letters)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letters_count(text):
    letter_counts = {}
    lower_text = text.lower()

    for char in lower_text:
        if char.isalpha():
            
            letter_counts[char] = letter_counts.get(char, 0) + 1

    return letter_counts


def print_report(path, words, letters):
    print(f"--- Begin report of {path} ---")
    print(f"{words} Words found in the document")
    print("\n")

    sortedLetters = sorted(list(letters.items()), key=lambda x: x[1], reverse=True)

    for letter in sortedLetters:
       print(f"The '{letter[0]}' character was found {letter[1]} times")

    print("--- End report ---")


main()
