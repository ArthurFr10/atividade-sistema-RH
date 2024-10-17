import os 
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

os.system("cls || cleas")

def menu():
("""
=== RH System ===

1 - Adicionar funcionário
2 - Consultar um funcionário 
3 - Atualizar os dados de um funcionário
4 - Excluir um uncionário
5 - Listar todos os funcionários
6 - Sair do sistema
""")
      
