#coding:utf-8
import xml.etree.ElementTree as etree
tree = etree.parse('music.xml')
root = tree.getroot()

el = root.findall('dict')[0].findall('dict')[0].findall('dict') 

for e in el:
    dic = {}
    for k,v in zip (e[::2],e[1::2]):
        dic[k.text] = v.text

    if 'Skip Count' in dic and 'Play Count' in dic:
        if int(dic['Play Count']) - int(dic['Skip Count']) < 0:
            print int(dic['Play Count']), int(dic['Skip Count']), dic['Name'].encode('utf-8').strip()
        
