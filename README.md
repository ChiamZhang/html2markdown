# html2markdown

`html2markdown` is a Python script that transforms HTML pages into clean, readable plain ASCII text. What's even better is that this ASCII text conveniently conforms to valid Markdown, a text-to-HTML formatting syntax.

To use it, one only needs to provide the URL of a website along with a few simple parameters. The script then converts the content into Markdown and downloads it locally, naming the file as `title.md`.

`html2markdown` 是一个将 HTML 页面转换为干净、易读的纯 ASCII 文本的 Python 脚本。更好的是，该 ASCII 文本也恰好是有效的 Markdown（一种文本到 HTML 的格式）。

我们只需要输入一个网站的url和简单的参数就可以进行使用，将markdown按照title.md命名下载到本地。

- [html2markdown](#html2markdown)
  - [English](#english)
    - [Introduction](#introduction)
      - [Functionality](#functionality)
      - [Demo](#demo)
  - [中文](#中文)
    - [介绍](#介绍)
      - [功能](#功能)
      - [demo](#demo-1)

## English

### Introduction

This directory consists of two files:

- `html2text.py`: This is derived from the GitHub project "html2text." I have performed a simple refactoring, modifying modules specific to Python 2, and eliminating unnecessary code.
  
- `html2markdown.py`: This is the core code responsible for implementing the functionality.

#### Functionality

1. **Web Scraping and Markdown Conversion:**
   - Utilizes the `requests` library to retrieve webpage content.
   - Utilizes `BeautifulSoup` to parse the HTML content of the webpage.
   - Converts HTML tables on the webpage to Markdown format.
   - Extracts the title and main content from HTML, converting them to plain text using the `html2text` library.
   - Combines the title and content into a Markdown-formatted string.

2. **File Operations:**
   - Defines functions to sanitize filenames by removing invalid characters.
   - Generates a random filename using alphanumeric characters.
   - Ensures the existence of a target directory for saving Markdown files and creates the directory if it doesn't exist.
   - Writes Markdown content to a file in the specified directory, using the sanitized or randomly generated filename.
   - Prints a message indicating the successful download of the file.

3. **Main Functionality:**
   - The `getHttpResponse` function takes a URL, title ID, content ID, and cookie data as parameters.
   - Sends an HTTP GET request to the specified URL with the provided headers and cookies.
   - Extracts the title and HTML content from the response using the specified title and content IDs.
   - Converts the title and HTML content to plain text using `html2text`.
   - Determines the sanitized or randomly generated filename.
   - ==Combines the title and content and writes them to a Markdown file.==

4. **Usage:**

```python
from html2markdown import html2markdown
html2Markdown(arg1, arg2, arg3, arg4)
```
- Parameter 1: URL to be converted (cannot be empty).
- Parameter 2: ID of the title element in the website's HTML, such as `articleContentId` on CSDN (if empty, it will be randomly named).
- Parameter 3: ID of the content element in the website's HTML, such as `article_content` on CSDN (if empty, the entire page will be converted).
- Parameter 4: Cookie information in JSON format (if empty, no cookie will be used).

#### Demo

There is a `test.py` in the directory containing a sample for users to reference. When obtaining parameters, you can use the browser's F12 to inspect elements.

## 中文

### 介绍

本目录下由两个文件组成：
    - html2text.py 这个源自于github项目html2text，本人进行了简单重构，代码对于一些只用于python2的模块进行了修改，并且删除了一些无用的代码。
    - html2markdown.py 这个是核心代码，主要用于功能的实现

#### 功能

1. **网页抓取与Markdown转换：**
   - 使用`requests`库获取网页内容。
   - 使用`BeautifulSoup`解析网页的HTML内容。
   - 将网页中的HTML表格转换为Markdown格式。
   - 提取HTML的标题和主要内容，使用`html2text`库将它们转换为纯文本。
   - 将标题和内容组合成Markdown格式的字符串。

2. **文件操作：**
   - 定义了一些函数来清理文件名，去除无效字符。
   - 使用字母数字字符生成一个随机文件名。
   - 确保存在用于保存Markdown文件的目标目录，如果不存在则创建该目录。
   - 将Markdown内容写入指定目录的文件中，使用清理后或随机生成的文件名。
   - 打印一条消息，指示文件成功下载。

3. **主功能：**
   - `getHttpResponse`函数以URL、标题ID、内容ID和Cookie数据作为参数。
   - 使用指定的标题和内容ID向URL发送HTTP GET请求，并携带提供的头信息和Cookie。
   - 使用指定的标题和内容ID从响应中提取标题和HTML内容。
   - 使用`html2text`将标题和HTML内容转换为纯文本。
   - 确定清理后或随机生成的文件名。
   - ==将标题和内容组合并写入Markdown文件==。

4. **用法：**

```python
from html2markdown import html2markdown
html2Markdown(参数1，参数2，参数3，参数4)
```

- 参数1:所要转化的网址（不能为空）
- 参数2:网站中文章的title的id，如在CSDN中为articleContentId （为空值则随机命名）
- 参数3:网站中文章的内容的id，如在CSDN中为article_content (为空则转化整个页面)
- 参数4:Cookie信息，Json格式即可，会自动转为可以使用的格式。(为空则不使用cookie)


#### demo

目录下有一个test.py,里面有一个样例供大家使用，获取参数的时候可以使用浏览器F12去寻找。
