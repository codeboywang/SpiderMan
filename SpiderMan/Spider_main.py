import url_manager , html_outputer , html_parser , html_downloader

class Spider_main(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print "craw %d:%s" % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 100:
                    break;
                count += 1
            except:
                print "crow failed"
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/python"
    obj_spider = Spider_main()
    obj_spider.craw(root_url)
