from src.main import Retriever, Generator


def test_retriever_returns_top_k_documents() -> None:
    docs = ["a", "b", "c"]
    retriever = Retriever(docs)

    results = retriever.retrieve("query", top_k=2)

    assert results == ["a", "b"]


def test_generator_includes_context_count() -> None:
    generator = Generator()

    answer = generator.generate("query", ["a", "b"])

    assert "2 context documents" in answer
