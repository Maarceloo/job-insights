# Job Insights

O Job Insights é um site sobre análises a partir de um conjunto de dados sobre empregos.

Suas implementações foram incorporadas a um aplicativo Web desenvolvido com Flask. também foi escrito alguns testes para a implementação de uma análise de dados. Por fim, como bônus, foi escrito uma rota e view para um recurso novo usando Flask!

 O site é responsavel por:

- Fazer a busca por empregos utilizando alguns filtros como por Tipo de emprego, indústria, salário anual;
- Decidir como mostrar a quantidade de resultados;
- Ao clicar no job, mostra detalhes sobre a vaga de emprego;

---

### 🔧 Instalação

Rodando a aplicacão.

Clone o repositorio:

```
git@github.com:Maarceloo/job-insights.git
```

Acesse `job-insights`

```
cd job-insights/
```

Crie o ambiente virtual para o projeto:

```
python3 -m venv .venv && source .venv/bin/activate
```

Instale as dependencias:

```
python3 -m pip install -r dev-requirements.txt
```

Para rodar o frontend execute o comando abaixo na raz do prijeto:

```
flask run
```

Clique aqui para visualizar a aplicação:

- [Job Insights](http://localhost:5000)

---

## ⚙️ Executando os teste

Para rodar os testes execute o comando:

```
python3 -m pytest
```

---

## 🛠️ Tecnologias

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Flake8](https://flake8.pycqa.org/en/latest/)
- [Pytest](https://docs.pytest.org/en/7.2.x/)

---

⌨️ Desenvolvido por [Marcelo De Lima](https://github.com/Maarceloo) 🛠️

---
