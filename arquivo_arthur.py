import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base


def menu():
    ("""
=== RH System ===

1 - Adicionar funcionário
2 - Consultar um funcionário 
3 - Atualizar os dados de um funcionário
4 - Excluir um uncionário
5 - Listar todos os funcionários
6 - Sair do sistema
 =>""")

#criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

#criando conexão com banco de dados
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

#criando tabela
Base = declarative_base()

class Funcionario(Base):
    
    def __init__(self, nome:str, idade:int, cpf:float, setor:str, funcao:str, salario:float, telefone:float):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone


#criando tabela no banco de dados
Base.metadata.create_all(bind=MEU_BANCO)

opcao = int(input("Digite a opção que deseja selecionar: "))

while True:
    menu()
    match opcao:
        case 1: 
    
            print("Solicitando dados para o usuário: ")
            nome = input("Digite seu nome: ")
            idade = int(input("Digite sua idade: "))
            cpf = float(input("Digite seu CPF: "))
            setor = str((input("Digite o seu setor: ")))
            funcao = str(input("Digite sua função: "))
            salario = float(input("Digite o valor do seu salário: "))
            telefone = float(input("Digite o seu telefone: "))



        case 2:
            