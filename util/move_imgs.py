import os
import re
import shutil

root = "..\\class\\Investment\\"
books = os.scandir(root)
pattern =  r'!\[.*?\]\((.*?)\)|!\[\[(.*?)\]\]'

def format_and_add_resource_prefix(match):
    if match.group(1) and "resource" in match.group(1):
        return f"![]({match.group(1)})"
    if match.group(1):
        return f'![](resource/{match.group(1)})'
    return f'![](resource/{match.group(2)})'

for book in (v for v in list(books) if v.is_dir()):
    notes = os.listdir(root+book.name)
    print(book.name)
    os.makedirs(root+book.name+"\\resource", exist_ok=True)
    content = ''
    for n in notes:
        if n == "resource": continue
        with open(root+book.name+"\\"+n, "r", encoding="utf8") as f:
            content = f.read()
            imgs = (v[0] if v[0] else v[1] for v in re.findall(pattern, content))
        if not imgs: continue


        for img in imgs:
            if img[:4] == "http" or "resource" in img: continue
            img = img.replace("%20", " ").strip()
            dest = root+book.name + f"\\resource\\{img}"
            if os.path.exists(dest): continue

            try:
                shutil.move("..\\..\\"+img, dest)
            except FileNotFoundError:
                shutil.move("..\\..\\finance\\img\\"+img, dest)
            except Exception as e:
                print(e, book.name)
                raise e
        
        content = re.sub(pattern, format_and_add_resource_prefix, content)
        with open(root+book.name+"\\"+n, "w", encoding="utf8") as f:
            f.write(content)


