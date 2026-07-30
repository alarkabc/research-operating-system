import faiss
import numpy as np
import pickle
from pathlib import Path


class VectorStore:

    def __init__(
        self,
        dimension=384
    ):

        self.dimension = dimension

        self.index = faiss.IndexFlatL2(dimension)

        self.documents = []

        self.metadata = []

    def add(
        self,
        text,
        embedding,
        metadata=None
    ):

        vector = np.asarray(
            embedding,
            dtype=np.float32
        ).reshape(1, -1)

        self.index.add(vector)

        self.documents.append(text)

        self.metadata.append(metadata or {})

    def search(
        self,
        embedding,
        top_k=5
    ):

        if len(self.documents) == 0:

            return []

        vector = np.asarray(
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

            if index == -1:

                continue

            results.append({

                "document": self.documents[index],

                "metadata": self.metadata[index],

                "distance": float(distance)

            })

        return results

    def count(self):

        return len(self.documents)

    def save(
        self,
        directory="vector_store"
    ):

        directory = Path(directory)

        directory.mkdir(
            exist_ok=True
        )

        faiss.write_index(

            self.index,

            str(directory / "index.faiss")

        )

        with open(

            directory / "documents.pkl",

            "wb"

        ) as f:

            pickle.dump(

                {

                    "documents": self.documents,

                    "metadata": self.metadata

                },

                f

            )

    def load(
        self,
        directory="vector_store"
    ):

        directory = Path(directory)

        self.index = faiss.read_index(

            str(directory / "index.faiss")

        )

        with open(

            directory / "documents.pkl",

            "rb"

        ) as f:

            data = pickle.load(f)

        self.documents = data["documents"]

        self.metadata = data["metadata"]


if __name__ == "__main__":

    db = VectorStore()

    db.add(

        "Artificial Intelligence",

        np.random.rand(384).tolist(),

        {

            "source": "demo"

        }

    )

    print(db.count())

    print(

        db.search(

            np.random.rand(384).tolist()

        )

    )
