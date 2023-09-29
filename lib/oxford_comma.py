def oxford_comma(items):
    if (len(items) < 2):
        return "".join(items)
    if (len(items) == 2):
        return " and ".join(items)
    last_word = items.pop(-1)
    return (f'{", ".join(items)}, and {last_word}')
