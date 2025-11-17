Atividade 02 - UC05 
O uso do IF NOT EXISTS é importante porque impede que o sistema tente criar uma tabela que 
já está no banco. Sem isso, cada vez que o arquivo fosse executado, 
o programa geraria erro por entender que a tabela já existe.
Com essa cláusula, o código fica mais seguro e mais inteligente: 
ele só cria a tabela se realmente for necessário, evitando retrabalho e garantindo que nada seja sobrescrito.

O commit() é o comando que realmente confirma todas as mudanças que fizemos no banco. Ele funciona como o botão “salvar” — sem ele, a criação da tabela ou qualquer alteração poderia simplesmente se perder.
Já o close() encerra a conexão com o banco de forma adequada. Fechar a conexão é essencial porque libera o arquivo para que outros programas possam usá-lo e evita problemas como travamentos, corrupções ou consumo desnecessário de recursos.

O arquivo banco.py pode ser facilmente reaproveitado porque ele já contém a estrutura básica para conectar ao SQLite e criar tabelas. Em projetos futuros, bastaria adaptar a parte da DDL (os comandos SQL) para representar outras tabelas — como professores, cursos, notas etc.
Ele também pode servir como um módulo de inicialização do banco em sistemas maiores, garantindo que toda a estrutura esteja pronta antes que a aplicação rode.
Ou seja, além de resolver o problema atual, esse arquivo acaba sendo uma base prática para qualquer projeto que precise de um banco SQLite organizado e criado automaticamente.