from pathlib import Path
from html import escape
from datetime import date
import json
BASE='/carta-de-cacador-portugal-web/'
ORIGIN='https://mcyj.github.io'+BASE
OUT=Path('dist')
ARTICLES=[
('guia-exame-carta-cacador','Guia atual da Carta de Caçador em Portugal','Uma visão responsável do exame, das fontes oficiais e dos limites de uma aplicação de estudo.',[
'O exame para obtenção da Carta de Caçador é administrado pelo ICNF em Portugal continental. O procedimento oficial consultado em 23 de outubro de 2026 descreve 20 perguntas, três hipóteses por pergunta e aprovação com pelo menos 15 respostas corretas. Confirme a duração, a convocatória e as instruções atuais diretamente no ICNF.',
'A preparação abrange procedimento, legislação cinegética, biologia e identificação de espécies, ecologia, ordenamento, meios de caça, conduta no terreno, sanidade e segurança alimentar. Conhecer uma resposta isolada não substitui compreender o cenário e decidir de forma segura.',
'A app Carta de Caçador Portugal inclui 500 questões originais em português europeu, conceitos por capítulo, explicações e revisão dos erros. O treino é independente: não é exame oficial, carta, licença, seguro, formação de armas nem avaliação prática.',
'Use o estudo digital juntamente com o manual, a legislação consolidada, o calendário venatório e as orientações atuais do ICNF. Em matérias de segurança, animais e armas, procure formação presencial qualificada.' ]),
('formato-20-perguntas','Formato da prova: 20 perguntas e treino cronometrado','Como treinar ritmo e precisão sem confundir simulação com certificação.',[
'O procedimento público do ICNF consultado em 23 de outubro de 2026 descreve 20 perguntas de escolha múltipla, com três hipóteses e uma resposta correta. A app oferece treino de 20 perguntas em 30 minutos; este temporizador de prática não confirma, por si só, a duração oficial da convocatória.',
'Para passar, a referência indica pelo menos 75%, ou 15 respostas certas. Como números e procedimentos podem mudar, reveja a informação oficial perto da data da prova e siga sempre a sua convocatória.',
'Num treino de 20 perguntas, faça primeiro uma passagem calma, marque as dúvidas e reserve os minutos finais para rever enunciados e negações. Não altere uma resposta apenas por ansiedade; procure uma razão concreta.',
'O simulador da app mede apenas o desempenho naquele conjunto independente. Não prevê um resultado oficial e não observa identificação de espécies no terreno, manuseamento seguro ou outra competência prática.' ]),
('inscricao-taxas-2026-2027','Inscrição e taxas: o que confirmar no ICNF','Custos separados, fontes atuais e o que verificar antes do pagamento.',[
'A inscrição no exame e a emissão da Carta de Caçador são etapas distintas. Consulte a tabela de taxas vigente no ICNF e confirme a regra etária aplicável antes de calcular o valor a pagar. Este guia não fixa um preço oficial atual.',
'O custo pessoal pode incluir deslocação, formação, equipamento, seguro, licença de caça ou outros requisitos. Não trate a taxa de exame ou o preço de uma app como custo completo universal.',
'Antes de pagar, confirme elegibilidade, documentos, local, data, entidade recebedora e tabela vigente diretamente no ICNF. Não use links recebidos sem verificar o domínio e guarde o comprovativo oficial.',
'A compra da app é independente da autoridade de exame. Não paga inscrição, emissão, licença nem reserva. A versão iOS está publicada na App Store; confirme preço e condições de compra na ficha atual da loja.' ]),
('plano-estudo-quatro-semanas','Plano de estudo de quatro semanas','Uma sequência equilibrada entre lei, espécies, segurança e revisão.',[
'Na primeira semana, organize as fontes: procedimento atual, lei consolidada, calendário e manual. Estude conceitos como terreno cinegético, área de proteção, período venatório e diferença entre carta e licença.',
'Na segunda semana, trabalhe identificação e biologia. Compare espécies semelhantes, habitat, comportamento e sinais. A regra de campo é simples: se a identificação ou o fundo não forem seguros, não existe disparo.',
'Na terceira semana, concentre-se em segurança, meios, cães, cetraria, biossegurança e recuperação responsável. Conteúdo digital ajuda na teoria, mas não substitui instrução presencial nem prática supervisionada.',
'Na última semana, alterne simulados de 20 perguntas com revisão dos erros. Registe a razão de cada erro, volte à fonte oficial e faça pelo menos uma sessão no ritmo de 30 minutos sem interrupções.' ]),
('estudar-legislacao-cinegetica','Como estudar legislação cinegética sem decorar frases','Método por conceitos, decisões e revalidação das regras atuais.',[
'Comece pelas definições que estruturam as decisões: recurso cinegético, ato venatório, terreno cinegético, terreno não cinegético, área de proteção, refúgio e jornada. Relacione cada conceito com uma situação concreta.',
'Depois separe regras estáveis de dados variáveis. Princípios de segurança e conservação tendem a ser duradouros; espécies autorizadas, períodos, taxas, editais e condicionamentos exigem confirmação atual.',
'Crie cartões com uma pergunta de decisão: “que informação falta?” ou “o que bloqueia a ação?”. Esse formato evita memorização cega e treina a resposta conservadora perante incerteza.',
'Nunca use a app como texto legal. Consulte o Diário da República e o ICNF. Quando duas fontes parecerem divergir, suspenda a conclusão e procure a redação consolidada ou orientação competente.' ]),
('identificacao-especies','Identificação de espécies: estudar para evitar o erro','Como combinar morfologia, habitat e comportamento com uma decisão segura.',[
'Uma identificação responsável usa vários sinais: forma, dimensão, plumagem ou pelagem, movimento, vocalização, habitat, época e composição do grupo. Um único vestígio ou uma silhueta rápida raramente basta.',
'Estude também espécies não cinegéticas e protegidas que podem ser confundidas. Reconhecer o que não pode ser alvo é tão importante como conhecer a espécie pretendida.',
'Use imagens atuais e fontes de conservação, mas trate fotografias como preparação. Luz, distância e cobertura vegetal mudam a perceção no terreno. A dúvida deve sempre terminar em não disparar.',
'As perguntas independentes da app trabalham decisões e sinais conceituais. Não reproduzem o questionário oficial e não avaliam a identificação prática em condições reais.' ]),
('seguranca-campo-armas','Segurança no campo e com armas','Princípios que devem permanecer acima da pontuação e da oportunidade.',[
'Mantenha o cano numa direção segura e o dedo fora do gatilho até existir decisão deliberada de disparar. Identifique alvo, trajetória e fundo. Movimento, som ou cor isolados não são um alvo.',
'Descarregue antes de atravessar obstáculos, entrar em veículos ou lidar com uma queda. Se houver falha de fogo ou possível obstrução, mantenha direção segura e siga o manual e a formação recebida.',
'Num grupo, defina postos, setores, sinais e procedimento de paragem. Nevoeiro, pessoas, estradas, animais domésticos ou perda de comunicação podem obrigar a suspender a atividade.',
'Esta página não ensina operação de uma arma. Procure instrução prática qualificada e cumpra a legislação, licenciamento, armazenamento, transporte e regras do local.' ]),
('usar-simulados','Como usar simulados sem criar falsa confiança','Transforme cada tentativa num ciclo de diagnóstico, fonte e nova decisão.',[
'Faça o primeiro diagnóstico sem estudar para obter um ponto de partida. O resultado serve para priorizar capítulos e não representa probabilidade oficial de aprovação.',
'Em cada erro, classifique a causa: desconhecimento, leitura apressada, regra desatualizada ou confusão entre espécies e contextos. Volte à fonte apropriada e escreva a razão da resposta correta.',
'Varie a ordem dos temas e faça sessões cronometradas só depois de compreender os conceitos. Repetir a mesma sequência pode medir memória do ecrã em vez de aprendizagem.',
'Na app, alterne questões por capítulo, explicações, revisão de erros e treino cronometrado. O progresso de estudo fica no dispositivo. Consulte a ficha da loja e os ecrãs da sua versão para confirmar acesso e condições de compra, sem deduzir uma subscrição a partir deste guia.' ]),
('checklist-dia-exame','Checklist para o dia do exame','Confirmações administrativas e uma rotina simples para reduzir imprevistos.',[
'Na véspera, confirme local, hora, identificação, convocatória, documentos e instruções atuais. Planeie deslocação com margem e não dependa de uma captura de ecrã desatualizada.',
'Leve apenas materiais permitidos. A app não deve ser usada durante uma sessão controlada se as regras não o permitirem. Siga as instruções do responsável e esclareça dúvidas antes do início.',
'Leia cada pergunta por completo, repare em palavras como “não”, “sempre” e “apenas” e controle o tempo indicado pelo responsável. O treino de 30 minutos na app ajuda a criar uma rotina, mas não substitui as instruções oficiais do dia.',
'Depois da prova, use apenas o canal oficial para resultado e próximos passos. Uma pontuação do treino não antecipa nem altera o registo oficial.' ]),
('revisao-erros-e-repeticao','Revisão de erros e nova tentativa','Como recuperar lacunas sem memorizar a posição das opções.',[
'Guarde o tema e a explicação do erro, não apenas a letra escolhida. Formule uma nova situação em que o mesmo princípio seja aplicado de outra forma.',
'Se o erro envolve valor, prazo, espécie autorizada ou período venatório, confirme se a fonte continua vigente. Informação antiga pode produzir uma resposta coerente e ainda assim errada hoje.',
'Intercale revisão espaçada com testes mistos. Um bom sinal de domínio é explicar por que cada opção insegura ou incompatível deve ser rejeitada.',
'Para uma repetição oficial, consulte as condições atuais do ICNF e a sua notificação. Este site não fixa prazo de repetição nem promete elegibilidade, porque esses dados dependem do processo vigente.' ])]

