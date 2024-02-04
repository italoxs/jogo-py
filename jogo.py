import random


class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"

    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = random.randint(
            self.get_nivel() * 2, self.get_nivel() * 4
        )  # base no nivel
        alvo.receber_ataque(dano)
        print(
            f"\n{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!\n"
        )


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"

    def ataque_escpecial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        alvo.receber_ataque(dano)
        print(
            f"\n{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!\n"
        )


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"


class Jogo:
    """Classe orquestradora do jogo"""

    def __init__(self) -> None:
        self.heroi = Heroi(nome="Heroi", vida=100, nivel=5, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Morcego", vida=100, nivel=5, tipo="Voador")

    def iniciar_batalha(self):
        """Fazer a gestão da batalha em turnos"""
        print("Iniciando batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhe dos personagens do Heroi:")
            print(self.heroi.exibir_detalhes())
            print("\nDetalhe dos personagens do Inimigo:")
            print(self.inimigo.exibir_detalhes())

            input("\nPressione Enter para atacar...")
            escolha = input("\nEscolha\n1 - Ataque Normal\n2 - Ataque Especial\n")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_escpecial(self.inimigo)
            else:
                print("Escolha inválida.\nEscolha novamente.")

            if self.inimigo.get_vida() > 0:
                # Inimigo ataca o heroi
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())
            print("\nParábens, você venceu a batalha")
        else:
            print(self.inimigo.exibir_detalhes())
            print(self.heroi.exibir_detalhes())
            print("\nVocê foi derrotado!")


# Criar instancia do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()
