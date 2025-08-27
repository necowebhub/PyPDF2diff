from PyPDF2 import PdfReader, PdfWriter

file1 = "StampsNEW.pdf"
file2 = "Stamps.pdf"
output = "diff_pages.pdf"

# Читаем оба файла
pdf1 = PdfReader(file1)
pdf2 = PdfReader(file2)

# Создаем множество текстов страниц из первого файла
pages_text_file1 = {page.extract_text() for page in pdf1.pages}

writer = PdfWriter()

# Проверяем каждую страницу второго файла
for page in pdf2.pages:
    text = page.extract_text()
    if text not in pages_text_file1:  # если текста нет в file1, добавляем в итог
        writer.add_page(page)

# Сохраняем разницу
with open(output, "wb") as f:
    writer.write(f)

print("Готово! Отличающиеся страницы сохранены в diff_pages.pdf")
