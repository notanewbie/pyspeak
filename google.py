from GetURL import *
import re;
File = returnURL("https://www.google.com/search?safe=active&hl=en&source=hp&ei=2rQfXaj9Kaqb_Qa8uaj4CA&q=Apple&oq=Apple&gs_l=psy-ab.3...1299.1881..1994...0.0..0.0.0.......0....1..gws-wiz.....0.").replace(">", ">\n")
Results = File.split('<h3 class="r">');
i = 0;
while i < len(Results):
    a = i + 1;
    print "Search result " + str(a) + ":\n" + Results[i]
    #URLs are between "/url?q=" and "&amp;sa=U&amp;"
    #Dscriptions are between "<span class="st">" and "</span>"
    i = i + 1;
#print re.search('<h3 class="r">;(.*)</h3>',File);
