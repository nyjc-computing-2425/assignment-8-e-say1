# Built-in imports

def reverse(text):
    """
    Takes in a string and returns the reversed string

    Parameters
    ----------
    text: str
         The string that you want to reverse
         
    """
    if len(text) == 0:
        return ""
        
    else:
        first_char = text[0]
        return reverse(text[1:]) + first_char
        
        
def is_palindrome(string):
    """
    Checks if the given string is a palindrome or not and returns True if it is but False if it's not

    Parameters
    ----------
    string: str
        The string you want to run the palindrome check on
    
    """
    if len(string) <= 1:
        return True
        
    else:
        if string[0] != string[-1]:
            return False
        else:
            return is_palindrome(string[1:-1])


    
    