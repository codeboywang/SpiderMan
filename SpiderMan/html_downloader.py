import urllib2


class HtmlDownLoader(object):

    def download(self,url):
        print "in html_downloader"
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode == 200:
            return None
        else:
            return response.read()