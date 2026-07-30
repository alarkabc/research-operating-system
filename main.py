from agents.planner import PlannerAgent

from browser.playwright_client import BrowserAgent

from embeddings.embedding_model import EmbeddingModel

from memory.vector_store import VectorStore

from rag.retriever import Retriever

from knowledge.graph import KnowledgeGraph


class ResearchOperatingSystem:


    def __init__(self):

        print("=" * 60)

        print("Research Operating System")

        print("=" * 60)

        self.planner = PlannerAgent()

        self.browser = BrowserAgent()

        self.embedding = EmbeddingModel()

        self.memory = VectorStore()

        self.retriever = Retriever(

            self.embedding,

            self.memory

        )

        self.graph = KnowledgeGraph()

        self.graph.add_node("Research")

        self.graph.add_node("Literature")

        self.graph.connect(

            "Research",

            "Literature"

        )

        self.planner.create_task(

            "Collect Papers",

            "Search latest AI-assisted cyberattack papers."

        )


    def demo(self):

        print()

        print("Tasks")

        for task in self.planner.pending_tasks():

            print(task)

        print()

        print("Embedding")

        vector = self.embedding.embed(

            "AI-assisted cyberattacks"

        )

        print()

        print("Vector Length:", len(vector))

        self.memory.add(

            "AI-assisted cyberattacks",

            vector

        )

        print()

        print("Retriever")

        print(

            self.retriever.retrieve(

                "AI cybersecurity"

            )

        )

        print()

        print("Knowledge Graph")

        self.graph.show()

        self.browser.start()

        self.browser.open(

            "https://arxiv.org"

        )

        self.browser.close()


if __name__ == "__main__":

    ros = ResearchOperatingSystem()

    ros.demo()
