from PyPDF2 import PdfReader


def read_my_pdf():

    path = "C:/users/workcarminatti/Downloads/arquivo.pdf"

    reader = PdfReader(path)
    page = reader.pages[0]
    text = page.extract_text()
    lista_itens = text.split("\n")


    # Descobrindo posição do valor (cod barra)
    for idx, values in enumerate(lista_itens):
        idx, values

    values = []

    values.append(lista_itens[57])
    values.append(lista_itens[59])

    return values


def get_date():
    dt = read_my_pdf()
    split_date = dt[1].split(" ")



    return split_date[0]


codigo = read_my_pdf()
vencimento = get_date()
