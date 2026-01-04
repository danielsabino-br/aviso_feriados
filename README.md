# 🚚 Aviso de Feriados Municipais

## 📌 Visão Geral

O **Aviso de Feriados Municipais** é um sistema em Python desenvolvido para auxiliar empresas de logística, transportadoras e equipes de planejamento a **evitar entregas em cidades onde há feriado municipal**.

O sistema roda em segundo plano no Windows e envia **notificações automáticas** quando um feriado municipal está próximo (entre **0 e 5 dias**), reduzindo custos operacionais, retrabalho e deslocamentos desnecessários.

---

## 🎯 Problema que o projeto resolve

Em operações logísticas, é comum que entregas sejam programadas sem considerar feriados municipais, causando:

* Tentativas de entrega sem sucesso
* Atrasos na rota
* Custos extras com combustível e tempo
* Insatisfação do cliente

Este projeto resolve esse problema de forma simples e automatizada.

---

## ⚙️ Funcionalidades

* 📍 Cadastro de cidades e feriados municipais
* 📅 Consulta de feriados futuros
* ❌ Exclusão de cidades cadastradas
* 🔔 Notificação automática de feriados entre **0 e 5 dias**
* 🕒 Execução contínua em segundo plano
* 📝 Geração de logs para auditoria e diagnóstico

---

## 🧠 Regra de Negócio

O sistema verifica o banco de dados periodicamente e dispara notificações quando:

* A data do feriado municipal estiver entre **hoje + 5 dias**

Exemplo:

* Hoje: 04/01/2026
* Feriado: 08/01/2026
* Resultado: 🔔 Notificação enviada (faltam 4 dias)

---

## 🗂️ Estrutura do Projeto

```
aviso_feriados/
│── banco_dados.py        # Criação e conexão com o banco SQLite
│── funcoes.py            # Regras de negócio e lógica principal
│── notification.py       # Disparo de notificações (plyer)
│── menu.py               # Interface de terminal (CRUD)
│── seg.plano.py          # Execução em segundo plano
│── banco_dados.db        # Banco de dados SQLite
│── log_execucao.txt      # Log de execuções
│── log_erro.txt          # Log de erros
```

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **SQLite** (banco de dados local)
* **Pandas** (consultas e manipulação de dados)
* **Plyer** (notificações no sistema operacional)

---

## ▶️ Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/aviso-feriados.git
cd aviso-feriados
```

### 2️⃣ Criar ambiente virtual (opcional, recomendado)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Instalar dependências

```bash
pip install pandas plyer
```

### 4️⃣ Executar o menu de cadastro

```bash
python menu.py
```

### 5️⃣ Executar o monitoramento automático

```bash
python seg.plano.py
```

---

## 🪟 Execução em Segundo Plano (Windows)

Para uso contínuo, recomenda-se:

* Executar via **Agendador de Tarefas do Windows**
* Opção: *Executar somente quando o usuário estiver conectado*
* Garantir que notificações do Python estejam habilitadas

---

## 📊 Logs e Diagnóstico

O sistema gera automaticamente:

* `log_execucao.txt` → confirma execuções do monitor
* `log_erro.txt` → registra falhas e exceções

Esses arquivos facilitam manutenção e auditoria.

---

## 🚀 Melhorias Futuras

* 🔕 Controle anti-spam de notificações
* 🌎 Integração com API de feriados nacionais/estaduais
* 📱 Versão com interface gráfica
* ☁️ Execução como serviço
* 🧪 Testes automatizados

---

## 👨‍💻 Autor

Projeto desenvolvido por **Daniel Francisco Sabino Rocha**
Estudante de Análise e Desenvolvimento de Sistemas e Python.

---

## 📄 Licença

Este projeto é de uso educacional e livre para estudos e melhorias.







