import os
import random
import string

import requests as requests

import html2text
from bs4 import BeautifulSoup

def html_table_to_markdown(html_table):
    soup = BeautifulSoup(html_table, 'html.parser')

    tables = soup.find_all('table')

    # 遍历每个表格并替换为Markdown格式
    for table in tables:
        markdown_table = ""


        thead = table.find('thead')
        if thead:
            markdown_table += "| " + " | ".join([th.text.strip() for th in thead.find_all('th')]) + " |<br>"
            markdown_table += "| " + " | ".join(["---" for _ in thead.find_all('th')]) + " |<br>"

        tbody = table.find('tbody')
        if tbody:
            for row in tbody.find_all('tr'):
                markdown_table += "| " + " | ".join([td.text.strip() for td in row.find_all('td')]) + " |<br>"

        # 创建新的Markdown表格
        new_table = soup.new_tag('p')
        new_table.append(BeautifulSoup(markdown_table, 'html.parser'))

        # 用新的Markdown表格替换原始表格
        table.replace_with(new_table)

    return soup

def sanitize_filename(filename):
    valid_chars = {char: None for char in string.whitespace + r'\/:*?"<>|'}

    # 使用 translate 方法删除非法字符
    sanitized_filename = filename.translate(str.maketrans(valid_chars))

    return sanitized_filename


def generate_random_filename(filename):
    """生成一个随机的文件名"""
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    random_str = sanitize_filename(random_str)
    return filename[:-3] + f"{random_str}.md"

def ensure_directory_exists(directory_path):
    """
    检测目录是否存在，如果不存在则创建目录
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def write_to_file(content, filename):
    """写入内容到文件"""
    target_directory = 'md'
    ensure_directory_exists(target_directory)

    full_path = os.path.join(target_directory, filename)
    while os.path.exists(full_path):
        # 如果文件已存在，则生成新的随机文件名
        filename = generate_random_filename(filename)
        full_path = os.path.join(target_directory, filename)

    with open(full_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"File {filename} Download！")



def getHttpResponse(url, titleID=None, contentID=None, cookie_data=None):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "DNT": "1",  # Do Not Track
        # 添加其他所需的头信息
    }
    cookies=""
    if cookie_data is not None:
        cookies = {cookie["name"]: cookie["value"] for cookie in cookie_data}

    response = requests.get(url, headers=headers, cookies=cookies)

    # 使用Beautiful Soup解析HTML
    html_content = response.text
    # soup = BeautifulSoup(html_content, 'html.parser')
    # print(html_content)
    soup=html_table_to_markdown(html_content)
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    random_str = sanitize_filename(random_str)
    if titleID is not None and titleID!="":

        tittle = str(soup.find(id=titleID))

    else : tittle=random_str
    if contentID is None or contentID=="":
        html_content=str(soup)
    else :html_content = str(soup.find(id=contentID))
    # print(html_content)
    return [tittle, html_content]

    # 现在你可以使用Beautiful Soup的方法来查找和提取页面中的信息


def html2markdown(url, titleID=None, contentID=None, cookie_data=None):

    ans = getHttpResponse(url, titleID, contentID, cookie_data)

    # print(html_content)
    tittle = html2text.html2text(ans[0])
    html_content = html2text.html2text(ans[1])

    fileName = tittle[2:]
    fileName = sanitize_filename(fileName + "") + ".md"

    write_to_file(tittle + html_content, fileName)
