import os
import json

# Função para carregar os contatos de um arquivo JSON
def carregar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

# Função para salvar os contatos em um arquivo JSON
def salvar_contatos(nome_arquivo, contatos):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(contatos, arquivo, indent=4)

def listar_contato(email, contatos):
    os.system('clear')
    print('=========================================')
    if email in contatos:
        contato = contatos[email]
        print(f'E-mail pesquisado: {email}')
        print(f'Nome: {contato["nome"].capitalize()}')
        print(f'Idade: {contato["idade"]}')
        print(f'Peso: {contato["peso"]}')
        print(f'Telefone: {contato["telefone"]}')
        print(f'Cidade: {contato["cidade"]}')
        print(f'Estado: {contato["estado"]}')
        print('=========================================')

    else:
        print('Contato não existe.')

def listar_todos_contatos(contatos):
    os.system('clear')
    print('Lista de todos os contatos (E-mails):\n')
    for email in contatos.keys():
        print(email)
    print('=========================================')

def adicionar_contato(contatos):
    os.system('clear')
    print('Adicionar novo contato:')
    email = input('Digite o e-mail do contato: ')
    if email in contatos:
        print('Este e-mail já existe na lista de contatos.')
    else:
        nome = input('Digite o nome do contato: ')
        idade = input('Digite a idade do contato: ')
        telefone = input('Digite o telefone do contato: ')
        peso = input('Digite o peso do contato: ')
        estado = input('Digite o estado do contato: ')
        cidade = input('Digite a cidade do contato: ')

        # Adicionar novo contato ao dicionário
        contatos[email] = {
            'nome': nome,
            'idade': idade,
            'telefone': telefone,
            'peso': peso,
            'estado': estado,
            'cidade': cidade.strip(','),  # Remover vírgula no final da cidade
        }
        print('Contato adicionado com sucesso!')
        salvar_contatos('contatos.json', contatos)

def main():
    # Carregar contatos a partir de um arquivo JSON
    contatos = carregar_contatos('contatos.json')
    
    while True:
        print('[1] Pesquisar')
        print('[2] Listar todos os contatos (por e-mail)')
        print('[3] Adicionar novo contato')
        print('[4] Sair')
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            email_pesquisa = input("Digite o e-mail do contato (ou 's' para sair): ")
            if email_pesquisa == 's':
                break
            listar_contato(email_pesquisa, contatos)
        elif escolha == '2':
            listar_todos_contatos(contatos)
        elif escolha == '3':
            adicionar_contato(contatos)
        elif escolha == '4':
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()
