#!/usr/bin/env python
import sys
import time
import warnings
from word.crew import WordCountCrew
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Executa a crew.
    """
    # Texto de entrada com 60 palavras
    input_text = ("Este é um exemplo simples de texto que contém exatamente vinte palavras "
                  "para testar nossa ferramenta de contagem de palavras. "
                  "Este é um exemplo simples de texto que contém exatamente vinte palavras "
                  "para testar nossa ferramenta de contagem de palavras. "
                  "Este é um exemplo simples de texto que contém exatamente vinte palavras "
                  "para testar nossa ferramenta de contagem de palavras.")

    inputs = {
        'text': input_text
    }

    # Primeira execução (sem cache)
    start_time = time.time()
    WordCountCrew().crew().kickoff(inputs=inputs)
    first_duration = time.time() - start_time
    print(f"Tempo de execução na primeira vez: {first_duration:.6f} segundos\n")

    # Segunda execução (com cache)
    start_time = time.time()
    WordCountCrew().crew().kickoff(inputs=inputs)
    second_duration = time.time() - start_time
    print(f"Tempo de execução na segunda vez: {second_duration:.6f} segundos\n")

    # Comparação
    improvement = first_duration - second_duration
    print(f"Melhoria de desempenho: {improvement:.6f} segundos")

if __name__ == "__main__":
    run()

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Word().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Word().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Word().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
