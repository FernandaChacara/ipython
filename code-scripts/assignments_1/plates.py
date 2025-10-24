def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# Rule 2: length between 2 and 6
def length_valid(s):
    return 2 <= len(s) <= 6


# Rule 1: must start with at least 2 letters
def starts_with_two_letters(s):
    return s[0].isalpha() and s[1].isalpha()


# Rule 5: no punctuation, spaces, or dots
def alphanumeric_only(s):
    return s.isalnum()


# Rule 3 + 4: numbers at the end, not starting with 0
def numbers_valid(s):
    found_number = False
    for char in s:
        if char.isdigit():
            if not found_number:
                if char == "0":   # first digit cannot be zero
                    return False
                found_number = True
        else:
            if found_number:
                return False      # letter after number -> invalid
    return True


def is_valid(s):
    return (
        length_valid(s)
        and starts_with_two_letters(s)
        and alphanumeric_only(s)
        and numbers_valid(s)
    )


main()

