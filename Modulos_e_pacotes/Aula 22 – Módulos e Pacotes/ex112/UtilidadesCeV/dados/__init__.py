cores = {"vermelho" : "\033[31m",
        "fim" : "\033[m"
}

def LeiaDinheiro(entrada):
    while True:
        analise = input(entrada).replace(",",".").strip()
        if not analise or analise.isalpha() or ' ' in analise:
            print(f'{cores["vermelho"]}ERRO! \"{analise}\" não é válido{cores["fim"]}')  
        else:
            break
    return float(analise)