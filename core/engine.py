class Engine:
    def __init__(self, realm):
        self.realm = realm
        self.rodando = True

    def loop(self):
        while self.rodando:
            print(f"\nRealm ativo: {self.realm.nome}")
            print(self.realm.descricao)

            for i, acao in enumerate(self.realm.acoes):
                print(f"{i} - {acao.nome}")

            escolha = input("Escolha uma ação (q para sair): ")

            if escolha.lower() == "q":
                self.rodando = False
                break

            try:
                acao = self.realm.acoes[int(escolha)]
                if acao.pode_executar(self):
                    acao.executar(self)
                else:
                    print("Ação não disponível.")
            except:
                print("Entrada inválida.")
