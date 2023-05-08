import pypdf

if __name__ == '__main__':
    with open('Working_Business_Proposal.pdf', 'rb') as f:
        pdf_reader = pypdf.PdfReader(f)
        print(len(pdf_reader.pages))
        page_one = pdf_reader.pages[0]
        page_one_text = page_one.extract_text()
        print(page_one_text)

        pdf_writer = pypdf.PdfWriter()
        pdf_writer.add_page(page_one)

        with open('Some_BrandNew_Doc.pdf', 'wb') as pdf_output:
            pdf_writer.write(pdf_output)
