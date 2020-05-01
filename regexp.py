import re

r1 = re.compile(r'\d')
r2 = re.compile("\\['data'\\]\\[\\d+\\]\\['created'\\]") 
r3 = re.compile("\\['data'\\]\\[\\d+\\]\\['y’\\]\\[\\d+\\]")
r4 = re.compile("data.+?chart.+?figure.+?data.+?\d+.+?y.+?\d+")

def search(r,e):
   if r.search(e): print(f'SEARCH: {e} matches {r}')
   else: print(f'SEARCH: {e} DOES NOT match {r}')

def match(r,e):
   if r.match(e): print(f'MATCH: {e} matches {r}')
   else: print(f'MATCH: {e} DOES NOT match {r}')


search(r1, '5abc')
match(r1, '5abc')
search(r1, 'x5abc')
match(r1, 'x5abc')
search(r2,"'data'][390]['type']")
search(r2,"['data'][391]['created']")
search(r2, "['data'][391]['id']")
search(r3, "['data']['chart']['figure']['data'][2]['y'][29]")
search(r4, "['data']['chart']['figure']['data'][2]['y'][29]")
search(r4, "['data']['chart']['figure']['data'][2]['x'][29]")
