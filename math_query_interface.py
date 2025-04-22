import gradio as gr
from transformers import pipeline
import re
from num2words import num2words

# Carrega o modelo leve distilgpt2 para geração de texto
generator = pipeline("text-generation", model="distilgpt2")

# Função para interpretar expressões matemáticas simples em linguagem natural
def parse_math_expression(query):
    # Normaliza a entrada para letras minúsculas
    query = query.lower().strip()
    
    # Dicionário de palavras para números
    word_to_num = { num2words(i, lang="pt"): i for i in range(0, 51) }
    
    # Dicionário de operações
    operation_map = {
        "soma": "+", "mais": "+", "adicao": "+",
        "subtracao": "-", "menos": "-",
        "multiplicacao": "*", "multiplicado" : "*", "vezes": "*",
        "divisao": "/", "dividido por": "/"
    }
    
    # Extrai números e operação da query
    numbers = []
    operation = None
    
    # Procura por números (em palavras ou dígitos)
    for word in query.split():
        if word in word_to_num:
            numbers.append(word_to_num[word])
        elif word.isdigit():
            numbers.append(int(word))
        elif word in operation_map:
            operation = operation_map[word]
    
    # Se encontrou dois números e uma operação, realiza o cálculo
    if len(numbers) >= 2 and operation:
        a, b = numbers[0], numbers[1]
        if operation == "+":
            return str(a + b)
        elif operation == "-":
            return str(a - b)
        elif operation == "*":
            return str(a * b)
        elif operation == "/":
            return str(a / b) if b != 0 else "Erro: Divisão por zero"
    
    return "Não consegui interpretar a expressão."

# Função principal para processar a entrada do usuário
def process_query(user_input):
    # Usa a LLM para gerar uma resposta inicial
    prompt = f"Responda apenas com o resultado da expressão: {user_input}"
    response = generator(prompt, max_length=50, num_return_sequences=1, truncation=True)[0]["generated_text"]
    
    # Extrai o resultado numérico da resposta da LLM, se possível
    match = re.search(r"\d+", response)
    if match:
        return match.group()
    
    # Caso a LLM não retorne um número claro, usa o parser de expressões
    return parse_math_expression(user_input)

# Cria a interface com Gradio
interface = gr.Interface(
    fn=process_query,
    inputs=gr.Textbox(label="Digite sua expressão (ex.: 'soma de dois mais dois')"),
    outputs=gr.Textbox(label="Resultado"),
    title="Calculadora de Expressões em Linguagem Natural",
    description="Digite uma expressão matemática em linguagem natural e receba o resultado."
)

# Lança a interface
if __name__ == "__main__":
    interface.launch()