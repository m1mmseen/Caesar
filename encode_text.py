def encode_text(text, key):
    new_string = ""
    encode = True
    if key < 0:
        encode = False
        key = key * -1
    for i in text:
        d = ord(i)
        if i.isupper():
            if encode:
                if d in range(65, 65 + (26 - key)):
                    new_string += chr(d + key)
                else:
                    new_string += chr(d - 26 + 3)
            else:
                if d in range(65, 65 + key):
                    new_string += chr(d + 26 - key);
                else:
                    new_string += chr(d - key)
        elif i.islower():
            if encode:
                if d in range(97, 97 + (26 - key)):
                    new_string += chr(d + key)
                else:
                    new_string += chr(d - 26 + 3)
            else:
                if d in range(97, 97 + key):
                    new_string += chr(d + 26 - key);
                else:
                    new_string += chr(d - key)
        else:
            new_string += i
    return new_string

