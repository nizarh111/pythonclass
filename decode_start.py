alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"


def decode_message(file_path):
    # Define a function to count vowels in a string
    def count_vowels(s):
        return sum(c in 'aeiouAEIOU' for c in s)

    # Mapping from vowels count to letter
    vowels_to_letter = {0: ' ', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

    decoded_message = ""

    # Open the file and read line by line
    with open(file_path, 'r') as file:
        for line in file:
            vowels_count = count_vowels(line)
            if vowels_count in vowels_to_letter:
                decoded_message += vowels_to_letter[vowels_count]
            else:
                decoded_message += '?' # In case the number of vowels exceeds the mapping

    return decoded_message

# Assuming 'secret.txt' is in the current directory
file_path = 'secret.txt'
message = decode_message(file_path)
print("Decoded message:", message)
