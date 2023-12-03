from html2markdown import html2markdown

# 中文
# html2Markdown(参数1，参数2，参数3，参数4)
# 参数1：所要转化的网址
# 参数2: 网站中文章的title的id，如在CSDN中为articleContentId
# 参数3：网站中文章的内容的id，如在CSDN中为article_content
# 参数4：Cookie信息，Json格式即可，会自动转为可以使用的格式。

# English
# html2Markdown(argument1, argument2, argument3, argument4)
# argument1: The URL to be converted.
# argument2: The id of the title in the website's HTML, e.g., "articleContentId" for CSDN.
# argument3: The id of the content in the website's HTML, e.g., "article_content" for CSDN.
# argument4: Cookie information in JSON format. It will be automatically converted to a usable format.


html2markdown("https://lunatic.blog.csdn.net/article/details/105257626","articleContentId","article_content","")

