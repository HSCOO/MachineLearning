import urllib

def read_text():
    quotes = open("/Users/apple/OnlyStu/MachineLearning/函数/text.rtf")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    url = 'http://www.wdylike.appspot.com/?q=' + 'shit'
    print url
    connection = urllib.urlopen(url)
    output = connection.read()
    print output
    connection.close()

read_text()