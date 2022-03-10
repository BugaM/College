def is_palindrome(s):
    """Function that recognizes if the string s is a palindrome"""
    reverse = s[::-1]
    if s == reverse:
        return True
    else:
        return False


if __name__ == '__main__':  # main funtion for testing
    print(is_palindrome('arara'))
