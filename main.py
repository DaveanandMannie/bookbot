def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    word_count = get_word_count(text)
    print(f'=============Report=================')
    print(f'Target {text}')
    print(f'{word_count} words in the text')
    count_dict = char_count(text)
    sorted_load = report_load(count_dict)
    for item in sorted_load:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print('==================End==================')
def get_word_count(text):
    return len(text.split())


def get_book(path):
    with open(path) as book:
        return book.read()


def char_count(text):
    char_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def sort_on(old_dict):
    return old_dict['num']


def report_load(dictionary):
    report_list = []
    for key in dictionary:
        if key.isalpha():
            temp = {
                'char': key,
                'num': dictionary[key]
            }
            report_list.append(temp)
    report_list.sort(reverse=True, key=sort_on)
    return report_list


main()
