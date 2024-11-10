def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniform comparison
    s = s.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return s == s[::-1]
