import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension=384):

        self.dimension = dimension

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.documents = []

    def add(self, text, embedding):

        vector = np.array(
            embedding,
            dtype=np.float32
        ).reshape(1, -1)

        self.index.add(vector)

        self.documents.append(text)

    def search(self, embedding, top_k=5):

        if len(self.documents) == 0:

            return []

        vector = np.array(
            embedding,
            dtype=np.float32
        ).reshape(1, -1)

        k = min(
            top_k,
            len(self.documents)
        )

        distances, indices = self.index.search(
            vector,
            k
        )

        results = []

        for distance, index in zip(
            distances[0],
            indices[0]
        ):

            if index != -1:

                results.append({

                    "document": self.documents[index],

                    "distance": float(distance)

                })

        return results


if __name__ == "__main__":

    db = VectorStore()

    db.add(

        "Artificial Intelligence",

        np.random.rand(384).tolist()

    )

    print(

        db.search(

            np.random.rand(384).tolist()

        )

    )
