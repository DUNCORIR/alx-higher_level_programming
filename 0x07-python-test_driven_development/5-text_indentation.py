def text_indentation(text):
    """
    Prints text with two new lines after each of these characters: ., ? and :

    Parameters:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty result string
    special_chars = ".?:"
    i = 0
    while i < len(text):
        # Print the current character
        print(text[i], end="")

        # Check if the current character is one of the specified characters
        if text[i] in special_chars:
            print("\n")
            i += 1
            # Skip any whitespace after the character
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
