#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    # Get all names defined in the hidden_4 module using dir()
    names = dir(hidden_4)

    # Filter names that don't start with "__" and sort them alphabetically
    filtered_names = sorted(
            name for name in names
            if not name.startswith("__")
    )

    # Print each name on a new line
    for name in filtered_names:
        print(name)