STORE='https://apps.apple.com/pt/app/id6801904047'
SOURCE='https://www.icnf.pt/caca/cacar/exame/procedimentosdeexame'
UPDATED={'guia-exame-carta-cacador','formato-20-perguntas','inscricao-taxas-2026-2027','usar-simulados','checklist-dia-exame'}

def ld(value):
 return '<script type="application/ld+json">'+json.dumps(value,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')+'</script>'

def nav():
 return f'''<header class="top"><a class="brand" href="{BASE}"><img src="{BASE}assets/app-icon.png" width="44" height="44" alt="Ícone Carta de Caçador Portugal"><span>Carta de Caçador Portugal</span></a><nav aria-label="Navegação principal"><a href="{BASE}#funcionalidades">App</a><a href="{BASE}guias/">Guias</a><a href="{BASE}faq/">Perguntas</a><a href="{BASE}suporte/">Suporte</a><a href="{BASE}en/" lang="en">EN</a></nav></header>'''

def head(title,desc,path='',lang='pt-PT',hreflang=False,noindex=False):
 url=ORIGIN+path
 alt='' if noindex else (f'<link rel="alternate" hreflang="pt-PT" href="{ORIGIN}"><link rel="alternate" hreflang="en" href="{ORIGIN}en/"><link rel="alternate" hreflang="x-default" href="{ORIGIN}">' if hreflang else f'<link rel="alternate" hreflang="{lang}" href="{url}"><link rel="alternate" hreflang="x-default" href="{url}">')
 robots='<meta name="robots" content="noindex,follow">' if noindex else ''
 return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)}</title><meta name="description" content="{escape(desc)}"><link rel="canonical" href="{url}">{alt}{robots}<meta property="og:type" content="website"><meta property="og:title" content="{escape(title)}"><meta property="og:description" content="{escape(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{ORIGIN}assets/app-icon.png"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="{escape(title)}"><meta name="twitter:description" content="{escape(desc)}"><link rel="icon" href="{BASE}assets/app-icon.png"><link rel="stylesheet" href="{BASE}assets/style.css"></head><body><a class="skip" href="#conteudo">Saltar para o conteúdo</a>{nav()}'''

def foot():
 return f'''<footer><p><strong>Preparação independente.</strong> Sem afiliação ou aval do ICNF.</p><nav aria-label="Informação legal"><a href="{BASE}faq/">Perguntas frequentes</a><a href="{BASE}privacidade/">Privacidade</a><a href="{BASE}termos/">Termos</a><a href="{BASE}suporte/">Suporte</a><a href="{BASE}contacto/">Contacto</a></nav><p>Formato público e disponibilidade da app verificados em 23-10-2026. Confirme requisitos, duração, taxas e calendário no <a href="{SOURCE}">ICNF</a>.</p></footer></body></html>'''

def store(en=False):
 label='Download on the App Store' if en else 'Descarregar na App Store'
 return f'<div class="store-row"><a class="store-link" href="{STORE}" aria-label="{label}"><img src="{BASE}assets/app-store-badge.svg" width="158" height="53" alt="{label}"></a></div>'

def write(path,html):
 p=OUT/path;p.mkdir(parents=True,exist_ok=True);(p/'index.html').write_text(html)

def cards():
 return ''.join(f'<article class="card"><p class="eyebrow">Guia</p><h3><a href="{BASE}guias/{slug}/">{escape(title)}</a></h3><p>{escape(desc)}</p></article>' for slug,title,desc,_ in ARTICLES)

def build():
 import shutil
 if OUT.exists(): shutil.rmtree(OUT)
 shutil.copytree('assets',OUT/'assets')
 desc='Estude a Carta de Caçador com 500 questões originais em português europeu, explicações, revisão de erros e treino offline. App independente do ICNF.'
 structured=ld({"@context":"https://schema.org","@type":"SoftwareApplication","@id":ORIGIN+"#app","name":"Carta de Caçador Portugal","applicationCategory":"EducationalApplication","operatingSystem":"iOS","url":ORIGIN,"downloadUrl":STORE,"inLanguage":"pt-PT","description":desc})
 home=head('Carta de Caçador Portugal — preparação independente',desc,'','pt-PT',True)+structured+f'''<main id="conteudo"><section class="hero"><div><p class="eyebrow">PREPARAÇÃO INDEPENDENTE · PORTUGAL</p><h1>Estude decisões seguras, não respostas decoradas.</h1><p class="lead">500 questões originais em português europeu, explicações e revisão dos erros para organizar a preparação da Carta de Caçador.</p>{store()}<p class="status">App iOS publicada. Confirme preço e condições na App Store. Não concede carta, licença ou resultado oficial.</p><a href="{SOURCE}">Consultar o procedimento oficial do ICNF</a></div><img class="hero-icon" src="{BASE}assets/app-icon.png" width="1024" height="1024" alt="Ícone da aplicação Carta de Caçador Portugal"></section>
