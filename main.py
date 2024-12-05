def main():
    """Main function"""
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(f"There are {get_word_count(text)} words in the book.")
    print(count_characters(text))
    

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


if __name__ == "__main__":
    main()

