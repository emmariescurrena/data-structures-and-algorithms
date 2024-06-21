# pylint: disable=bare-except
# pylint: disable=invalid-name
# pyright: reportMissingModuleSource=false

"""Modules..."""


def palindrome(word):
    """Verify if word is a palindrome"""

    if len(word) in [0, 1]:
        return "is"
    elif word[0] == word[-1]:
        return palindrome(word[1:-1])
    else:
        return "isn't"


def main():
    """Ask word"""

    word = input("Insert word to verify if it is a palindrome: ")
    print(f"'{word}' {palindrome(word)} a palindrome")
    quit()


main()
