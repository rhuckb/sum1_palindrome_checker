from main import is_palindrome

def test_simple_palindrome():
    assert is_palindrome("toot") is True

def test_simple_non_palindrome():
    assert is_palindrome("hello") is False

def test_palindrome_with_spaces():
    assert is_palindrome("too hot to hoot") is True

def test_palindrome_capital():
    assert is_palindrome("Toot") is True

def test_empty_string():
    assert is_palindrome("") is True

def test_non_palindrome_with_spaces_punctuation():
    assert is_palindrome("Tooty toot toot!") is False     