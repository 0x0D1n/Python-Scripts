import sys

#Create dictionary of chars
dictionary_chars = " -!-\"-#-$-%-&-\'-(-)-*-+-,-/-:-;-<-=->-?-@-[-\-]-^-`-{-|-}"
clean_chars = dictionary_chars.split("-")

#Create dictionary of URL encoded chars
dictionary_url = "%20,%21,%22,%23,%24,%25,%26,%27,%28,%29,%2A,%2B,%2C,%2F,%3A,%3B,%3C,%3D,%3E,%3F,%40,%5B,%5C,%5D,%5E,%60,%7B,%7C,%7D"
clean_url = dictionary_url.split(",")


#Decode given URL encoded string
def decode(string_to_decode):
    decoded_string = ""
    i = 0
    while i < len(string_to_decode):
        if string_to_decode[i] == "%":
            new_string = string_to_decode[i:i+3]
            if new_string in clean_url:
                new_index = clean_url.index(new_string)
                decoded_string += clean_chars[new_index]
                i += 3
        else:
            decoded_string += string_to_decode[i]
            i += 1
    return decoded_string

#URL encode given string
def encode(string_to_encode):
    encoded_string = ""
    for key, value in enumerate(string_to_encode):
        if value in clean_chars:
            new_index = clean_chars.index(value)
            encoded_string += clean_url[new_index]
        else:
            encoded_string += value
    return encoded_string


def main():
    
    if len(sys.argv) != 3:
        print("[+] Usage : url -d (decode) | -e (encode) \"string\" [+]")
        print("[+] Don't forget \"\" for the encoding part          [+]")
        exit()
     
    if sys.argv[1] == "-d":
        print(decode(sys.argv[2]))
    elif sys.argv[1] == "-e":
        print(encode(sys.argv[2]))
    else:
        print("[+] Only -d and -e options are allowed [+]")
    

main()
