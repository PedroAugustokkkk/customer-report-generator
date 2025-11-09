# 📈 Gerador de Relatório de Cliente AI (Protótipo)

> Uma ferramenta interna de produtividade que usa IA Generativa (Google Gemini) para automatizar a escrita de relatórios e e-mails para clientes de agências.

Este protótipo (direcionado à Click Interativo e TW2) demonstra como a IA Generativa pode resolver um gargalo operacional crítico em agências de marketing: a comunicação com o cliente.
Caso deseje testar a ferramenta agora, pode acessar a URL: https://customer-report.streamlit.app

## 🎯 O Problema

Membros da equipe (Gerentes de Conta, Analistas de Mídia) gastam horas por semana coletando métricas e, mais importante, *traduzindo* essas métricas em um texto otimista e profissional para um e-mail de atualização. É um trabalho repetitivo, demorado e que exige um tom de escrita específico.

## 💡 A Solução

Uma ferramenta interna "Generative AI" (GenAI). Em vez de ler documentos (como em um RAG), esta ferramenta *cria* conteúdo novo.

O funcionário da agência simplesmente insere os dados brutos (Cliques, Custo, Conversões) em um formulário. A ferramenta envia esses dados para um LLM (Google Gemini Flash) com um "Prompt Mestre" cuidadosamente engenheirado, que instrui a IA a agir como um "Gerente de Contas Sênior" e escrever um parágrafo de resumo perfeito.

**Valor para o Negócio:**
* **Economia de Horas:** Reduz o tempo de escrita de relatórios de horas para segundos.
* **Padronização da Qualidade:** Garante que todo cliente receba uma comunicação clara, otimista e profissional, independente de qual analista a escreveu.
* **Foco no Estratégico:** Libera a equipe para gastar tempo analisando dados em vez de escrevendo e-mails.

## ✨ Funcionalidades Principais

* **Interface de Métrica:** Um formulário limpo em Streamlit para inserir os KPIs (Cliques, Custo, Conversões, Nome do Cliente).
* **Engenharia de Prompt:** Um "Prompt Mestre" (`prompt_template`) que define a "persona" (Gerente de Contas Sênior), o tom (otimista) e a tarefa (resumo de e-mail).
* **Modelo Rápido (GenAI):** Utiliza o `gemini-2.5-flash` para geração de texto quase instantânea.
* **Output Pronto para Copiar:** A IA gera um parágrafo em uma `st.text_area`, pronto para o funcionário copiar e colar no e-mail.

## 🛠️ Stack de Tecnologia

* **Frontend:** Streamlit
* **Orquestração de Prompt:** LangChain
* **LLM (Geração):** Google Gemini 2.5 Flash (via API)

(Nota: Esta stack é intencionalmente mais leve que a de um RAG, pois não requer vetorização, embeddings locais ou bancos de dados vetoriais como FAISS).

## 🚀 Como Executar Localmente

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/seu-usuario/agencia-ai-reporter.git](https://github.com/seu-usuario/agencia-ai-reporter.git)
    cd agencia-ai-reporter
    ```

2.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3.  Instale as dependências (leves):
    ```bash
    pip install -r requirements.txt
    ```

4.  Configure suas chaves de API (veja abaixo).

5.  Execute a aplicação:
    ```bash
    streamlit run app.py
    ```

## 🔑 Configuração

Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API do Google:

```plaintext
GOOGLE_API_KEY="sua-chave-secreta-do-google-aqui"
