- Install
$ pip install wikipedia

- Use in script
from wikipedia import page

wiki_page = page("Tango")
print(wiki_page.summary)

for link in wiki_page.links:
    print(link)