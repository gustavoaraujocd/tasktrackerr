# Demonstração ponta a ponta - TaskTracker

Roteiro executável manualmente; não é evidência de uma sessão humana já realizada.
Todos os dados abaixo são fictícios. Inicie uma única execução, pois os registros vivem em memória.

## Início
```bash
docker compose run --build --rm tasktracker-app
```
Alternativa local após instalar as dependências: `python src/main.py`.

## Sequência

1. Escolha 2. Deve mostrar lista vazia.
2. Escolha 1. No título, envie apenas espaços; confirme a rejeição e informe "Entregar atividade".
3. Descrição: "Exemplo acadêmico". Prioridade: "urgente" deve ser rejeitada; depois use "Alta".
4. Data: "31/02/2099" deve ser rejeitada; depois "31/12/2099". Hora: "25:61" deve ser rejeitada; depois "18:30".
5. Copie o ID completo exibido. Escolha 2 e confirme os campos e status Pendente.
6. Escolha 4, cole o ID e confirme a consulta. Repita com um ID inexistente: erro orientado e menu continua.
7. Escolha 5 e cole o ID. Título: "Atividade revisada"; deixe descrição, prioridade, data e hora em branco para manter. Status: "em_andamento".
8. Escolha 7 e filtre por "em_andamento". Deve aparecer a tarefa atualizada.
9. Escolha 6 e cole o ID. Depois filtre por "concluida"; deve aparecer a tarefa concluída.
10. Cadastre outra tarefa com data "01/01/2000" e hora "10:00". O terminal deve alertar atraso. Conclua pelo ID e confirme que esse alerta desaparece.
11. Escolha 3 para sair. Ao reiniciar, a lista deve estar vazia (limite de persistência documentado).

## Harness
```bash
docker compose build tests
docker compose run --rm tests
```
O snapshot técnico possui 39 testes aprovados no CI. Uma pessoa de fora da equipe ainda precisa conferir o clone limpo e este roteiro seguindo apenas o README.
