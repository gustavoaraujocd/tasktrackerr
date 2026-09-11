# Receita Lógica do Sistema — TaskTracker

## Fluxo principal

1. Iniciar o sistema.
2. Exibir o menu principal.
3. Permitir ao usuário escolher uma ação.
4. Se a opção for cadastrar tarefa:
   - solicitar título;
   - solicitar descrição;
   - solicitar prioridade;
   - solicitar prazo;
   - validar os dados;
   - definir o status inicial como pendente;
   - salvar a tarefa;
   - informar que o cadastro foi realizado.
5. Se a opção for listar tarefas:
   - verificar se existem tarefas cadastradas;
   - apresentar cada tarefa com seus dados principais.
6. Se a opção for atualizar tarefa:
   - solicitar o identificador da tarefa;
   - localizar a tarefa;
   - permitir alteração dos campos válidos;
   - salvar as alterações.
7. Se a opção for concluir tarefa:
   - solicitar o identificador;
   - localizar a tarefa;
   - alterar o status para concluída;
   - salvar a alteração.
8. Se a opção for sair:
   - encerrar o sistema.
9. Caso a opção seja inválida:
   - informar o erro;
   - retornar ao menu principal.

## Validações previstas

- Não permitir título vazio.
- Aceitar somente prioridades válidas.
- Aceitar somente datas em formato válido.
- Não atualizar uma tarefa inexistente.
- Não concluir uma tarefa inexistente.

## Observação

Este algoritmo está descrito em linguagem natural propositalmente. A transformação para código Python pertence à próxima fase do projeto.
