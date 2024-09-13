import os
import re
import shutil

root = "temp\\book\\"
books = os.scandir(root)
pattern =  r'!\[.*?\]\((.*?)\)|!\[\[(.*?)\]\]'


for book in (v for v in list(books) if v.is_dir()):
    notes = os.listdir(root+book.name)
    print(book.name)
    os.makedirs(root+book.name+"\\resource", exist_ok=True)
    for n in notes:
        if n == "resource": continue
        with open(root+book.name+"\\"+n, "r", encoding="utf8") as f:
            imgs = re.findall(pattern, f.read())

        for img in (v[0] if v[0] else v[1] for v in imgs):
            if img[:4] == "http": continue
            img = img.replace("%20", " ").strip()
            dest = root+book.name + f"\\resource\\{img}"
            if os.path.exists(dest): continue

            try:
                shutil.move(img, dest)
            except FileNotFoundError:
                shutil.move("재무금융\\"+img, dest)
            except Exception as e:
                print(e, book.name)
                raise e
