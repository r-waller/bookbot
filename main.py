def main():
    """Main function"""
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    text = get_book_text(book_path)
    print(f"{get_word_count(text)} found in the document.\n")
    print(get_alpha_count(count_characters(text)))
    print("--- End report ---")

def get_book_text(path):
    """Return the text of the book"""
    with open(path) as f:
        return f.read()


def get_word_count(text):
    """Return word count""" 
    return len(text.split())


def count_characters(text):
    """Count the characters in the text""" 
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if char in char_count:
            char_count[char] +=  1  
        else:
            char_count[char] = 1  
    return char_count


def get_alpha_count(dict: dict[str, int]):
    """Return the count of each letter in the text."""
    return "\n".join(
        map(
            lambda x: f"The '{x[0]}' character was found {x[1]} times.",
            filter(
                lambda x: x[0].isalpha(), 
                sorted(
                    dict.items(),
                    key=lambda x: x[1],
                    reverse=True
                )
            )
        )
    )


if __name__ == "__main__":
    main()

