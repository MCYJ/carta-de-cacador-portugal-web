from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import json
import xml.etree.ElementTree as ET

ROOT=Path('dist')
ORIGIN='https://mcyj.github.io/carta-de-cacador-portugal-web/'
BASE='/carta-de-cacador-portugal-web/'

class Page(HTMLParser):
 def __init__(self,html):
  super().__init__();self.links=[];self.metas=[];self.h1=0;self.refs=[];self.lang='';self.jsonld=[];self.capture=False;self.buffer='';self.feed(html)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang','')
  if tag=='link':self.links.append(a)
  if tag=='meta':self.metas.append(a)
  if tag=='h1':self.h1+=1
  for key in ['href','src']:
   if key in a:self.refs.append(a[key])
  if tag=='script' and a.get('type')=='application/ld+json':self.capture=True;self.buffer=''
 def handle_data(self,data):
  if self.capture:self.buffer+=data
 def handle_endtag(self,tag):
  if tag=='script' and self.capture:self.jsonld.append(json.loads(self.buffer));self.capture=False

urls=[n.text for n in ET.parse(ROOT/'sitemap.xml').getroot().findall('{*}url/{*}loc')]
assert len(urls)==18
pages={}
for url in urls:
 path=url.removeprefix(ORIGIN);file=ROOT/path/'index.html';html=file.read_text();page=Page(html);pages[url]=page
 assert page.h1==1,url
 assert [l['href'] for l in page.links if l.get('rel')=='canonical']==[url],url
 assert any(m.get('name')=='description' and m.get('content') for m in page.metas),url
 assert not any(m.get('name')=='robots' and 'noindex' in m.get('content','') for m in page.metas),url
 assert all(token not in html for token in ['WAITING_FOR_REVIEW','120</strong>','Em análise','Under review','PreOrder','entitlement']),url
 for ref in page.refs:
  if ref.startswith(BASE):
   target=ref.split('#')[0].removeprefix(BASE);assert (ROOT/target/('index.html' if target.endswith('/') or not target else '')).exists(),(url,ref)
for url,page in pages.items():
 alternates=[l for l in page.links if l.get('rel')=='alternate'];assert any(l.get('hreflang')==page.lang and l.get('href')==url for l in alternates),url
 assert len([l for l in alternates if l.get('hreflang')=='x-default'])==1,url
 for link in alternates:
  target=pages[link['href']]
  if link['hreflang']!='x-default':assert target.lang==link['hreflang'] and any(l.get('href')==url and l.get('hreflang')==page.lang for l in target.links),url
 for item in page.jsonld:
  if item.get('@type')=='SoftwareApplication':assert 'offers' not in item and item['operatingSystem']=='iOS'
  if item.get('@type')=='Article':
   assert item['@id']==url+'#article' and item['url']==url and item['citation']
   assert all(c in page.refs for c in item['citation'])
   crumb=next(i for i in page.jsonld if i.get('@type')=='BreadcrumbList')
   assert crumb['itemListElement'][-1]['item']==url
   assert all(c['item'] in pages for c in crumb['itemListElement'])
notfound=Page((ROOT/'404.html').read_text())
assert any(m.get('name')=='robots' and m.get('content')=='noindex,follow' for m in notfound.metas)
assert not any(l.get('hreflang') for l in notfound.links)
css=(ROOT/'assets/style.css').read_text();assert 'word-break:keep-all' in css and '194px' in css and '75px' in css
print(f'PASS {len(pages)} indexable routes, Article/Breadcrumb, current Store CTA, hreflang, assets and 404')
