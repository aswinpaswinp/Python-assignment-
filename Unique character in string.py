def has_unique_characters(input_string):
    # Create a set to track characters we've seen
    seen_characters = set()

    # Iterate through each character in the string
    for char in input_string:
        # If the character is already in the set, return False (not unique)
        if char in seen_characters:
            return False
        # Otherwise, add the character to the set
        seen_characters.add(char)

    # If no duplicate characters were found, return True
    return True

# Get user input
input_string = input("Enter a string: ")

# Check for uniqueness and display result
if has_unique_characters(input_string):
    print("The string has all unique characters.")
else:
    print("The string does not have all unique characters.")
