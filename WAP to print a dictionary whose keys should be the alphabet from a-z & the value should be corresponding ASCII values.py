# WAP to print a dictionary whose keys should be the alphabet from a-z and the values should be corresponding ASCII values.
ascii_dict = {chr(i): ord(chr(i)) for i in range(97,123)}
print(ascii_dict)