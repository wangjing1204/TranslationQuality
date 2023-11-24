# coding = utf-8

import bibtexparser as bp
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
import csv

# with open('anthology+abstracts.bib','r',encoding='utf-8') as bibfile:
#     parser = BibTexParser()  # 声明解析器类
#     # parser.customization = convert_to_unicode  # 将BibTeX编码强制转换为UTF编码
#     bibdata = bp.load(bibfile, parser = parser)  # 通过bp.load()加载

import re,json

bib_list = []
with open('anthology+abstracts.bib', 'r', encoding='utf-8') as bibfile:
    bibdata = bibfile.read().strip().split('}\n')


for ref in bibdata:
    paper = re.sub('@.*proceedings\{','',ref)
    entry = {}
    info_list = paper.split(',\n')
    for info in info_list:
        info = info.strip()
        if info:
            if '=' not in info:
                entry['id'] = info
            else:
                info = info.split(' = ')
                k = info[0]
                v = info[1].replace('"','')
                if 'editor' in k or 'author' in k:
                    v = v.replace(',',' ')
                    v = re.sub('\s+and\n\s+','&',v)

                entry[k] = v
    print(entry)

    bib_list.append(entry)

with open('ACLbib.json','w',encoding='utf-8') as jf:
    json.dump(bib_list,jf,ensure_ascii=False,indent=4)

