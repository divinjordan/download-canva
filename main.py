import requests
import re


url = "https://export-download.canva.com/Sd6po/DAFV5uSd6po/7/0-1007266014.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJHKNGJLC2J7OGJ6Q%2F20221226%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221226T150237Z&X-Amz-Expires=32857&X-Amz-Signature=b56db184f52522dfbda1140b236240ce14dc8ea59c820ab0397e5cd413da4d0e&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27Dossier%2520Inter-Progress.pdf&response-expires=Tue%2C%2027%20Dec%202022%2000%3A10%3A14%20GMT"

result = requests.get(url)

file = open('result.pdf','wb')
file.write(result.content)