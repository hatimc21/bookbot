import sys
from stats import get_num_words, get_char_freq, sort_char_freq

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Retrieve the book file path from command-line arguments
    book_path = sys.argv[1]

    # Read the book text
    book_text = get_book_text(book_path)

    # Analyze the book text
    num_words = get_num_words(book_text)
    char_freq = get_char_freq(book_text)
    sorted_char_freq = sort_char_freq(char_freq)

    # Display the analysis results
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...\n")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words\n")
    print("--------- Character Count -------")
    for char, count in sorted_char_freq:
        print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
