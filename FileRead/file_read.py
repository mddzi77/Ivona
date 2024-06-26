import fitz


def read_pdf(file_path, text_input):
    try:
        byte_string = file_path
        proper_path = byte_string.decode('utf-8')
        doc = fitz.open(proper_path)
        pdf_text = ""
        for page_num in range(doc.page_count):
            page = doc[page_num]
            pdf_text += page.get_text()
        text_input.text = pdf_text
    except Exception as e:
        text_input.text = f"Error: {str(e)}"
