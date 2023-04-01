# PDFconverter
Веб-сайт для преобразования файлов .docx в. pdf

## Прежде всего:

Клонируйте репозиторий и перейдите в установленную папку:
```
git clone https://github.com/Ryize/PDFconverter.git
cd PDFconverter
```

Установите requirements:
```
pip3 install -r requirements.txt
```

Соберите statics и выполните migrations:
```
python3 manage.py collectstatic
python3 manage.py migrate
```

Запустите проект:
```
python3 manage.py runserver
```

> Технологии, использованные в проекте: Python3, Django, docx2pdf, os, random, re, string.
