import re,json

bib_list = []
with open('anthology+abstracts.bib', 'r', encoding='utf-8') as bibfile:
    bibdata = bibfile.read().strip()

bibdata = re.sub('}\n','}\n\n',bibdata)


reflist = bibdata.split('\n\n')

TQ_biblist = []
HTQ_biblist = []
HT_biblist = []
TQ_H_biblist = []

for ref in reflist:
    if re.search('[Hh]uman [Tt]ranslation [Qq]uality',ref):
        HTQ_biblist.append(ref)


    if re.search('[Tt]ranslation [Qq]uality',ref):
        TQ_biblist.append(ref)

    if re.search('[Hh]uman [Tt]ranslation',ref):
        HT_biblist.append(ref)

    if re.search('[Tt]ranslation [Qq]uality',ref) and re.search('[Hh]uman',ref):
        TQ_H_biblist.append(ref)
print(len(TQ_biblist))
print(len(HTQ_biblist))
print(len(HT_biblist))
print(len(TQ_H_biblist))

with open('acl_TQ_abstract.bib','w',encoding='utf-8') as bf:
    bf.write('\n'.join(TQ_biblist))

with open('acl_TQ&h_abstract.bib','w',encoding='utf-8') as bf:
    bf.write('\n'.join(TQ_H_biblist))

with open('acl_HT_abstract.bib','w',encoding='utf-8') as bf:
    bf.write('\n'.join(HT_biblist))

with open('acl_HTQ_abstract.bib','w',encoding='utf-8') as bf:
    bf.write('\n'.join(HTQ_biblist))