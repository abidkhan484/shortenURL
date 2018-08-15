random_number = 1234123412
url_characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-_'
charecter_length = len(url_characters)


# here the encoding occurs
def encode_url(iden):
    temp = random_number + iden
    url_list = []
    while temp:
        pos = temp % charecter_length
        url_list.append(url_characters[pos])
        temp //= charecter_length
    url = ''.join(url_list)

    return url

# here i want to decode
def decode_url(url):
    url_list = list(url)
    url_index = 0
    for i in range(len(url_list)):
        url_index += ((charecter_length ** i) * url_characters.find(url_list[i]))

    return url_index
