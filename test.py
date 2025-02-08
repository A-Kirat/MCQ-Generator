from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

llm = LLM(
    model="gemini/gemini-1.5-pro-latest",
    temperature=0.7,
    api_key= os.getenv("GEMINI_API_KEY")
)


#.......................................................................................................... 

@CrewBase
class McqGen:
    """PdfRag crew"""

    agents_config = 'agents.yaml'
    tasks_config = 'tasks.yaml'

    @agent
    def text_analyist_agent(self) -> Agent:
        # Ensure that the agent config is correctly loaded from 'agents.yaml'
        return Agent(
            config=self.agents_config['text_analyist_agent'],  # Make sure this key exists in agents.yaml
            verbose=True,
            llm=llm  # Pass the initialized Gemini LLM model here
        )

    
    @agent
    def question_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['question_generator_agent'],
            verbose=True,
            llm=llm
        )

    @task
    def text_analyist_task(self) -> Task:
        # Ensure that the task config is correctly loaded from 'tasks.yaml'
        return Task(
            config=self.tasks_config['text_analyist_task'],  # Make sure this key exists in tasks.yaml
        )

    @task
    def question_generator_task(self) -> Task:
        return Task(
            config=self.tasks_config['question_generator_task'],
        )

    @crew
    def crew(self) -> Crew:
        # Create a Crew instance with the agents and tasks defined
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,  # Change process as needed
            verbose=True,
            # You can also use Process.hierarchical if needed
            # process=Process.hierarchical, 
        )
