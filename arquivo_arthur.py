import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base


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
        
