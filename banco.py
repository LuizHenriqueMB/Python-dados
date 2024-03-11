import random
import locale
import csv
import pandas as pd
from faker import Faker

# Inicialize o Faker
fake = Faker('pt_BR')

# Define a formatação de moeda para o Real brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Dicionário de marcas de carros de luxo com modelos e preços
marcas_carros = {
    "Mercedes-Benz": {
        "modelos": ["Classe S", "Classe E", "Classe C", "AMG GT"],
        "precos": [400000, 250000, 150000, 600000]
    },
    "BMW": {
        "modelos": ["Série 7", "Série 5", "Série 3", "M8"],
        "precos": [450000, 300000, 180000, 700000]
    },
    "Audi": {
        "modelos": ["A8", "A6", "A4", "R8"],
        "precos": [420000, 280000, 160000, 650000]
    },
    "Lamborghini": {
        "modelos": ["Aventador", "Huracan", "Urus"],
        "precos": [2000000, 1500000, 800000]
    },
    "Ferrari": {
        "modelos": ["812 Superfast", "F8 Tributo", "Portofino"],
        "precos": [2500000, 2000000, 1800000]
    },
    "Porsche": {
        "modelos": ["911", "Panamera", "Cayenne"],
        "precos": [500000, 350000, 250000]
    },
    "Rolls-Royce": {
        "modelos": ["Phantom", "Ghost", "Cullinan"],
        "precos": [1000000, 800000, 900000]
    },
    "Bentley": {
        "modelos": ["Continental GT", "Flying Spur", "Bentayga"],
        "precos": [800000, 700000, 750000]
    },
    "Jaguar": {
        "modelos": ["XF", "XJ", "F-Type"],
        "precos": [300000, 400000, 200000]
    },
    "Lexus": {
        "modelos": ["LS", "RX", "LC"],
        "precos": [350000, 280000, 320000]
    },
    "Aston Martin": {
        "modelos": ["DB11", "Vantage", "DBS Superleggera"],
        "precos": [900000, 800000, 1000000]
    },
    "Koenigsegg": {
        "modelos": ["Regera", "Jesko", "Gemera"],
        "precos": [3000000, 2800000, 2600000]
    },
    "Ford": {
        "modelos": ["Mustang", "GT", "F-150"],
        "anos_fabricacao": [2022, 2021, 2023],
        "precos": [70000, 500000, 40000]
    },
    "Dodge": {
        "modelos": ["Challenger", "Charger", "Viper"],
        "anos_fabricacao": [2022, 2021, 2023],
        "precos": [60000, 65000, 120000]
    },
    "Chevrolet": {
        "modelos": ["Corvette", "Camaro", "Silverado"],
        "anos_fabricacao": [2022, 2021, 2023],
        "precos": [60000, 50000, 40000]
    },
    "Nissan": {
        "modelos": ["GT-R", "370Z"],
        "anos_fabricacao": [2022, 2021],
        "precos": [115000, 30000]
    }
}

# Lista de cores de carros
cores = ["Preto", "Branco", "Prata", "Azul", "Vermelho", "Cinza", "Verde", "Amarelo"]

# Função para gerar nome de comprador fictício
def gerar_nome_comprador():
    return fake.name()  # Usar o faker para gerar um nome de comprador aleatório

# Função para gerar data de nascimento aleatória
def gerar_data_nascimento():
    dia = random.randint(1, 28)
    mes = random.randint(1, 12)
    ano = random.randint(1950, 2005)
    return f"{dia:02d}/{mes:02d}/{ano}"

# Função para gerar CPF aleatório
def gerar_cpf():
    return f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}"

# Função para gerar comprovante de residência fictício
def gerar_endereco():
    numero = random.randint(100, 9999)
    rua = random.choice(["Rua A", "Rua B", "Rua C", "Rua D", "Rua E"])
    estado = random.choice(["SP", "RJ", "MG", "DF", "BA"])
    return f"{rua}, {numero}, {estado}"

# Criação da base de dados
base_de_dados = []

for _ in range(200):
    marca = random.choice(list(marcas_carros.keys()))
    modelos = marcas_carros[marca]["modelos"]
    precos = marcas_carros[marca]["precos"]
    modelo = random.choice(modelos)
    preco = precos[modelos.index(modelo)]
    cor = random.choice(cores)
    nome_comprador = gerar_nome_comprador()  # Usar o faker para gerar um nome de comprador aleatório
    data_nascimento = gerar_data_nascimento()
    cpf = gerar_cpf()
    endereco = gerar_endereco()
    preco_pago = round(preco * random.uniform(0.8, 1.2), 2) # Preço pago pode variar até 20% do preço original
    
    registro = {
        "Marca": marca,
        "Modelo": modelo,
        "Preço": locale.currency(preco, grouping=True),
        "Cor": cor,
        "Nome do Comprador": nome_comprador,
        "Data de Nascimento": data_nascimento,
        "CPF": cpf,
        "Endereço": endereco,
        "Preço Pago": locale.currency(preco_pago, grouping=True)
    }
    
    base_de_dados.append(registro)

# Escrever os registros em um arquivo CSV
with open('registros.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=base_de_dados[0].keys())
    writer.writeheader()
    writer.writerows(base_de_dados)

# Ler o arquivo CSV com pandas
df = pd.read_csv('registros.csv')

# Gerar tabela HTML
html_table = df.to_html(index=False)

# Escrever tabela HTML em um arquivo HTML
with open('registros.html', 'w', encoding='utf-8') as file:
    file.write(html_table)

print("Arquivo CSV e HTML gerados com sucesso!")