# BIBLIOTECAS
import requests
import os
import sys

nome = input('\n\nQual NOME do paciente: ')

def consumir_api():

    r = requests.get('http://127.0.0.1:8000/pacientes')

    # Convertendo dados
    data = r.json()

    for clinica in data:
        if clinica['nome'] == nome :
            print('\n\nID: ',clinica['id_paciente'])
            print('NOME: ',clinica['nome'])
            print('DATA DE NASCIMENTO: ',clinica['data_nascimento'])
            print('RG: ',clinica['rg'])
            print('ENDEREÇO: ',clinica['endereco'])
            print('Nº DA CASA: ',clinica['numero_endereco'])
            print('BAIRRO: ',clinica['bairro_endereco'])
            print('CEP: ',clinica['cep'])
            print('DATA DO CADASTRO: ',clinica['data_cadastro'],'\n\n')


if __name__ == '__main__':
    consumir_api()
    