import json
import wikipediaapi

articles = open('articles.txt', encoding='utf-8').read().splitlines()
bad_section_titles = set(open('bad_section_titles.txt', encoding='utf-8').read().splitlines())
langs = open('langs.txt', encoding='utf-8').read().splitlines()
res = {lang:([-100] * len(articles)) for lang in langs}
wiki = wikipediaapi.Wikipedia('en')

def parse_sections(p):
    res = ''
    for s in p.sections:
        if s.title not in bad_section_titles:
            res += s.title + '\n' + s.text + '\n' + parse_sections(s)
    return res

def parse_page(p):
    return len(parse_sections(p))
    
for ind, article in enumerate(articles):
    page = wiki.page(article)
    langlinks = page.langlinks
    langlinks['en'] = page
    article_info = []
    for l in langs:
        if l in langlinks:
            res[l][ind] = parse_page(langlinks[l])
    print(ind + 1, '/', len(articles))


out = open("wikiData.txt", "w", encoding='utf-8')
for key, value in res.items():
    out.write(key + ' ' + ' '.join([str(i) for i in value]) + '\n')
out.close()
