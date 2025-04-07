def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_freq(text):
    text = text.lower() 
    char_freq = {}

    for char in text:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    return char_freq

def sort_char_freq(char_freq_dict):
    sorted_char_freq = sorted(char_freq_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_char_freq
