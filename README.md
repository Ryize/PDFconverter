# PDFconverter
A website for converting files .docx to. pdf

## Deploy locally:

Clone the repository and go to installed folder:
```
git clone https://github.com/Ryize/PDFconverter.git
cd PDFconverter
```

Install requirements:
```
pip3 install -r requirements.txt
```

Run the bot:
```
python3 manage.py collectstatic
python3 manage.py migrate
python3 manage.py runserver
```

> Technologies used in the project: Python3, Django, docx2pdf, os, random, re, string.
