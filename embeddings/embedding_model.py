from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(
        self,
        model_name="all-MiniLM-L6-v2"
    ):

        print("Loading embedding model...")

        self.model = SentenceTransformer(model_name)

    def embed(
        self,
        text
    ):

        return self.model.encode(text).tolist()

    def embed_batch(
        self,
        texts
    ):

        return self.model.encode(texts).tolist()


if __name__ == "__main__":

    model = EmbeddingModel()

    vectors = model.embed_batch(

        [

            "Artificial Intelligence",

            "Cybersecurity",

            "Quantum Computing"

        ]

    )

    print(

        len(vectors),

        len(vectors[0])

    )
