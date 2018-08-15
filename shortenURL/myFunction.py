from shortenURL.db import get_db


# take this code in different file
random_number = 1234123412
url_characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-_'
charecter_length = len(url_characters)


def get_length_of_DB():
    db = get_db()
    counter = db.execute('select count(*) as c from entries').fetchone()['c']
    return counter


# here the encoding occurs
def encode_url(index):
    temp = random_number + index
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
        if url_list[i] not in url_characters:
            return -1
        url_index += ((charecter_length ** i) * url_characters.find(url_list[i]))

    idx = url_index - random_number
    totalURL = get_length_of_DB()
    if idx > totalURL or idx < 1:
        return -1

    return idx


def find_shorten_url_index(url):
    db = get_db()

    id = db.execute('select id from entries where url=?',(url,)).fetchone()
    if id is None:
        db.execute('insert into entries (url) values (?)', (url,))
        db.commit()
        id = get_length_of_DB()
    else:
        id = id['id']

    return id


def find_original_url(url_index):
    db = get_db()

    original_url = db.execute('select url from entries where id=?',(url_index,)).fetchone()['url']

    return original_url

# take this code in different file
# end of the code
