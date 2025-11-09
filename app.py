import streamlit as st
from dotenv import load_dotenv

# LLM e Prompts
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# --- Configurações Globais ---
load_dotenv()
# (A chave GOOGLE_API_KEY é lida automaticamente pelo ChatGoogleGenerativeAI)

# --- 1. Configuração da Chain Generativa ---

@st.cache_resource
def get_generative_chain():
    """
    Configura e retorna a chain de geração de texto.
    
    Utiliza 'gemini-1.5-flash-latest' para alta velocidade.
    """
    
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7 # Aumentamos a temperatura para um texto mais 'criativo' e 'humano'
    )

    # Este é o "Prompt Mestre", o coração deste projeto.
    # É o 'roteiro' que a IA deve seguir.
    prompt_template = """
    Você é um Gerente de Contas Sênior em uma agência de marketing digital. Sua linguagem é
    otimista, profissional e focada em resultados (mas sem ser robótica).
    
    Sua tarefa é escrever um parágrafo curto (3-4 frases) para um e-mail de
    atualização semanal para o cliente.
    
    Use os dados fornecidos abaixo. Foque no que deu certo.

    DADOS DA CAMPANHA:
    - Nome do Cliente: {nome_cliente}
    - Total de Cliques: {cliques}
    - Custo Total (R$): {custo}
    - Total de Conversões (Vendas/Leads): {conversoes}

    Exemplo de Tom: "Olá [Cliente], tivemos uma ótima semana! Conseguimos aumentar
    o engajamento e as conversões ficaram bem acima da meta..."
    
    Escreva agora o parágrafo de resumo para o cliente:
    """
    prompt = ChatPromptTemplate.from_template(prompt_template)

    # O StrOutputParser apenas garante que a saída seja uma string de texto simples
    output_parser = StrOutputParser()

    # Monta a 'chain' (Prompt -> LLM -> Parser de Saída)
    chain = prompt | llm | output_parser
    
    return chain

# --- 2. Interface Streamlit (UI) ---

def main():
    """Função principal que renderiza a aplicação Streamlit."""
    
    st.set_page_config(page_title="Gerador de Relatório AI", page_icon="📈")
    st.title("📈 Gerador de Relatório de Cliente AI")
    st.write("Uma ferramenta interna para automatizar resumos de performance.")

    # Inicializa a chain (usa o cache)
    try:
        chain = get_generative_chain()
    except Exception as e:
        st.error(f"Erro ao inicializar o modelo de IA: {e}")
        st.stop()

    # Coleta de dados com st.form para evitar recarregamento a cada input
    with st.form(key="metrics_form"):
        st.subheader("📊 Insira as Métricas da Semana")
        
        # Colunas para melhor layout
        col1, col2 = st.columns(2)
        
        with col1:
            nome_cliente = st.text_input("Nome do Cliente", placeholder="Ex: Loja do Zé")
            cliques = st.number_input("Cliques (Google Ads)", min_value=0, step=1)
        
        with col2:
            custo = st.number_input("Custo (R$)", min_value=0.0, format="%.2f", step=10.0)
            conversoes = st.number_input("Conversões (Leads/Vendas)", min_value=0, step=1)
        
        # Botão de envio do formulário
        submit_button = st.form_submit_button(label="Gerar Resumo Otimista")

    # Processamento (só ocorre após o clique no botão)
    if submit_button:
        # Validação simples
        if not nome_cliente or not cliques or not conversoes:
            st.warning("Por favor, preencha todos os campos para gerar o resumo.")
        else:
            # Cria o dicionário de input para a chain
            input_data = {
                "nome_cliente": nome_cliente,
                "cliques": cliques,
                "custo": custo,
                "conversoes": conversoes
            }
            
            with st.spinner("Gerando texto com o Gemini..."):
                try:
                    # Invoca a chain de geração
                    generated_text = chain.invoke(input_data)
                    
                    st.subheader("✅ Resumo Gerado para Copiar")
                    st.text_area("Texto do E-mail:", generated_text, height=150)
                    st.success("Texto gerado com sucesso!")
                    
                except Exception as e:
                    st.error(f"Erro ao gerar o texto: {e}")

# --- Ponto de Entrada ---
if __name__ == "__main__":
    main()