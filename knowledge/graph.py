class KnowledgeGraph:

    def __init__(self):
        self.graph = {}

    def add_node(self,name):
        self.graph[name] = []

    def connect(self,a,b):
        self.graph.setdefault(a,[]).append(b)

    def show(self):
        return self.graph


if __name__ == "__main__":
    kg = KnowledgeGraph()
    kg.add_node("AI")
    kg.add_node("Cybersecurity")
    kg.connect("AI","Cybersecurity")
    print(kg.show())
