# Projeto Final: Sistema de RH

[English](README.md) | Português

Este é o projeto final para o módulo. O objetivo é criar um sistema de RH que cumpra os requisitos especificados abaixo.

## Requisitos

O sistema deve ser capaz de armazenar registros de funcionários, incluindo nome, sobrenome, telefone, profissão e data de nascimento.

Funcionalidades do sistema:

- `Criar`: Permitir adicionar novos registros ao sistema.
- `Ler` Encontrar registros completos, buscando pelo nome ou profissão. O nome deve ser apresentado com as primeiras letras maiúsculas, e o número de telefone deve estar no formato "(dd) 1234-5678". Os dados devem ser apresentados de forma visualmente agradável.
- `Atualizar` Permitir atualizar um registro, buscando pelo número de telefone.
- `Deletar`: Permitir excluir um registro, buscando pelo número de telefone.

Cada operação deve ser implementada em sua própria função. Deve ser possível chamar uma única função chamada `menu()`, que permitirá ao usuário acessar as diferentes operações.

## Bônus

- **Bônus 1**: Ao realizar a operação de leitura, mostrar quantos dias faltam para o aniversário do colaborador registrado.
- **Bônus 2**: Receber o CEP do colaborador e armazenar o endereço correspondente.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
