import os
from pathlib import Path

from pypdf import PdfReader


class PDFParser:

    def extract_text(self, pdf_path):

        pdf_path = Path(pdf_path)

        if not pdf_path.exists():

            raise FileNotFoundError(pdf_path)

        reader = PdfReader(str(pdf_path))

        pages = []

        for i, page in enumerate(reader.pages):

            try:

                text = page.extract_text()

            except Exception as e:

                print(f"Warning: page {i + 1}: {e}")

                text = ""

            if text:

                pages.append(text)

        return "\n".join(pages)

    def extract_metadata(self, pdf_path):

        reader = PdfReader(pdf_path)

        meta = reader.metadata

        return {

            "title": getattr(meta, "title", None),

            "author": getattr(meta, "author", None),

            "subject": getattr(meta, "subject", None),

            "creator": getattr(meta, "creator", None),

            "producer": getattr(meta, "producer", None),

            "pages": len(reader.pages)

        }

    def save_text(self, pdf_path, output_dir="papers"):

        os.makedirs(output_dir, exist_ok=True)

        text = self.extract_text(pdf_path)

        output_file = os.path.join(

            output_dir,

            Path(pdf_path).stem + ".txt"

        )

        with open(

            output_file,

            "w",

            encoding="utf-8"

        ) as f:

            f.write(text)

        return output_file


if __name__ == "__main__":

    parser = PDFParser()

    pdf = r"downloads\2603_28944v2.pdf"

    metadata = parser.extract_metadata(pdf)

    print()

    print("=" * 70)

    print("Metadata")

    print("=" * 70)

    print(metadata)

    print()

    print("Extracting text...")

    txt = parser.save_text(pdf)

    print()

    print("Saved to:", txt)

    print()

    text = parser.extract_text(pdf)

    print("Characters:", len(text))

    print()

    print(text[:1000])
