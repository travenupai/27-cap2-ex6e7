#crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from src.word.tools.custom_tool import WordCountTool

@CrewBase
class WordCountCrew():
    """Word Count Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def word_counter(self) -> Agent:
        return Agent(
            config=self.agents_config['word_counter'],
            tools=[WordCountTool()],
            verbose=True
        )

    @task
    def word_count_task(self) -> Task:
        return Task(
            config=self.tasks_config['word_count_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Cria a Word Count Crew"""
        return Crew(
            agents=self.agents,  # Criado automaticamente pelo decorador @agent
            tasks=self.tasks,    # Criado automaticamente pelo decorador @task
            process=Process.sequential,
            verbose=True,
        )
