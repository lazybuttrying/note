import os
import re
import shutil

root = "..\\class\\Corporate Finance\\"
books = os.scandir(root)
pattern =  r'!\[.*?\]\((.*?)\)|!\[\[(.*?)\]\]'

def format_and_add_resource_prefix(match):
    if match.group(1):
        if ("resource" in match.group(1) or "http" in match.group(1)):
            return f"![]({match.group(1).replace(' ', '%20')})"
        else:
            return f'![](resource/{match.group(1).replace(" ", "%20")})'
    return f'![](resource/{match.group(2).replace(" ", "%20")})'

# for book in (v for v in list(books) if v.is_dir()):
#     notes = os.listdir(root+book.name)
#     print(book.name)
#     if book.name == "resource": continue
#     os.makedirs(root+book.name+"\\resource", exist_ok=True)

notes = os.listdir(root)
content = ''

for n in notes:
    if n == "resource": continue
    with open(root+"\\"+n, "r", encoding="utf8") as f:
        content = f.read()
        imgs = (v[0] if v[0] else v[1] for v in re.findall(pattern, content))
    if not imgs: continue


    for img in imgs:
        if img[:4] == "http" or "resource" in img: continue
        img = img.replace("%20", " ").strip()
        dest = root + f"\\resource\\{img}"
        if os.path.exists(dest): continue

        try:
            shutil.move("..\\..\\"+img, dest)
        except FileNotFoundError:
            shutil.move("..\\"+img, dest)
        except Exception as e:
            print(e,)
            raise e
    
    content = re.sub(pattern, format_and_add_resource_prefix, content)
    with open(root+"\\"+n, "w", encoding="utf8") as f:
        f.write(content)


