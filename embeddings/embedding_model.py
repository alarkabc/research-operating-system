class EmbeddingModel:
    """
    Placeholder embedding model.
    """

    def embed(self, text: str):
        return [float(ord(c)) for c in text[:64]]


if __name__ == "__main__":
    model = EmbeddingModel()
    print(model.embed("Quantum AI"))
