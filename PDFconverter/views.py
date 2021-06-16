import os
import random
import re
import string

from django.contrib import messages
from django.http import FileResponse
from django.shortcuts import render
from PDFconverter.models import File
from docx2pdf import convert


def index_page(request):

    if request.FILES:
        files = request.FILES['docFile']

        file = File.objects.create(file=files)
        file.save()

        if file.get_file_size() > 13107200:
            messages.error(request, 'Размер файла слишком большой, максимум 12.5МБ!')
            os.remove(file.file.path)
            return render(request, 'PDFconverter/index_page.html')

        filename, file_extension = file.get_file_path_extension()

        pat = '^[a-zA-Z1-9{}]+$'.format(re.escape(string.punctuation))

        if file_extension != '.docx':
            messages.error(request, 'Документ должен быть в формате .docx!')
            os.remove(filename + file_extension)
            file.delete()
            return render(request, 'PDFconverter/index_page.html')

        if bool(re.match(pat, str(files))):
            convert(file.file.path)
            os.remove(file.file.path)
        else:
            symbol_list = '\ '
            symbol_list = symbol_list.replace(' ', '')
            file_path_list = filename.split(symbol_list)
            file_path_list[-1] = ''
            filename_new = ''
            for i in file_path_list:
                filename_new += i + '\ '
            filename_new = filename_new.replace(' ', '')
            filename_new += ''.join(random.choice(string.ascii_letters) for _ in range(16))
            os.rename(filename + file_extension, filename_new + file_extension)

            filename = filename_new

            convert(filename_new + file_extension)

            os.remove(filename_new + file_extension)

        file.delete()

        return FileResponse(open(filename + '.pdf', 'rb'), as_attachment=True)

    return render(request, 'PDFconverter/index_page.html')
