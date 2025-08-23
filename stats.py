def get_num_words(text):
    words = text.split()
    return len(words)

def count_each_character(text):
    text = text.lower()
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        if ch.isalpha():
            sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

# def sort_data(char_count):
#     unsorted_dict ={}
#     for char in char_count:
#         if char.isalpha():
#             unsorted_dict[char] = char_count[char]
#     sorted_dict = unsorted_dict.sort(key=lambda x: x[0])
#     return unsorted_dict