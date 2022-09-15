from os import system


class Sistema():

    def lerDados(self, nome_arq: str = "usuarios.txt") -> tuple[list, list]:
        """
        Recebe como parâmetro um nome de um arquivo e 
        retorna os nomes e os bytes contidos no arquivo.

        :param name: recebe por padrão 'usuarios.txt'
        :return: retona duas listas. Uma contem nome de usuário e a segunda os bytes.
        """
        nomes = []
        bites = []
        try:
            with open(nome_arq, "r") as dados:
                c = 0
                for item in dados.readlines():
                    lista = item.split()
                    nomes.append(lista[0])
                    bites.append(lista[-1])

        except FileNotFoundError:
            print("Arquivo não foi encontrado, tente novamente")
            exit()

        except FileExistsError:
            print("Arquivo de dados não existe")
            exit()

        return nomes, bites

    def bytesParaMegabytes(self, bytes: float = 0.0) -> float:
        """
        Recebe um valor em bytes e retorna esse valor em megabytes.

        :param bytes: por padrão recebe 0.0
        :return: retorna o valor em megabytes
        """
        bites = float(bytes)
        megaBytes = float(bites * (10 ** -6))
        return megaBytes

    def porcetagemDeUso(self, mega_bytes: list = []) -> tuple[list, float, float]:
        """
        Recebe uma lista com valores, soma e então retorna a porcentagem de cada valor segundo o total.

        :param mega_bytes: recebe uma lista com valores. Por padrão, uma lista vazia.
        :return: retorna uma lista com a porcetagem de cada valor, e o valor total da soma junto com a média.
        """
        mb = mega_bytes
        mb_total = 0
        porcetagem = []
        c = 0
        for item in mb:
            mb_total += item
            c += 1

        for item in mb:
            x = (item / mb_total) * 100
            porcetagem.append(x)

        media = mb_total / c
        return porcetagem, mb_total, media

    def formatarArquivo(self, name_arq: str = "relátorio.txt", user: list = [], bites: list = []) -> None:
        """
        Recebe o nome do arquivo de saida, a lista de nomes e bites utilizados por cada usuário
        e tem como saída a criação de um arquivo com o nome recebido

        :param name_arq: por padrão será "relátorio.txt"
        :param user: lista de usuarios
        :param bites: lista de bites ordenados
        :return: None
        """
        megaBytes = []

        for item in bites:
            x = self.bytesParaMegabytes(item)
            megaBytes.append(x)

        porcetagem, mb_total, media = self.porcetagemDeUso(
            mega_bytes=megaBytes)

        try:
            open(name_arq, "r")

        except FileNotFoundError:
            print("Arquivo não existe, vamos criar")
            open(name_arq, "w+")
            print(f"Arquivo '{name_arq}' foi criado com sucesso")

        with open(name_arq, "w+") as relatorio:
            relatorio.write("{:24}{} \n".format(
                "ACME inc.", "Uso de espaco em disco pelos usuarios"))
            relatorio.write("{}\n".format("--"*40))
            relatorio.write("{:6}{:18}{:>10}{:>15}\n".format(
                "id.", "Usuarios", "Espaco utilizado", "% do uso"))
            relatorio.write("\n")

            c = 0
            for item in user:
                relatorio.write("{:<5} {:<18}{:>10.2f} MB{:>16.2f}\n".format(
                    c+1, item, megaBytes[c], porcetagem[c]))

                c += 1

            relatorio.write("\n")
            relatorio.write(
                "Espaco total ocupado: {:.2f} MB\n".format(mb_total))
            relatorio.write(
                "Espaco medio ocupado: {:.2f} MB".format(media))

    def run(self) -> None:
        """
        Inicia o programa
        :return: None
        """
        system("cls")
        self.nomeArquivo = input(
            "Digite o nome do arquivo: (enter para padrão) ")
        if self.nomeArquivo == "":
            nomes, bites = self.lerDados("usuarios.txt")
        else:
            nomes, bites = self.lerDados(self.nomeArquivo)

        nome_relatorio = input(
            "Digite o nome do arquivo para saida: (enter para padrão) ")

        if nome_relatorio == "":
            self.formatarArquivo(user=nomes, bites=bites)
        else:
            self.formatarArquivo(name_arq=nome_relatorio,
                                 user=nomes, bites=bites)

        print("Arquivo de saida pronto, obrigado por utilizar este programa")


if __name__ == "__main__":
    sis = Sistema()
    sis.run()
