class HtmlOutputer(object):

    def __init__(self):
        self.data = []

    def collect_data(self,data):
        print 'in html_outputer def collect_data'
        if data is None:
            return
        self.data.append(data)

    def output_html(self):
        print 'in html_outputer def output_html'
        font = open('output.html','w')
        font.write('<html><meta charset="utf-8">')
        font.write('<body>')
        font.write('<table>')

        #ASCII
        for data in self.data:
            font.write("<tr>")
            font.write("<td>%s</td>" % data['url'])
            font.write("<td>%s</td>" % data['title'].encode('utf-8'))
            font.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            font.write("</tr>")

        font.write('</table>')
        font.write('</body>')
        font.write('</html>')

        font2 = open('output2.md', 'w')
        font2.write('# 100 pices of Baidu Baike\n')

        # ASCII
        for data in self.data:
            font2.write("# %s\n" % data['title'].encode('utf-8'))
            font2.write("**[%s](%s)**\n" % (data['url'],data['url']))
            font2.write(">%s\n" % data['summary'].encode('utf-8'))
            font2.write("* * *\n")
