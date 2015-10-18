import urllib2
import operator
from HTMLParser import HTMLParser

class HTMLTagCounter(HTMLParser):
    tags = {}
    
    def handle_starttag(self, tag, attrs):
        if tag not in self.tags:
            self.tags[tag] = 1
        else:
            self.tags[tag] = self.tags[tag] + 1

    def get_html_source(self,URL):
        request = urllib2.Request(URL, headers={'User-Agent' : "Browser"}) 
        page = urllib2.urlopen(request)
        return page.read()

    def sort_tags(self):
        return sorted(self.tags.items(), key=operator.itemgetter(1), reverse=True)

    def top_five(self):
        sorted_tags = self.sort_tags()
        print "the 5 most used tags are:"
        for i in range(0,5):
            print sorted_tags[i]
    
    def total_number_of_elements(self):
        return len(self.tags)

if __name__ == "__main__":
    counter = HTMLTagCounter()
    source = counter.get_html_source("http://ordergroove.com/company")
    counter.feed(source)
    print "The page has a total number of " + str(counter.total_number_of_elements()) + " elements"
    counter.top_five()

