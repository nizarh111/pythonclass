def count_b_bob(text):

    pattern = r'b.*?Bob'
    matches = re.findall(pattern, text, re.IGNORECASE)

    return len(matches)

count_b_bob