<section class="facts" aria-label="Prática independente e referência pública"><div><strong>500</strong><span>questões originais na app</span></div><div><strong>20</strong><span>perguntas na prova teórica</span></div><div><strong>15/20</strong><span>aprovação indicada pelo ICNF</span></div><div><strong>Offline</strong><span>estudo e progresso local</span></div></section>
<section id="funcionalidades"><p class="eyebrow">FLUXO DE ESTUDO</p><h2>Compreender, praticar e voltar aos erros</h2><div class="grid3"><article><h3>Estudo por capítulo</h3><p>Organize legislação, espécies, ecologia, segurança e outros temas em conceitos e questões.</p></article><article><h3>Treino cronometrado</h3><p>Pratique conjuntos de 20 perguntas em 30 minutos. O temporizador da app não substitui a convocatória oficial.</p></article><article><h3>Revisão com explicações</h3><p>Reveja respostas, repita erros e acompanhe o progresso guardado no dispositivo.</p></article></div></section>
<section><p class="eyebrow">A APP POR DENTRO</p><h2>Veja os ecrãs publicados na App Store</h2><div class="screens">{''.join(f'<figure><img src="{BASE}assets/screen-{i}.jpg" width="221" height="480" loading="lazy" decoding="async" alt="{alt}"><figcaption>{alt}</figcaption></figure>' for i,alt in enumerate(['Apresentação da app','Prática e explicações','Estudo organizado'],1))}</div></section>
<section><p class="eyebrow">FONTES E LIMITES</p><h2>Preparação alinhada com fontes públicas</h2><p class="wide">O âmbito público do ICNF e a legislação orientam os temas, sem copiar o questionário oficial. A app não substitui formação prática, segurança de armas, identificação no terreno, seguro, inscrição, licença ou carta.</p></section>
<section><div class="section-head"><div><p class="eyebrow">GUIAS</p><h2>Informação para preparar com responsabilidade</h2></div><a href="{BASE}guias/">Ver todos</a></div><div class="cards">{cards()}</div></section></main>'''+foot()
 write(Path('.'),home)
 guides=head('Guias da Carta de Caçador','Guias independentes sobre formato, inscrição, estudo, espécies e segurança.','guias/')+f'<main id="conteudo"><p class="eyebrow">CENTRO DE GUIAS</p><h1>Preparar com fontes, contexto e segurança</h1><p class="lead">Dez guias originais. Dados variáveis devem ser confirmados diretamente no ICNF.</p><div class="cards">{cards()}</div></main>'+foot();write(Path('guias'),guides)
 for index,(slug,title,ad,paras) in enumerate(ARTICLES):
  body=''.join(f'<p>{escape(p)}</p>' for p in paras)
  path=f'guias/{slug}/';url=ORIGIN+path;modified='2026-10-23' if slug in UPDATED else '2026-09-28'
  article_data={"@context":"https://schema.org","@type":"Article","@id":url+"#article","url":url,"inLanguage":"pt-PT","headline":title,"datePublished":"2026-09-28","dateModified":modified,"author":{"@type":"Organization","@id":ORIGIN+"#publisher","name":"RushLabs","url":ORIGIN},"publisher":{"@type":"Organization","@id":ORIGIN+"#publisher","name":"RushLabs","url":ORIGIN},"mainEntityOfPage":url,"citation":[SOURCE]}
  crumbs=ld({"@context":"https://schema.org","@type":"BreadcrumbList","@id":url+"#breadcrumbs","itemListElement":[{"@type":"ListItem","position":i+1,"name":name,"item":item} for i,(name,item) in enumerate([('Início',ORIGIN),('Guias',ORIGIN+'guias/'),(title,url)])]})
  other=ARTICLES[(index+1)%len(ARTICLES)]
  html=head(title+' — Carta de Caçador Portugal',ad,path)+ld(article_data)+crumbs+f'<main id="conteudo" class="article"><nav class="crumb" aria-label="Breadcrumb"><a href="{BASE}">Início</a> / <a href="{BASE}guias/">Guias</a> / <span>{escape(title)}</span></nav><p class="eyebrow">GUIA · ATUALIZADO {modified}</p><h1>{escape(title)}</h1><p class="lead">{escape(ad)}</p>{body}<aside><strong>Confirmação oficial</strong><p>Consulte procedimento, convocatória e legislação atuais antes de tomar qualquer decisão.</p><a href="{SOURCE}">Abrir o ICNF</a></aside><h2>Continuar a preparação</h2><p><a href="{BASE}guias/{other[0]}/">{escape(other[1])}</a></p><p><a class="button secondary" href="{BASE}guias/">Voltar aos guias</a></p></main>'+foot();write(Path('guias')/slug,html)
 faq_items=[('A aplicação é oficial?','Não. É uma ferramenta de estudo independente, sem afiliação ou aval do ICNF. Não concede carta ou licença e não garante aprovação.'),('Quantas perguntas inclui?','A ficha pública atual descreve 500 questões originais em português europeu, com explicações e revisão. Não são perguntas oficiais.'),('Qual é o formato indicado pelo ICNF?','O procedimento consultado descreve 20 perguntas com três hipóteses e aprovação a partir de 15 respostas corretas. Confirme as instruções atuais no ICNF.'),('Os 30 minutos são uma regra oficial confirmada?','O treino da app usa 20 perguntas em 30 minutos. Para a duração oficial da sua prova, consulte a convocatória e o ICNF.'),('Onde confirmo preço e acesso?','Na ficha atual da App Store e nos ecrãs da sua versão. Este site não fixa preço nem condições de subscrição.'),('Posso estudar sem ligação?','A app inclui estudo offline e progresso local. Instalação, compras e operações da loja podem exigir ligação.')]
 faq=head('Perguntas frequentes — Carta de Caçador Portugal','Respostas sobre app independente, 500 questões, formato ICNF, treino offline e condições de compra.','faq/')+'<main id="conteudo" class="article"><h1>Perguntas frequentes</h1>'+''.join(f'<section class="faq-item"><h2>{escape(q)}</h2><p>{escape(a)}</p></section>' for q,a in faq_items)+f'<p><a href="{SOURCE}">Confirmar o procedimento no ICNF</a></p>'+store()+'</main>'+foot();write(Path('faq'),faq)
 pages={
 'privacidade':('Privacidade','Como o site e a aplicação tratam informação.','<p>Este site estático não inclui analytics, formulários, contas ou cookies de publicidade. O alojamento GitHub Pages pode manter registos técnicos segundo as políticas do GitHub.</p><p>O progresso de estudo da aplicação fica no dispositivo. Instalação e compras seguem as interfaces e políticas da loja. Consulte também as informações de privacidade da ficha atual da app.</p><p>Não envie documentos pessoais, detalhes de armas ou informação clínica por email de suporte.</p>'),
 'termos':('Termos de utilização','Limites do serviço independente de estudo.','<p>O conteúdo não está afiliado nem é avalizado pelo ICNF. Não constitui aconselhamento jurídico, formação de armas, certificação, seguro, inscrição, licença ou Carta de Caçador.</p><p>Não existe garantia de aprovação. Regras, taxas e calendários podem mudar; confirme fontes oficiais. Compras digitais seguem os termos e mecanismos da respetiva loja.</p><p>Não use conteúdo digital para substituir supervisão prática ou justificar atividade não autorizada.</p>'),
 'suporte':('Suporte','Ajuda com prática, progresso local e acesso à aplicação.','<h2>Problemas de acesso ou compra</h2><p>Confirme a conta da loja e as condições apresentadas na sua versão. Se existir opção de restauro, utilize a mesma conta da compra. Não envie credenciais ou recibos com dados pessoais.</p><h2>Progresso e prática</h2><p>Indique a versão e os passos para reproduzir o problema. O desempenho de treino é privado e não constitui resultado oficial.</p><h2>Questões sobre exame ou licença</h2><p>Contacte o ICNF. O suporte da app não confirma elegibilidade, documentos, armas, licenças ou calendário.</p>'),
 'contacto':('Contacto','Contacto técnico da aplicação independente.','<p>Suporte técnico RushLabs. Indique versão, dispositivo e passos para reproduzir um problema, sem enviar documentos pessoais.</p><p>Para inscrição, exame, carta, licença ou calendário, use os contactos oficiais do ICNF.</p>')
 }
 for path,(title,description,body) in pages.items():
  html=head(title+' — Carta de Caçador Portugal',description,path+'/')+f'<main id="conteudo" class="article"><h1>{title}</h1>{body}<p>Contacto técnico: <a href="mailto:june1012june@gmail.com">june1012june@gmail.com</a>.</p></main>'+foot();write(Path(path),html)
 en=head('Carta de Caçador Portugal — independent study app','Study with 500 original European Portuguese questions, explanations and offline progress. Independent of ICNF.','en/','en',True)+f'''<main id="conteudo"><section class="hero"><div><p class="eyebrow">INDEPENDENT STUDY · PORTUGAL</p><h1>Prepare with safety-first decisions.</h1><p class="lead">500 original European Portuguese questions, explanations, timed practice and local study progress. Not affiliated with ICNF and not a licence, official exam or practical training.</p>{store(True)}<p class="status">Available on the App Store. Check the current listing for price and purchase conditions.</p></div><img class="hero-icon" src="{BASE}assets/app-icon.png" width="1024" height="1024" alt="Carta de Caçador Portugal app icon"></section><section><h2>Practice is not certification</h2><p class="wide">The ICNF procedure consulted describes 20 questions with three options and a pass threshold of 15 correct answers. The app's 30-minute practice timer is not evidence of the official duration. Reconfirm eligibility, dates, fees and instructions with <a href="{SOURCE}">ICNF</a>.</p><p><a href="{BASE}guias/">Read the Portuguese study guides</a></p></section></main>'''+foot();write(Path('en'),en)
 notfound=head('Página não encontrada','A página solicitada não existe.','404.html',noindex=True)+f'<main id="conteudo" class="article"><h1>Página não encontrada</h1><p><a href="{BASE}">Voltar ao início</a></p></main>'+foot();(OUT/'404.html').write_text(notfound)
 routes=['','guias/','faq/','privacidade/','termos/','suporte/','contacto/','en/']+[f'guias/{a[0]}/' for a in ARTICLES]
 def modified(path):
  return '2026-09-28' if path.startswith('guias/') and path!='guias/' and path.split('/')[1] not in UPDATED else '2026-10-23'
 (OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{ORIGIN+p}</loc><lastmod>{modified(p)}</lastmod></url>' for p in routes)+'</urlset>')
 (OUT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {ORIGIN}sitemap.xml\n')
 (OUT/'.nojekyll').write_text('')

if __name__=='__main__': build(); print(f'built {sum(1 for _ in OUT.rglob("*.html"))} html pages')
