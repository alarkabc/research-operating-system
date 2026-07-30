from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(self,
                 model_name="all-MiniLM-L6-v2"):

        print("Loading embedding model...")

        self.model = SentenceTransformer(model_name)

    def embed(self, text: str):

        return self.model.encode(text).tolist()


if __name__ == "__main__":

    model = EmbeddingModel()

    vector = model.embed(
        "AI-assisted cyberattacks"
    )

    print("Embedding dimension:", len(vector))
