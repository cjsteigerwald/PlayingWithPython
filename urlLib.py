#!/usr/bin/python
#  
# read the data from the URL and print it
#
import urllib2

def main():
    # web address
    web_addy = "https://www.youtube.com/user/guru99com"

    # open a connection to a URL using urllib2
    webUrl = urllib2.urlopen(web_addy)

    print_result_code(webUrl)
    print_page_data(webUrl)

# prints response code
def print_result_code(webUrl):     
    #get the result code and print it
    print "result code: " + str(webUrl.getcode()) 
  
# read the data from the URL and print it
def print_page_data(webUrl):
    # read url into variable data and print
    data = webUrl.read()
    print data
 
if __name__ == "__main__":
  main()