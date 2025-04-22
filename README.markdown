# Math Query Interface

## Descrição

O **Math Query Interface** é um projeto Python que permite aos usuários inserir expressões matemáticas em linguagem natural, como "soma de dois mais dois", e receber o resultado numérico, como "4". O projeto utiliza uma interface web interativa construída com a biblioteca Gradio e processa as entradas com o modelo de linguagem leve **distilgpt2** do Hugging Face, complementado por um parser personalizado para interpretar e calcular expressões matemáticas simples.

## Funcionalidades

- **Entrada em linguagem natural**: Permite que os usuários digitem expressões matemáticas como "soma de dois mais dois" ou "três vezes quatro".
- **Processamento com LLM**: Usa o modelo **distilgpt2** para entender a intenção da entrada.
- **Cálculo preciso**: Um parser personalizado extrai números e operações para garantir resultados corretos.
- **Interface amigável**: Interface web simples fornecida pelo Gradio, acessível via navegador.

## Tecnologias Utilizadas

- **Python 3.8+**: Linguagem de programação principal.
- **Gradio**: Biblioteca para criar interfaces web interativas.
- **Transformers (Hugging Face)**: Usada para carregar e executar o modelo **distilgpt2**.
- **PyTorch**: Framework de machine learning necessário para o modelo **distilgpt2**.
- **re**: Módulo nativo do Python para expressões regulares, usado no parser.

## Pré-requisitos

- Python 3.8 ou superior ([download](https://www.python.org/downloads/)).
- pip (gerenciador de pacotes do Python).
- Conexão com a internet para baixar o modelo **distilgpt2** e as dependências.

## Instalação

1. **Clone o repositório** ou crie um diretório para o projeto:
   ```bash
   mkdir math-query-interface
   cd math-query-interface
   ```
   Salve o arquivo `math_query_interface.py` neste diretório.

2. **Crie e ative um ambiente virtual** (recomendado):
   ```bash
   python -m venv venv
   ```
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```

3. **Instale as dependências**:
   ```bash
   pip install gradio transformers torch

   pip install num2words
   ```

## Como Executar

1. Certifique-se de que o ambiente virtual está ativado e as dependências estão instaladas.
2. No diretório do projeto, execute o script:
   ```bash
   python math_query_interface.py
   ```
3. O Gradio iniciará um servidor web local (geralmente em `http://127.0.0.1:7860`). Uma janela do navegador abrirá automaticamente com a interface.
4. Na interface, digite uma expressão matemática em linguagem natural (ex.: "soma de dois mais dois") e clique em "Submit" para ver o resultado.

Para parar o servidor, pressione `Ctrl + C` no terminal e desative o ambiente virtual com:
```bash
deactivate
```

## Exemplos de Uso

| Entrada                      | Saída Esperada |
|------------------------------|----------------|
| soma de dois mais dois       | 4              |
| três vezes quatro            | 12             |
| cinco menos um               | 4              |
| seis dividido por dois       | 3              |

## Limitações

- O modelo **distilgpt2** é leve e pode não interpretar corretamente expressões complexas ou ambíguas.
- O parser suporta apenas operações básicas (+, -, *, /) com dois números.
- Entradas fora do formato esperado (ex.: "qual é a soma de dois") podem gerar resultados incorretos.
- O projeto não lida com números negativos ou frações.

## Solução de Problemas

- **Erro "ModuleNotFoundError"**: Verifique se todas as dependências estão instaladas e se o ambiente virtual está ativado.
- **Interface não abre**: Acesse manualmente `http://127.0.0.1:7860` ou verifique se a porta está livre.
- **Modelo não baixa**: Confirme que há conexão com a internet e espaço em disco suficiente (~500 MB).
- **Respostas incorretas**: Use entradas simples e claras, como "soma de dois mais dois".
