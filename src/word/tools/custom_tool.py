from crewai.tools import BaseTool  # Ajuste conforme necessário
import time
from datetime import datetime, timedelta

# Variáveis globais para controle de cache
cache_word_count = None
ultima_consulta = None

class WordCountTool(BaseTool):
    name: str = "WordCountTool"
    description: str = (
        "Esta ferramenta conta o número de palavras em um texto fornecido.\n"
        "Entrada: um texto como string.\n"
        "Saída: uma string descrevendo o total de palavras encontradas."
    )

    def _run(self, text: str) -> str:
        global cache_word_count, ultima_consulta
        word_count = len(text.split())

        if word_count > 50:
            agora = datetime.now()
            # Verifica se o cache pode ser usado (última consulta há menos de 5 minutos)
            if ultima_consulta and (agora - ultima_consulta < timedelta(minutes=5)):
                return f"Usando cache: o texto fornecido contém {cache_word_count} palavras."

            # Atualiza o cache
            cache_word_count = word_count
            ultima_consulta = agora
            # Simula uma operação demorada
            time.sleep(2)
            return f"O texto fornecido contém {word_count} palavras."

        else:
            # Simula uma operação demorada
            time.sleep(2)
            return f"O texto fornecido contém {word_count} palavras."
