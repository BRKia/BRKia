from translation import trans

with open("text.txt", encoding="utf-8") as f:
    content = f.read()
content = trans(content)

with open("Chi.py", encoding="utf-8") as f:
    content = f.read() + content

# print(content)
exec(content)