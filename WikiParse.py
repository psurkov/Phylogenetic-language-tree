import json
import wikipediaapi

def parse_page(w):
    return len(w.text)

articles = open('articles.txt', encoding='utf-8').read().splitlines()
langs = open('langs.txt', encoding='utf-8').read().splitlines()
wiki = wikipediaapi.Wikipedia('en')
res = {}
for ind, article in enumerate(articles):
    page = wiki.page(article)
    langlinks = page.langlinks
    langlinks['en'] = page
    info_for_title = []
    for l in langs:
        if l in langlinks:
            info_for_title.append(parse_page(langlinks[l]))
        else:
            print("Not found", article, l)
    res[article] = info_for_title
    print(ind + 1, '/', len(articles))


out = open("wikiData.json", "w", encoding='utf-8')
out.write(json.dumps({'langs' : langs, 'data' : res}))
out.close()
