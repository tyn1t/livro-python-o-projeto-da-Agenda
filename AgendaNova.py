import sys
import pickle 
from functools import total_ordering


def nulo_ou_vazio(texto): 
    return texto is None or not texto.strip()
def valida_faixa_inteiro(pergunta, inicio, fim, padrao=None): 
    while True: 
        try: 
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada) and padrao is None:
                entrada = padrao 
            valor = int(entrada)
            if inicio <= valor <= fim: 
                return valor
        except ValueError:
            print(f"Valor inválido,favor digitar entre {inicio} e {fim}")
        if inicio > valor or valor > fim: 
                print(f"Valor inválido,favor digitar entre {inicio} e {fim}")
       
def valida_faixa_inteiro_ou_branco(pergunta,inicio,fim): 
    while True: 
        try: 
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada): 
                return None
            valor = int(entrada) 
            if inicio <= valor <= fim: 
               return valor 
        except ValueError: 
            print(f"Valor invalido, favor digitar rntre {inicio} e {fim}")
        if inicio > valor or valor > fim: 
                print(f"Valor inválido,favor digitar entre {inicio} e {fim}")
class ListaUnica:

    def __init__(self, elem_class): 
        self.lista = []
        self.elem_class = elem_class 

    def __len__(self): 
        return len(self.lista)

    def __iter__(self): 
        return iter(self.lista)

    def __getitem__(self,p):
        return self.lista[p]

    def indeceValito(self,i): 
        return i >= 0 and i < len(self.lista)

    def adiciona(self,elem): 
        if self.pesquisa(elem) == -1: 
            self.lista.append(elem)

    def remove(self, elem): 
        self.lista.remove(elem)

    def pesquisa(self,elem):
        self.verifica_tipo(elem)
        try:
            return self.lista.index(elem)
        except ValueError: 
            return -1

    def verifica_tipo(self, elem): 
        if type(elem) != self.elem_class: 
            raise TypeError("Tipo inválito")
        
    def ordena(self, chave=None):
        self.lista.sort(key=chave)


@total_ordering
class Nome:

    def __init__(self, nome): 
        self.nome = nome 

    def __str__(self):
        return self.nome
    def __repr__(self):
        return f"<Class {type(self).__name__} em 0x{id(self):x} Nome:{self.__nome} Chave:{self.__chave}>"

    def __eq__(self, outro):
        return self.nome == outro.nome
    
    def __lt__(self, outro):
        return self.nome < outro.nome

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, valor): 
        if nulo_ou_vazio(valor): 
            raise ValueError("Nome não pode ser nul nem em branco")
        self.__nome = valor 
        self.__chave = Nome.CriaChave(valor)
    @property
    def chave(self):
        return self.__chave
    
    @staticmethod 
    def CriaChave(nome): 
        return nome.strip().lower()



@total_ordering
class TipoTelefone:
    def __init__(self,tipo):
        self.tipo = tipo
    def __str__(self):
        return f"({self.tipo})"
    def __eq__(self, outro):
        if outro is None:
            return False 
        return self.tipo == outro.tipo 
    
    def __lt__(self,outro): 
        return self.tipo < outro.tipo  

class Telefone:
    def __init__(self,numero, tipo=None):
        self.numero = numero
        self.tipo = tipo 

    def __str__(self): 
        if self.tipo is not None:
            tipo = self.tipo 
        else: 
            tipo = ""
        return f"{self.numero} {tipo}"

    def __eq__(self, outro):
        return self.numero == outro.numero and ( (self.tipo == outro.tipo) or (self.tipo is None or outro.tipo is None)) 

    @property
    def numero(self): 
        return self.__numero
    @numero.setter
    def numero(self, valor):
        if nulo_ou_vazio(valor):
            raise ValueError("Numero não pode ser None ou em branco")
        self.__numero = valor 

class Telefones(ListaUnica):
    def __init__(self): 
        super().__init__(Telefone)
class TiposTelefone(ListaUnica):
    def __init__(self): 
        super().__init__(TipoTelefone)
