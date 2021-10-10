def ler_dados(arq_name):
    nomes = []
    bites = []
    try:
        with open(arq_name, "r") as dados:
            c = 0
            for item in dados.readlines():
                if c // 2 == 0:
                    nomes.append(item)
                
                elif c // 2 != 0:
                    nomes.append(item)
                
                c += 1
    except FileExistsError:
        print("Arquivo de dados não foi encontrado ou não existe")

    print(nomes)
    print(bites)

    
ler_dados("usuarios.txt")
