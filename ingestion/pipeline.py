from crawler.arxiv_crawler import ArxivCrawler
from parser.pdf_parser import PDFParser
from chunking.text_chunker import TextChunker


class IngestionPipeline:

    def __init__(
        self,
        embedding_model,
        vector_store,
        knowledge_graph=None,
        chunk_size=600,
        overlap=100
    ):

        self.embedding_model = embedding_model
        self.vector_store = vector_store
        self.knowledge_graph = knowledge_graph

        self.crawler = ArxivCrawler()
        self.parser = PDFParser()
        self.chunker = TextChunker(
            chunk_size=chunk_size,
            overlap=overlap
        )

    def ingest_query(
        self,
        query,
        max_results=5
    ):

        papers = self.crawler.search(
            query=query,
            max_results=max_results
        )

        print()
        print("=" * 70)
        print("Starting Research Paper Ingestion")
        print("=" * 70)
        print()

        total_chunks = 0

        for index, paper in enumerate(papers, start=1):

            print(f"[{index}/{len(papers)}] {paper['title']}")

            pdf_path = self.crawler.download_pdf(paper)

            if pdf_path is None:

                print("Skipped (No PDF)")
                print()
                continue

            text = self.parser.extract_text(pdf_path)

            chunks = self.chunker.chunk(text)

            embeddings = self.embedding_model.embed_batch(chunks)

            for chunk, embedding in zip(chunks, embeddings):

                metadata = {

                    "title": paper["title"],

                    "authors": paper["authors"],

                    "paper_id": paper["id"],

                    "pdf": paper["pdf"],

                    "local_pdf": pdf_path

                }

                self.vector_store.add(

                    chunk,

                    embedding,

                    metadata

                )

            if self.knowledge_graph is not None:

                try:

                    self.knowledge_graph.add_document(

                        title=paper["title"],

                        metadata=metadata

                    )

                except Exception as e:

                    print(f"Knowledge Graph Warning: {e}")

            total_chunks += len(chunks)

            print(f"PDF     : {pdf_path}")
            print(f"Chunks  : {len(chunks)}")
            print()

        print("=" * 70)
        print("INGESTION COMPLETE")
        print("=" * 70)
        print(f"Papers Indexed : {len(papers)}")
        print(f"Chunks Indexed : {total_chunks}")
        print(f"Vector Entries : {self.vector_store.count()}")
        print("=" * 70)

        return papers


if __name__ == "__main__":

    from embeddings.embedding_model import EmbeddingModel
    from memory.vector_store import VectorStore

    embedding = EmbeddingModel()

    vector_store = VectorStore()

    pipeline = IngestionPipeline(

        embedding_model=embedding,

        vector_store=vector_store

    )

    pipeline.ingest_query(

        "AI assisted cyberattacks",

        max_results=3

    )

    print()

    print("Stored vectors:", vector_store.count())

    print()

    query = "LLM cyber attacks"

    query_embedding = embedding.embed(query)

    results = vector_store.search(

        query_embedding,

        top_k=5

    )

    print("=" * 70)
    print("Semantic Search Results")
    print("=" * 70)

    for i, result in enumerate(results, start=1):

        print()

        print(f"Result {i}")

        print("Distance :", result["distance"])

        print("Title    :", result["metadata"].get("title"))

        print("Authors  :", ", ".join(result["metadata"].get("authors", [])))

        print()

        print(result["document"][:400])

        print("-" * 70)