class DadoAgenda: 
    def __init__(self,nome):
        self.nome = nome 
        self.telefones = Telefones()
    
    @property 
    def nome(self): 
        return self.__nome 
    @nome.setter
    def nome(self, valor): 
        if type(valor) != Nome: 
            raise TypeError("nomedeve ser uma instância da classe Nome")
        self.__nome = valor 
    def pesquisaTelefone(self, telefone): 
        posicao = self.telefones.pesquisa(Telefone(telefone))
        if posicao == -1: 
            return None 
        else: 
            return self.telefones[posicao]

class Agenda(ListaUnica): 
    def __init__(self):
        super().__init__(DadoAgenda)
        self.tiposTelefone = TiposTelefone()
    def adicionaTipo(self, tipo):
        self.tiposTelefone.adiciona(TipoTelefone(tipo))
    def pesquisaNome(self, nome): 
        if type(nome) == str: 
            nome = Nome(nome)
        for dados in self.lista:
            if dados.nome == nome: 
                return dados 
        else: 
            return None 
    def ordena(self):
        super().ordena(lambda dado: str(dado.nome))

class Menu: 
    def __init__(self):
        self.opcoes = [["sair",None]]
    def adicionaopcoes(self, nome, funcao): 
        self.opcoes.append([nome, funcao])
    def exibe(self): 
        print("====")
        print("Menu")
        print("====")
        for i ,opcoes in  enumerate(self.opcoes): 
            print(f"[{i}] - [{opcoes[0]}]")
        print()
    def execute(self): 
        while True: 
            self.exibe()
            escolha = valida_faixa_inteiro("Excolha uma opção:",0,len(self.opcoes)-1)
            if escolha == 0: 
                break 
            self.opcoes[escolha][1]()       
         



