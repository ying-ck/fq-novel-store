# -*- coding: utf-8 -*-
import requests as req
from lxml import etree
from ebooklib import epub
import json,time,random,os

CODE = [[58344,58715],[58345,58716]]
charset=json.loads('[["D","在","主","特","家","军","然","表","场","4","要","只","v","和","?","6","别","还","g","现","儿","岁","?","?","此","象","月","3","出","战","工","相","o","男","直","失","世","F","都","平","文","什","V","O","将","真","T","那","当","?","会","立","些","u","是","十","张","学","气","大","爱","两","命","全","后","东","性","通","被","1","它","乐","接","而","感","车","山","公","了","常","以","何","可","话","先","p","i","叫","轻","M","士","w","着","变","尔","快","l","个","说","少","色","里","安","花","远","7","难","师","放","t","报","认","面","道","S","?","克","地","度","I","好","机","U","民","写","把","万","同","水","新","没","书","电","吃","像","斯","5","为","y","白","几","日","教","看","但","第","加","候","作","上","拉","住","有","法","r","事","应","位","利","你","声","身","国","问","马","女","他","Y","比","父","x","A","H","N","s","X","边","美","对","所","金","活","回","意","到","z","从","j","知","又","内","因","点","Q","三","定","8","R","b","正","或","夫","向","德","听","更","?","得","告","并","本","q","过","记","L","让","打","f","人","就","者","去","原","满","体","做","经","K","走","如","孩","c","G","给","使","物","?","最","笑","部","?","员","等","受","k","行","一","条","果","动","光","门","头","见","往","自","解","成","处","天","能","于","名","其","发","总","母","的","死","手","入","路","进","心","来","h","时","力","多","开","已","许","d","至","由","很","界","n","小","与","Z","想","代","么","分","生","口","再","妈","望","次","西","风","种","带","J","?","实","情","才","这","?","E","我","神","格","长","觉","间","年","眼","无","不","亲","关","结","0","友","信","下","却","重","己","老","2","音","字","m","呢","明","之","前","高","P","B","目","太","e","9","起","稜","她","也","W","用","方","子","英","每","理","便","四","数","期","中","C","外","样","a","海","们","任"],["s","?","作","口","在","他","能","并","B","士","4","U","克","才","正","们","字","声","高","全","尔","活","者","动","其","主","报","多","望","放","h","w","次","年","?","中","3","特","于","十","入","要","男","同","G","面","分","方","K","什","再","教","本","己","结","1","等","世","N","?","说","g","u","期","Z","外","美","M","行","给","9","文","将","两","许","张","友","0","英","应","向","像","此","白","安","少","何","打","气","常","定","间","花","见","孩","它","直","风","数","使","道","第","水","已","女","山","解","d","P","的","通","关","性","叫","儿","L","妈","问","回","神","来","S","","四","望","前","国","些","O","v","l","A","心","平","自","无","军","光","代","是","好","却","c","得","种","就","意","先","立","z","子","过","Y","j","表","","么","所","接","了","名","金","受","J","满","眼","没","部","那","m","每","车","度","可","R","斯","经","现","门","明","V","如","走","命","y","6","E","战","很","上","f","月","西","7","长","夫","想","话","变","海","机","x","到","W","一","成","生","信","笑","但","父","开","内","东","马","日","小","而","后","带","以","三","几","为","认","X","死","员","目","位","之","学","远","人","音","呢","我","q","乐","象","重","对","个","被","别","F","也","书","稜","D","写","还","因","家","发","时","i","或","住","德","当","o","l","比","觉","然","吃","去","公","a","老","亲","情","体","太","b","万","C","电","理","?","失","力","更","拉","物","着","原","她","工","实","色","感","记","看","出","相","路","大","你","候","2","和","?","与","p","样","新","只","便","最","不","进","T","r","做","格","母","总","爱","身","师","轻","知","往","加","从","?","天","e","H","?","听","场","由","快","边","让","把","任","8","条","头","事","至","起","点","真","手","这","难","都","界","用","法","n","处","下","又","Q","告","地","5","k","t","岁","有","会","果","利","民"]]')
headers_lib = [
    {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47'}
    ]

headers = headers_lib[random.randint(0,len(headers_lib)-1)]

def get_cookie(zj,t=0):
    global cookie
    bas = 1000000000000000000
    if t==0:
        for i in range(random.randint(bas*6,bas*8),bas*9):
            time.sleep(random.randint(50,150)/1000)
            cookie = 'novel_web_id='+str(i)
            if len(down_text(zj,2))>200:
                with open(cookie_path, 'w', encoding='UTF-8') as f:
                    json.dump(cookie,f)
                return 's'
    else:
        cookie = t
        if len(down_text(zj,2))>200:
            return 's'
        else:
            return 'err'

def add_output(k, v):
    cmd = f'echo "{k}={v}" >> $GITHUB_OUTPUT'
    print(f'{cmd}: {os.system(cmd)}')

def down_zj(it):
    global headers
    an = {}
    ele = etree.HTML(req.get('https://fanqienovel.com/page/'+str(it),headers=headers).text)
    a = ele.xpath('//div[@class="chapter"]/div/a')
    for i in range(len(a)):
        an[a[i].text] = a[i].xpath('@href')[0].split('/')[-1]
    if ele.xpath('//h1/text()')==[]:
        return ['err',0,0]
    return [ele.xpath('//h1/text()')[0],an,ele.xpath('//span[@class="info-label-yellow"]/text()')]

def interpreter(uni,mode):
    bias = uni - CODE[mode][0]
    if bias < 0 or bias >= len(charset[mode]) or charset[mode][bias] =='?':
        return chr(uni)
    return charset[mode][bias]

def str_interpreter(n,mode):
    s = ''
    for i in range(len(n)):
        uni = ord(n[i])
        if CODE[mode][0] <= uni <= CODE[mode][1]:
            s += interpreter(uni,mode)
        else:
            s += n[i]
    return s

def down_text(it, mod=1):
    global cookie
    headers2 = headers
    headers2['cookie'] = cookie
    f = False
    while True:
        try:
            res = req.get('https://fanqienovel.com/reader/' + str(it), headers=headers2)
            n = '\n'.join(etree.HTML(res.text).xpath('//div[@class="muye-reader-content noselect"]//p/text()'))
            break
        except:
            if mod == 2:
                return ('err')
            f = True
            time.sleep(0.4)
    if mod == 1:
        s = str_interpreter(n, 0)
    else:
        s = n
    try:
        if mod == 1:
            return s, f
        else:
            return s
    except:
        s = s[6:]
        tmp = 1
        a = ''
        for i in s:
            if i == '<':
                tmp += 1
            elif i == '>':
                tmp -= 1
            elif tmp == 0:
                a += i
            elif tmp == 1 and i == 'p':
                a = (a + '\n').replace('\n\n', '\n')
        return a, f

def sanitize_filename(filename):
    illegal_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    illegal_chars_rep = ['＜','＞','：','＂','／','＼','｜','？','＊']
    for i in range(len(illegal_chars)):
        filename = filename.replace(illegal_chars[i], illegal_chars_rep[i])
    return filename


def down_book(it):
    global ft
    name, zj, zt = down_zj(it)
    if name == 'err':
        return 'err'
    zt = zt[0]

    safe_name = sanitize_filename(name)
    book_dir = os.path.join(script_dir, safe_name)

    book_json_path = os.path.join(bookstore_dir, safe_name + '.json')

    if os.path.exists(book_json_path):
        with open(book_json_path, 'r', encoding='UTF-8') as json_file:
            ozj = json.load(json_file)
    else:
        ozj = {}
    
    cs = 0
    tcs=0
    for i in zj:
        f = False
        if i in ozj:
            try:
                int(ozj[i])
                f = True
            except:
                zj[i] = ozj[i]
        else:
            f = True
        if f:
            zj[i],st = down_text(zj[i])
            ft=True
            time.sleep(random.randint(config['delay'][0],config['delay'][1])/1000)
            if st:
                tcs+=1
                if tcs>7:
                    tcs=0
                    get_cookie(tzj)
            cs += 1
            if cs>=5:
                cs = 0
                with open(book_json_path, 'w', encoding='UTF-8') as json_file:
                    json.dump(zj, json_file,ensure_ascii=False)

    with open(book_json_path, 'w', encoding='UTF-8') as json_file:
        json.dump(zj, json_file,ensure_ascii=False)
    
    fg = '\n' + config['kgf'] * config['kg']
    if config['save_mode']==1:
        text_file_path = os.path.join(config['save_path'], safe_name + '.txt')
        with open(text_file_path, 'w', encoding='UTF-8') as text_file:
            for chapter_title in zj:
                text_file.write('\n'+chapter_title + fg)
                if config['kg'] == 0:
                    text_file.write(zj[chapter_title] + '\n')
                else:
                    text_file.write(zj[chapter_title].replace('\n', fg) + '\n')
    elif config['save_mode']==2:
        text_dir_path = os.path.join(config['save_path'], safe_name)
        if not os.path.exists(text_dir_path):
            os.makedirs(text_dir_path)
        for chapter_title in zj:
            text_file_path = os.path.join(text_dir_path, sanitize_filename(chapter_title) + '.txt')
            with open(text_file_path, 'w', encoding='UTF-8') as text_file:
                text_file.write(fg)
                if config['kg'] == 0:
                    text_file.write(zj[chapter_title] + '\n')
                else:
                    text_file.write(zj[chapter_title].replace('\n', fg) + '\n')
        
    else:
        print('保存模式出错！')

    return zt

def down_book_epub(it):
    name, zj, zt = down_zj(it)
    if name == 'err':
        return 'err'
    zt = zt[0]

    safe_name = sanitize_filename(name)
    book_dir = os.path.join(script_dir, safe_name)

    book_json_path = os.path.join(bookstore_dir, safe_name + '.json')

    if os.path.exists(book_json_path):
        with open(book_json_path, 'r', encoding='UTF-8') as json_file:
            ozj = json.load(json_file)
    else:
        ozj = {}

    book = epub.EpubBook()
    book.set_title(name)
    book.set_language('zh')

    # 创建目录列表
    toc = []

    cs = 0
    for chapter_title, chapter_id in zj.items():
        f = False
        if chapter_title in ozj:
            try:
                int(ozj[chapter_title])
                f = True
            except:
                zj[chapter_title] = ozj[chapter_title]
        else:
            f = True
        if f:
            chapter_content = down_text(chapter_id)
            time.sleep(random.randint(config['delay'][0], config['delay'][1]) / 1000)
            cs += 1
            if cs >= 5:
                cs = 0
                with open(book_json_path, 'w', encoding='UTF-8') as json_file:
                    json.dump(zj, json_file, ensure_ascii=False)

            # 保留原来换行符
            formatted_content = chapter_content.replace('\n', '<br/>')
            chapter = epub.EpubHtml(title=chapter_title, file_name=f'{chapter_title}.xhtml', content=f'<h1>{chapter_title}</h1><p>{formatted_content}</p>')
            book.add_item(chapter)

            # 将章节添加到目录列表
            toc.append((epub.Section(chapter_title), [chapter]))
            book.spine.append(chapter)
        pbar.update(1)

    # 设置目录
    book.toc = toc
    # 添加目录文件
    book.add_item(epub.EpubNcx())
    # 编写 EPUB 文件
    epub.write_epub(os.path.join(config['save_path'], f'{safe_name}.epub'), book, {})

    return 's'

def down_book_html(it):
    name, zj, zt = down_zj(it)
    if name == 'err':
        return 'err'
    zt = zt[0]

    safe_name = sanitize_filename(name)
    book_dir = os.path.join(script_dir, f"{safe_name}(html)")
    if not os.path.exists(book_dir):
        os.makedirs(book_dir)

    book_json_path = os.path.join(bookstore_dir, safe_name + '.json')

    if os.path.exists(book_json_path):
        with open(book_json_path, 'r', encoding='UTF-8') as json_file:
            ozj = json.load(json_file)
    else:
        ozj = {}

    # 生成目录 HTML 文件内容，添加 CSS 样式和响应式设计的 meta 标签
    toc_content = """
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>目录</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f5f5f5;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li a {
            color: #007bff;
            text-decoration: none;
        }
        li a:hover {
            text-decoration: underline;
        }
        p {
            margin: 10px 0;
        }
    </style>
</head>
<body>
<h1>目录</h1>
<ul>
"""
    for chapter_title in zj:
        toc_content += f"<li><a href='{chapter_title}.html'>{chapter_title}</a></li>"
    toc_content += "</ul></body></html>"

    # 将目录内容写入文件
    with open(os.path.join(book_dir, "index.html"), "w", encoding='UTF-8') as toc_file:
        toc_file.write(toc_content)

    cs = 0
    for chapter_title, chapter_id in zj.items():
        f = False
        if chapter_title in ozj:
            try:
                int(ozj[chapter_title])
                f = True
            except:
                zj[chapter_title] = ozj[chapter_title]
        else:
            f = True
        if f:
            chapter_content = down_text(chapter_id)
            time.sleep(random.randint(config['delay'][0], config['delay'][1]) / 1000)
            cs += 1
            if cs >= 5:
                cs = 0
                with open(book_json_path, 'w', encoding='UTF-8') as json_file:
                    json.dump(zj, json_file, ensure_ascii=False)

            # 生成章节 HTML 文件内容，添加 CSS 样式、返回顶部按钮和装饰元素，同时保留换行符
            formatted_content = chapter_content.replace('\n', '<br/>')
            next_chapter_button = ""
            if len(zj) > list(zj.keys()).index(chapter_title) + 1:
                next_chapter_key = list(zj.keys())[list(zj.keys()).index(chapter_title) + 1]
                next_chapter_button = f"<button onclick=\"location.href='{next_chapter_key}.html'\">下一章</button>"

            chapter_html_content = f"""
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{chapter_title}</title>
    <style>
        body {{
            display: flex;
            min-height: 100vh;
        }}
     .left-side {{
            flex: 1;
            background-color: #ffffff;
        }}
     .content {{
            flex: 3;
            background-color: white;
            padding: 20px;
        }}
     .right-side {{
            flex: 1;
            background-color: #ffffff;
        }}
        button {{
            background-color: #d3d3d3;
            color: black;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
        }}
        #toggle-mode {{
            position: absolute;
            top: 20px;
            right: 20px;
        }}
        @media (prefers-color-scheme: dark) {{
            body {{
                background-color: #333;
            }}
         .left-side,.right-side {{
                background-color: #444;
            }}
         .content {{
                background-color: #222;
                color: white;
            }}
            button {{
                background-color: #555;
                color: white;
            }}
        }}
    </style>
    <script>
        let isDarkMode = false;
        document.getElementById('toggle-mode').addEventListener('click', function() {{
            isDarkMode =!isDarkMode;
            if (isDarkMode) {{
                document.body.classList.add('dark-mode');
                localStorage.setItem('mode', 'dark');
            }} else {{
                document.body.classList.remove('dark-mode');
                localStorage.setItem('mode', 'light');
            }}
        }});

        // 检查本地存储以确定初始模式
        const savedMode = localStorage.getItem('mode');
        if (savedMode === 'dark') {{
            document.body.classList.add('dark-mode');
            isDarkMode = true;
        }}
    </script>
</head>
<body>
<div class="left-side"></div>
<div class="content">
    <h1>{chapter_title}</h1>
    <p>{formatted_content}</p>
    <a href="#" id="back-to-top">返回顶部</a>
</div>
<div class="right-side"></div>
<div style="text-align: center; position: fixed; bottom: 20px; width: 100%;">
    <button onclick="location.href='index.html'">目录</button>
    {next_chapter_button}
    <button onclick="backToTop()">返回顶部</button>
    <button id="toggle-mode">切换模式</button>
</div>
<script>
    // 当用户滚动页面时显示/隐藏返回顶部按钮
    window.onscroll = function() {{
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {{
            document.getElementById("back-to-top").style.display = "block";
        }} else {{
            document.getElementById("back-to-top").style.display = "none";
        }}
    }};

    // 当用户点击返回顶部按钮时，滚动页面到顶部
    function backToTop() {{
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    }}
</script>
</body>
</html>
"""

            # 将章节内容写入文件
            with open(os.path.join(book_dir, f"{chapter_title}.html"), "w", encoding='UTF-8') as chapter_file:
                chapter_file.write(chapter_html_content)
        pbar.update(1)

    return 's'

def down_book_latex(it):
    name, zj, zt = down_zj(it)
    if name == 'err':
        return 'err'
    zt = zt[0]

    safe_name = sanitize_filename(name)

    book_json_path = os.path.join(bookstore_dir, safe_name + '.json')

    if os.path.exists(book_json_path):
        with open(book_json_path, 'r', encoding='UTF-8') as json_file:
            ozj = json.load(json_file)
    else:
        ozj = {}

    latex_content = ""
    for chapter_title, chapter_id in zj.items():
        f = False
        if chapter_title in ozj:
            try:
                int(ozj[chapter_title])
                f = True
            except:
                zj[chapter_title] = ozj[chapter_title]
        else:
            f = True
        if f:
            chapter_content = down_text(chapter_id)
            time.sleep(random.randint(config['delay'][0], config['delay'][1]) / 1000)

            # 将章节内容转换为 LaTeX 格式
            formatted_content = chapter_content.replace('\n', '\\newline ')
            latex_content += f"\\chapter{{{chapter_title}}}\n{formatted_content}\n"

    # 在脚本所在目录下输出 LaTeX 文件
    latex_file_path = os.path.join(script_dir, f'{safe_name}.tex')
    with open(latex_file_path, 'w', encoding='UTF-8') as latex_file:
        latex_file.write(latex_content)

    return 's'
                
def book2down(inp):
    if str(inp)[:4] == 'http':
        inp = inp.split('?')[0].split('/')[-1]
    try:
        book_id = int(inp)
        with open(record_path, 'r', encoding='UTF-8') as f:
            records = json.load(f)
        if book_id not in records:
            records.append(book_id)
        with open(record_path, 'w', encoding='UTF-8') as f:
            json.dump(records, f)
        if config['save_mode'] == 3:
            status = down_book_epub(book_id)
        elif config['save_mode'] == 4:
            status = down_book_html(book_id)
        elif config['save_mode'] == 5:  # 新增的 LaTeX 保存模式
            status = down_book_latex(book_id)
        else:
            status = down_book(book_id)
        if status == 'err':
            return 'err'
        else:
            return 's'
    except ValueError:
        return 'err'


#script_dir = os.path.dirname(os.path.abspath(__file__))
script_dir = ''

# 设置data文件夹的路径
data_dir = os.path.join(script_dir, 'data')

# 检查data文件夹是否存在，如果不存在则创建
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# 设置bookstore文件夹的路径
bookstore_dir = os.path.join(data_dir,'bookstore')

# 检查bookstore文件夹是否存在，如果不存在则创建
if not os.path.exists(bookstore_dir):
    os.makedirs(bookstore_dir)

# 更新record.json和config.json的文件路径
record_path = os.path.join(data_dir, 'record.json')
config_path = os.path.join(data_dir, 'config.json')

# 检查并创建配置文件config.json
config_path = os.path.join(data_dir, 'config.json')
reset = {'kg': 0,'kgf': '　','delay': [50, 150], 'save_path': '', 'save_mode': 1, 'space_mode': 'halfwidth'}
if not os.path.exists(config_path):
    if os.path.exists('config.json'):
        os.replace('config.json',config_path)
    else:
        config = reset
        with open(config_path, 'w', encoding='UTF-8') as f:
            json.dump(reset, f)
else:
    with open(config_path, 'r', encoding='UTF-8') as f:
        config = json.load(f)
for i in reset:
    if not i in config:
        config[i] = reset[i]

# 检查并创建记录文件record.json
record_path = os.path.join(data_dir, 'record.json')
if not os.path.exists(record_path):
    if os.path.exists('record.json'):
        os.replace('record.json',record_path)
    else:
        with open(record_path, 'w', encoding='UTF-8') as f:
            json.dump([], f)

print('get cookie')
cookie_path = os.path.join(data_dir, 'cookie.json')
tzj = int(random.choice(list(down_zj(7143038691944959011)[1].values())[21:]))
tmod = 0
if os.path.exists(cookie_path):
    with open(cookie_path, 'r', encoding='UTF-8') as f:
        cookie = json.load(f)
    tmod = 1
if tmod==0 or get_cookie(tzj,cookie)=='err':
    get_cookie(tzj)
print('success')

ft=False
with open(record_path, 'r', encoding='UTF-8') as f:
    records = json.load(f)
for book_id in records:
    status = book2down(book_id)
    if status == 'err' or status == '已完结':
        records.remove(book_id)
with open(record_path, 'w', encoding='UTF-8') as f:
    json.dump(records, f)
if ft:
    add_output('found_new', 'true')
print('update success')


