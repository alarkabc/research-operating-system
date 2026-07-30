class Retriever:

    def __init__(self, embedding_model, vector_store):

        self.embedding = embedding_model

        self.vector_store = vector_store

    def add_document(self, text):

        embedding = self.embedding.embed(text)

        self.vector_store.add(
            text,
            embedding
        )

    def retrieve(self, query, top_k=5):

        embedding = self.embedding.embed(query)

        return self.vector_store.search(
            embedding,
            top_k
        )


if __name__ == "__main__":

    from embeddings.embedding_model import EmbeddingModel
    from memory.vector_store import VectorStore

    embedding = EmbeddingModel()

    store = VectorStore()

    retriever = Retriever(
        embedding,
        store
    )

    retriever.add_document(
        "Artificial Intelligence improves cybersecurity."
    )

    retriever.add_document(
        "Quantum computing threatens RSA."
    )

    results = retriever.retrieve(
        "AI cybersecurity"
    )

    for item in results:

        print(item)
