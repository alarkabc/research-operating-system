from agents.planner import PlannerAgent
from browser.playwright_client import BrowserAgent
from embeddings.embedding_model import EmbeddingModel
from memory.vector_store import VectorStore
from rag.retriever import Retriever
from knowledge.graph import KnowledgeGraph


class ResearchOperatingSystem:

    def __init__(self):
        self.planner = PlannerAgent()
        self.browser = BrowserAgent()
        self.embedding = EmbeddingModel()
        self.memory = VectorStore()
        self.retriever = Retriever(self.memory)
        self.graph = KnowledgeGraph()

    def initialize(self):

        self.graph.add_node("Research")
        self.graph.add_node("Literature")
        self.graph.connect("Research", "Literature")

        self.planner.create_task(
            "Collect Papers",
            "Search latest AI-assisted cyberattack papers."
        )

        self.browser.start()

    def execute(self):

        print("=" * 60)
        print("Research Operating System")
        print("=" * 60)

        print("\nTasks")
        for task in self.planner.pending_tasks():
            print(task)

        print("\nEmbedding")
        vector = self.embedding.embed(
            "AI-assisted cyberattacks"
        )

        self.memory.add("query", vector)

        print("\nVector Length:", len(vector))

        print("\nRetriever")
        self.retriever.retrieve(
            "AI-assisted cyberattacks"
        )

        print("\nKnowledge Graph")
        print(self.graph.show())

        self.browser.open("https://arxiv.org")

        self.browser.close()


if __name__ == "__main__":

    system = ResearchOperatingSystem()

    system.initialize()

    system.execute()
