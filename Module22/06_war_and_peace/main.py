import re
import zipfile
from collections import Counter, OrderedDict

archive = zipfile.ZipFile('voyna-i-mir.zip', 'r')
archive.extractall()
archive.close()

pattern = r'[А-Яа-яA-Za-z]'

with open('voyna-i-mir.txt', 'r', encoding='utf8') as book:
    book_txt = book.read()

letters = re.findall(pattern, book_txt, flags=re.MULTILINE)
counts = Counter(letters)
# sorted(counts.items(), key=lambda x: x[1], reverse=True)
y = OrderedDict(counts.most_common())

# print(counts)
# for i in counts:
#     print(i, counts[i])

# print(y)
for i in y:
    print(i, y[i])
