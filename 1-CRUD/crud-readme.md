## Project instructions

Você foi contratado para trabalhar no RH de uma empresa multinacional como trainee! Na sua primeira semana, você estará no setor de RH. Sua primeira tarefa é criar um sistema que atenda aos seguintes requisitos:

O sistema deve ser capaz de armazenar os registros dos funcionários, que incluem pelo menos: nome, sobrenome, telefone, profissão e data de nascimento.

O sistema deve ser capaz de realizar as operações básicas de um banco de dados: Criar, Ler, Atualizar e Deletar, ou seja:

- ```Criar```: Permitir ao usuário adicionar novos registros ao sistema.

- ```Ler```: Permitir ao usuário encontrar o registro completo, pesquisando pelo nome ou pela profissão. Os dados devem ser apresentados de forma que o nome tenha as primeiras letras em maiúsculas. O número de telefone deve ser apresentado no formato "(dd) 1234-5678". Os dados devem ser apresentados de forma visualmente agradável.

- ```Atualizar```: Permitir ao usuário atualizar um registro, pesquisando pelo número de telefone.

- ```Deletar```: Permitir ao usuário excluir um registro, pesquisando pelo número de telefone.

Cada operação deve ser implementada em sua própria função.

Deve ser possível chamar uma única função chamada ```menu()```, que permitirá ao usuário acessar as diferentes operações.

```Bônus 1```: Ao realizar a operação de leitura, mostrar quantos dias faltam para o aniversário do colaborador registrado.

```Bônus 2```: Receber o CEP do colaborador e armazenar o endereço correspondente.
