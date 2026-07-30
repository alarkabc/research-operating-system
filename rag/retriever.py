class Retriever:

    def __init__(self, vector_store):
        self.vector_store = vector_store

    def retrieve(self, query):
        print(f"Searching for: {query}")
        return []


if __name__ == "__main__":
    r = Retriever(None)
    print(r.retrieve("AI Cybersecurity"))
