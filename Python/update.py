#!python
import sys # 한글 출력하기 위해서
import codecs # 한글 출력하기 위해서
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print("Content-Type: text/html;charset=utf-8\r\n")
import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r', encoding='utf-8').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'
print('''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>WEB1 - html</title>
</head>
<body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
        {listStr}
    </ol>
    <a href="create.py">create</a>
    <form action="process_update.py" method="post">
        <input type="hidden" name="pageId" value="{form_default_title}">
        <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
        <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></p>
        <p><input type="submit"></p>
    </form>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=view.getList(), form_default_title=pageId , form_default_description=description))