class AppAgenda: 
    @staticmethod
    def pede_nome(): 
        return input("Nome:")
    @staticmethod
    def pede_telefone(): 
        return input("Telefone:")
    @staticmethod 
    def mostra_dados(dados):
        print(f"Nome:{dados.nome}")
        for telefone in dados.telefones:
            print(f"Telefone:{telefone}")
        print()
    @staticmethod
    def mostra_dados_telefone(dados):
        print(f"Nome:{dados.nome}")
        for l , Telefone in enumerate(dados.telefones):
            print(f"{l} - Telefone: {Telefone}")
        print()
    @staticmethod 
    def pede_nome_arquivo():
        return input("Nome do arquivo")
    def __init__(self): 
        self.agenda = Agenda()
        self.agenda.adicionaTipo("Celular")
        self.agenda.adicionaTipo("Residência")
        self.agenda.adicionaTipo("Trabalho")
        self.agenda.adicionaTipo("Fax")
        self.menu = Menu()
        self.menu .adicionaopcoes("Novo",self.novo)
        self.menu .adicionaopcoes("Altera",self.Altera)
        self.menu .adicionaopcoes("Apaga",self.apaga)
        self.menu .adicionaopcoes("Lista",self.lista)
        self.menu .adicionaopcoes("Grava",self.grava)
        self.menu .adicionaopcoes("le",self.le)
        self.menu .adicionaopcoes("Ordena",self.ordena)
        self.ultimo_nome = None

    def pede_tipo_telefone(self, padrao=None): 
        for i, tipo in enumerate(self.agenda.tiposTelefone):
            print(f"{i} - {tipo}",end=None)
        t = valida_faixa_inteiro("Tipo:",0, len(self.agenda.tiposTelefone)-1,padrao)
        return self.agenda.tiposTelefone[t]

    def pesquisa(self,nome): 
        dado = self.agenda.pesquisaNome(nome)
        return dado 

    def novo(self): 
        novo = AppAgenda.pede_nome()
        if nulo_ou_vazio(novo):
            return 
        nome = Nome(novo)
        if self.pesquisa(nome) is not None: 
            print("Nome: já existi")
            return 
        registro = DadoAgenda(nome)
        self.menu_telefones(registro)
        self.agenda.adiciona(registro)
    def apaga(self): 
        if len(self.agenda) == 0: 
            print("Agenda vazia nada  a  apaga")
        nome = AppAgenda.pede_nome()
        if nulo_ou_vazio(nome): 
            return 
        p = self.pesquisa(nome)
        if p is not None: 
            self.agenda.remove(p)
            print(f"Apagado.. A agenda agora possui apenas:{len(self.agenda)} resgistro")
        else: 
            print(f"Nome não encontrado.")
    
    def Altera(self): 
        if len(self.agenda) == 0: 
            print(f"Agenda esta vazia, nad apara altera")
        nome = AppAgenda.pede_nome()
        if nulo_ou_vazio(nome):
            return 
        p = self.pesquisa(nome)
        if p is not None: 
            print("Encontrado...")
            AppAgenda.mostra_dados(p)
            print("Digite enter caso não queira altera nome")
            novo = AppAgenda.pede_nome()
            if not nulo_ou_vazio(novo): 
                p.nome =Nome(novo)
                self.menu_telefones(p)
        else:
            print("Nome não encontrado!")
    def menu_telefones(self,dados): 
        while True: 
            print("Editando telefone")
            AppAgenda.mostra_dados_telefone(dados)
            if len(dados.telefones) > 0: 
                print("[A] -ALTERA  [D] - APAGA]",end="")
            print("[N] - NOVO  [S] - SAIR")
            operacao = input("Escolha um operação:")
            operacao = operacao.lower()
            if operacao not in ["a","d","n","s"]:
                continue 
            if operacao == 'a' and len(dados.telefones) > 0:
                self.altera_telefones(dados)
            elif operacao == 'd' and len(dados.telefones) > 0: 
                self.apaga_telefone(dados)
            elif operacao == 'n': 
                self.novo_telefone(dados)
            elif operacao == "s": 
                break 
    def novo_telefone(self,dados): 
        telefone = AppAgenda.pede_telefone()
        if nulo_ou_vazio(telefone): 
            return 
        if dados.pesquisaTelefone(telefone) is not None:
            print("Telefone já existe")
        tipo = self.pede_tipo_telefone()
        dados.telefones.adiciona(Telefone(telefone,tipo))
    
    def apaga_telefone(self, dados):
        t = valida_faixa_inteiro_ou_branco("Digite a posiçao do número a apaga, enter para sair:",0, len(dados.telefones)-1)
        if t is None: 
            return 
        dados.telefones.remove(dados.telefones[t])
    
    def altera_telefones(self, dados):
        t = valida_faixa_inteiro_ou_branco(
            "Digite a posiçao do numero a altera, enter para sair:",
            0,len(dados.telefones)-1)
        if t is None: 
            return 
        telefone = dados.telefones[t]
        print(f"Telefone:{telefone}")
        print("digite enter caso não queira alterar o número")
        novotelefone = AppAgenda.pede_telefone()
        if not nulo_ou_vazio(novotelefone): 
            telefone.numero = novotelefone
        print("Digeti enter caso não quer altera o tipo")
        telefone.tipo = self.pede_tipo_telefone(
            self.agenda.tiposTelefone.pesquisa(telefone.tipo))
    
    def lista(self):
        print("Agenda")
        print("-"* 60)
        for e in self.agenda: 
            AppAgenda.mostra_dados(e)
        print("-"*60)

    def le(self, nome_arquivo=None):
        if nome_arquivo is None: 
            nome_arquivo =AppAgenda.pede_nome_arquivo()
        if nulo_ou_vazio(nome_arquivo): 
            return 
        with open(nome_arquivo, "rb") as arquivos:
            self.agenda = pickle.load(arquivos)
        self.ultimo_nome = nome_arquivo 

    def ordena(self): 
        self.agenda.ordena()
        print("Agenda ordenada")

    def grava(self):
        if self.ultimo_nome is not None:
            print(f"Ultimo nome utilizado foi '{self.ultimo_nome}'")
            print("Digita enter caso queira utilizar o mesmo nome")
        nome_arquivo = AppAgenda.pede_nome_arquivo()
        if nulo_ou_vazio(nome_arquivo): 
            if self.ultimo_nome is not None: 
                nome_arquivo = self.ultimo_nome 
            else: 
                return 
        with open(nome_arquivo,'wb') as arquivo: 
            pickle.dump(self.agenda,arquivo)
    
    def execute(self): 
        self.menu.execute()


if __name__=="__main__":
    app = AppAgenda()
    if len(sys.argv) > 1: 
        app.lê(sys.argv[1])
    app.execute()



