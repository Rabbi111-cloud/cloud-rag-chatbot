class RAG:
    def __init__(self):
        # initialize embeddings, vector DB, etc later
        pass

    async def answer(self, question: str):
        # temporary dummy response
        return f"You asked: {question}. RAG response will go here."

    async def index_bytes(self, contents: bytes, filename: str):
        # temporary indexing (for testing)
        print(f"Indexed: {filename}, size: {len(contents)} bytes")
