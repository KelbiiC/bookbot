def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print(total_word_count(file_contents))

def total_word_count(text):
    return len(text.split())

main()