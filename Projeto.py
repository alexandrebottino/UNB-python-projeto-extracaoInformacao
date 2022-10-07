import pdfplumber
import os

os.chdir('C:\\Users\\alexa\\PycharmProjects\\pythonProject1\\artigos')

for artigo in os.listdir():
    pdf = pdfplumber.open(artigo)
    paginas = len(pdf.pages)

    pagina = pdf.pages[0]
    texto = pagina.extract_text()
    linhas = texto.split("\n")

    issn = ''
    doi = ''
    email = ''
    palavrasChave = ''
    titulo = ''
    autor = ''
    resumo = ''

    espacoEmBranco = 0
    auto = 0
    controleCopia = 0
    for linha in linhas:
        auto = auto + 1
        if linha != " ":
            if "ISSN" in linha:
                issn = linha
            elif "DOI" in linha:
                doi = linha
            elif "@" in linha:
                email = email + " - "+ linha
            elif "Palavras-chave" in linha:
                palavrasChave = palavrasChave + "" + linha
            elif ("ISSN" not in linha) and (auto <= 8):
                titulo = titulo + linha
            elif linha.istitle() and doi=="":
                    autor = autor + " " + linha
            else:
                espacoEmBranco = espacoEmBranco + 1
        if "Resumo" in linha:
            controleCopia = 1
        if "Palavras-chave" in linha:
                controleCopia = 0
                break
        elif (controleCopia == 1):
            resumo = resumo + "\n" +linha




    print("#####INFORMAÇÕES#####")
    print(issn)
    print("TITULO:" + titulo)
    print("Autor:" + autor)
    print("E-mails:" + str(email))
    print(doi)
    print(palavrasChave)
    print("Quantidade de páginas:" + str(paginas))
    print(resumo)
    print("\n")

