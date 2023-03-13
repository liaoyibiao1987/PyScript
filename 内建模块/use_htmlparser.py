from html.parser import HTMLParser
from html.entities import name2codepoint
import requests

class UserHtmlParser(HTMLParser):
    """description of class"""

    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []

    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for each in attrlist:
                if attrname == each[0]:
                    return each[1]
            return None

        if tag == 'li' and _attr(attrs, 'data-title'):
            movie = {}
            movie['actors'] = _attr(attrs, 'data-actors')
            movie['director'] = _attr(attrs, 'data-director')
            movie['duration'] = _attr(attrs, 'data-dutation')
            movie['title'] = _attr(attrs, 'data-title')
            movie['rate'] = _attr(attrs, 'data-rate')
            self.movies.append(movie)
    
    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)
    #覆盖handle_data方法,用来处理获取的html数据,这里保存在data数组
    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

def movieparser(url):
    #headers = {}
    req = requests.get(url)
    s = req.text
    myparser = UserHtmlParser()
    myparser.feed(s)
    myparser.close()
    return myparser.movies
#parser = UserHtmlParser()
#parser.feed('''<html>
#<head></head>
#<body>
#<!-- test html parser -->
#    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
#</body></html>''')

if __name__ == '__main__':
    url = 'https://movie.douban.com/'
    movies = movieparser(url)
    for each in movies:
        print('%(title)s|%(rate)s|%(actors)s|%(director)s|%(duration)s' % each)

