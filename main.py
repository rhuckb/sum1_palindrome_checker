def is_palindrome(text):
    cleared_text = "".join(char.lower() for char in text if char.isalnum())
    return cleared_text == cleared_text[::-1]