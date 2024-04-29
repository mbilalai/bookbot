def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

# def main():
#   book_path = "books/frankenstein.txt"
#   text = get_book_text(book_path)
#   num_words = get_num_words(text)
#   letters_dict = letter_count(text)
#   sorted_letter_list = sorted_letters_list(letters_dict)
#   print("--- Begin report of {book_path} ---")
#   print(f"{num_words} words found in the document")
#   print()

#   #for item in chars_sorted_list:

#   print(f"{letters_dict} letters found int the document")

# def get_num_words(text):
#   words = text.split()
#   return(len(words))

# def sort_on(dict):
#   return dict['num']

# # def sorted_letters_list(num_letters_dict):
#   sorted_list = []
#   for l in num_letters_dict:
#     sorted_list.append({"letter": l, "num": num_letters_dict})
#   sorted_list.sort(reverse=True, key=sort_on)
#   return sorted_list

# def letter_count(text):
#   letters = {}
#   for l in text:
#     lowered = l.lower()
#     if lowered in letters:
#       letters[lowered] += 1
#     else:
#       letters[lowered] = 1
#   return letters

# #def sort_on(dict):


# def get_book_text(path):
#   with open(path) as f:
#     return f.read()

# main()