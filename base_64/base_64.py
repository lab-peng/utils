import base64


def text_to_file(text_path, file_path):  # provided we know what format the original text is of
    with open(text_path, 'rb') as fr:
        coded_string = fr.read()

    # create a writable pdf file and write the decoded message
    with open(file_path, 'wb') as fw:
        decoded_file = base64.decodebytes(coded_string)
        fw.write(decoded_file)


def file_to_text(file_path, text_path):
    with open(file_path, "rb") as pdf_file:
        encoded_string = base64.b64encode(pdf_file.read())

    with open(text_path, 'w') as fw:
        fw.write(str(encoded_string))


text_to_file('base64_texts/base64_1.txt', 'base64_files/1.png')
text_to_file('base64_texts/base64_2.txt', 'base64_files/2.pdf')
file_to_text('base64_files/苏拓估(2021)第00520号鸿文雅苑40幢805室.pdf', 'base64_texts/苏拓估(2021)第00520号鸿文雅苑40幢805室.txt')
