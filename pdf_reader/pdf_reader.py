# ---------------------------------
# PDF Reader Project
# ---------------------------------

import PyPDF2

print("===== PDF READER =====")

# Open PDF File
pdf_file = open("sample.pdf", "rb")

# Create PDF Reader Object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Total Pages
total_pages = len(pdf_reader.pages)

print(f"\nTotal Pages: {total_pages}")

# Read Pages
for page_num in range(total_pages):

    page = pdf_reader.pages[page_num]

    text = page.extract_text()

    print(f"\n===== PAGE {page_num + 1} =====\n")

    print(text)

# Close File
pdf_file.close()
