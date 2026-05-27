from stats import get_num_words, char_count, dict_sorted
import sys
def get_book_text(path):
    with open(path) as f:
        return f.read()
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def main():
    path = sys.argv[1]
    a = get_book_text(path)
    ttl_words = get_num_words(a)
    bad_dict = char_count(a)
    good_list = dict_sorted(bad_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {ttl_words} total words")
    print("--------- Character Count -------")
    for item in good_list:
        if item["char"].isalpha():
            char, count = item["char"], item["num"]
            print(f"{char}: {count}")
    print("============= END ===============")

main()


