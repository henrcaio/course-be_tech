import os
import requests
from datetime import datetime

# DB para ser preenchida com Nome, Sobrenome, CPF, Data de Nascimento, Telefone e Endereço
db = []


# Função para receber a data de nascimento e armazenar no formado adequado
def birthdate() -> datetime:
    date_string = input(
        "Digite a data de nascimento do funcionário no formato DD/MM/YYYY: "
    )
    birthdate = datetime.strptime(date_string, "%d/%m/%Y")
    return birthdate


# Função para calcular dias até próximo aniversário
def days_to_next_bday(birthdate: datetime) -> int:
    today = datetime.today()
    bday = birthdate.replace(year=today.year)

    # Caso já tenha passado o aniversário esse ano
    if bday < today:
        y = today.year + 1
        bday = bday.replace(year=y)
        print(bday)
        delta = bday - today
    else:
        delta = bday - today

    return delta.days


# Função disponibilizada pelo professor!
def recebe_cep_retorna_endereco(cep: str) -> list:
    cep = cep.replace("-", "").replace(".", "").replace(" ", "")
    if len(cep) == 8:
        link = f"https://viacep.com.br/ws/{cep}/json/"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        uf = dic_requisicao["uf"]
        cidade = dic_requisicao["localidade"]
        bairro = dic_requisicao["bairro"]
        logradouro = dic_requisicao["logradouro"]
        # Adendo para retornar endereço formatado
        endereco = []
        endereco.append(logradouro)
        endereco.append(bairro)
        endereco.append(cidade)
        endereco.append(uf)
        endereco_formatado = " ".join(endereco)
        return [endereco_formatado]
    else:
        raise Exception("CEP Inválido")


# Esta função permite a entrada dos dados do funcionário para incluí-lo na base de dados
def create():
    new_employee = []
    new_employee.append(input("Digite o nome do funcionário: ").lower())
    new_employee.append(input("Digite o sobrenome do funcionário: ").lower())
    new_employee.append(input("Digite a profissão do funcionário: ").lower())
    new_employee.append(
        input("Digite o número do CPF do funcionário (sem pontos ou traços): ")
    )
    date = birthdate()
    new_employee.append(date)
    new_employee.append(
        input(
            "Digite o número de telefone do funcionário (com DDD e sem traços ou parênteses): "
        )
    )

    # Recebendo CEP e chamando função para gerar endereço
    cep = input("Digite o CEP do funcionário (sem pontos ou traços): ")
    endereco = recebe_cep_retorna_endereco(cep)
    new_employee.append(endereco)

    db.append(new_employee)


# Esta função permite a leitura dos dados via pesquisa por nome ou profissão
def read():
    found = False
    search = input("Digite um nome ou profissão: ").lower()
    for person in db:
        if search in person:
            os.system("cls")
            found = True
            days = days_to_next_bday(person[4])

            print(
                f"{person[0].capitalize()} {person[1].capitalize()} é {person[2].capitalize()} com CPF de número {person[3]}"
            )
            print(
                f"Nascido(a) em {person[4].strftime('%d/%m/%y')} e telefone de número ({person[5][:2]}){person[5][2:7]}-{person[5][7:]}"
            )
            print(f"Residente de {person[6]}")
            print(f"E faltam {days} para seu próximo aniversário!\n")

    if found == False:
        print("ERROR 002! Funcionário não encontrado!")
        print("Entre em contato com o RH!")


# Esta função permite a alteração dos dados via pesquisa por número de CPF
def update():
    search = input("Digite o CPF do usuário: ")
    for person in db:
        if search in person:
            os.system("cls")
            print(
                f"{person[0].capitalize()} {person[1].capitalize()} é {person[2].capitalize()} com CPF de número {person[3]}"
            )
            print(
                f"Nascido(a) em {person[4].strftime('%d/%m/%y')} e telefone de número ({person[5][:2]}){person[5][2:7]}-{person[5][7:]}"
            )

            # Identificando qual campo o usuário quer editar
            print("Qual campo gostaria de atualizar:")
            print("Nome - Cargo - Sobrenome - CPF - Nascimento - Telefone")
            field_to_updt = input().upper()

            if field_to_updt == "NOME":
                new_name = input("Digite o novo nome: ")
                person[0] = new_name

            elif field_to_updt == "SOBRENOME":
                new_lastname = input("Digite o novo sobrenome: ")
                person[1] = new_lastname

            elif field_to_updt == "CARGO":
                new_position = input("Digite o novo Cargo: ")
                person[2] = new_position

            elif field_to_updt == "CPF":
                new_cpf = input("Digite o novo CPF: ")
                person[3] = new_cpf

            elif field_to_updt == "NASCIMENTO":
                new_birthdate = birthdate()
                person[4] = new_birthdate

            elif field_to_updt == "TELEFONE":
                new_phone = input("Digite o novo telefone: ")
                person[5] = new_phone

            else:
                print("ERROR 3! Campo inválido!")


# Esta função permite a exclusão dos dados via pesquisa por número de CPF
def delete():
    search = input("Digite o CPF do usuário: ")
    for person in db:
        if search in person:
            os.system("cls")
            print("Tem certeza que deseja remover este funcionário dos registros?")
            print(
                f"{person[0].capitalize()} {person[1].capitalize()} é {person[2].capitalize()} com CPF de número {person[3]}"
            )
            print(
                f"Nascida em {person[4].strftime('%d/%m/%y')} e telefone de número ({person[5][:2]}){person[5][2:7]}-{person[5][7:]}"
            )

            confirm_delete = input("Confirmar a exclusão? (S/N)").upper()
            if confirm_delete == "S":
                db.remove(person)
                print("Registro removido com sucesso!")


# Função principal
def menu():
    logout = False

    while logout != True:
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("Bem Vindo!")
        print("Digite um comando para começar: ")
        print("Criar - Ler - Atualizar - Deletar - Sair")
        option = input().upper()

        # Verifica a opção criar e chama a função adequada
        if option == "CRIAR":
            create()

        # Verifica a opção Ler e chama a função adequada
        elif option == "LER":
            read()

        # Opção Atualizar
        elif option == "ATUALIZAR":
            update()

        # Opção Deletar
        elif option == "DELETAR":
            delete()

        # Opção Sair
        elif option == "SAIR":
            confirmation = False
            while confirmation != True:
                enter_confirm = input("Tem certeza que deseja sair? (S/N)").upper()
                if enter_confirm == "S":
                    logout = True
                    break
                elif enter_confirm == "N":
                    break
                else:
                    continue

        # Caso de entrada errada do usuário
        else:
            print("ERROR 001!")
            print("Digite um comando válido!")


menu()

os.system("cls")

print("Obrigado por utilizar os sistemas MP4/4!")
