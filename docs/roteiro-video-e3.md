# TaskTracker | Roteiro de demonstração
## Estado e preparação
Roteiro preparado; vídeo não gravado nem publicado nesta execução. Não há URL final. O formato sugerido é 5 minutos, 16:9, voz/rosto do responsável, conforme guia local anterior do Bootcamp II; confirmar o limite específico da Entrega 3 com a disciplina.
Abra repositório, README, SDD, PRs, CI e terminal. Use a candidata somente enquanto não houver release; mostre a branch e o SHA real com git branch --show-current e git rev-parse HEAD. Após release, use checkout da tag real. Aumente a fonte e ensaie. Não apresente a candidata como main homologada.
## 0:00-0:35 | Identificação e problema
Apresente nome/RA, curso e objetivo de organizar tarefas por prioridade, prazo e status. Se for apresentação de grupo, confirme os participantes reais. Diga o estado atual da entrega e quais etapas ainda dependem de revisão.
## 0:35-1:20 | Arquitetura e contrato
Mostre src/main.py, models.py e service.py. Explique CLI -> serviço -> Task -> memória; UUID; enum; atualização atômica. Mostre SDD As-Built. Diga que dados se perdem ao encerrar e que não há API HTTP.
## 1:20-3:20 | Aplicação real
Execute docker compose run --build --rm tasktracker-app e aguarde sucesso. Se usar Python, declare que esta parte é execução local: python src/main.py. Não alegue execução Docker a partir de um teste Python.
1. Cadastre: opção 1; título vazio (erro), depois 'Entrega 3'; descrição 'Demo real'; prioridade urgente (erro), depois Alta; data 31/12/2099; hora 18:30.
2. Liste em 2; copie o ID real; consulte em 4.
3. Atualize em 5; use o ID; altere título para 'Entrega 3 revisada'; mantenha os demais com Enter; status em_andamento.
4. Filtre em 7 por concluida; mostre ausência de correspondências sem alegar cadastro vazio.
5. Conclua em 6 com o ID; filtre por concluida em 7; mostre a tarefa.
6. Se houver tempo, cadastre outra tarefa com data 01/01/2000, sem hora, e mostre um alerta por ciclo. Saia em 3; esclareça perda dos dados.
## 3:20-4:20 | Testes e coverage
Execute python -m pytest -q --cov --cov-report=term-missing. Mostre o resultado real e explique aprovação dos testes versus cobertura de linhas/ramos. Abra HTML/JUnit da mesma revisão. Mostre os jobs test e docker da execução correspondente ao SHA exibido. Não use CI antigo como prova de código novo.
## 4:20-5:00 | Governança e encerramento
Abra PR e ruleset. Se merge/tag ainda não ocorreram, diga explicitamente que aguardam aprovação e que v1.0.0 não foi publicada. Após publicação real, mostre release vinculada ao commit de main e arquivos. Cite retrospectiva e limitações: memória, monousuário e ausência de benchmark comparativo empírico.
## Publicação e conferência
Grave as interações de verdade, sem substituir por narração de comandos não executados. Publique no destino exigido pela disciplina, confira acesso anônimo, insira o link real no README e regenere material de submissão. O roteiro e logs não equivalem ao vídeo. Não enviar como entrega plenamente homologada enquanto faltarem aceite, release ou demonstração exigida.
