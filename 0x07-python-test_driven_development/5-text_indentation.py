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
    result = ""
    i = 0
    length = len(text)

    while i < length:
        result += text[i]

        # Check if the current character is one of the specified characters
        if text[i] in ".?:":
            result += "\n\n"  # Add two new lines after the character
            # Skip any whitespace after the character
            while i + 1 < length and text[i + 1] == ' ':
                i += 1

        i += 1

    # Print the resulting text without leading or trailing spaces
    print(result.strip())
