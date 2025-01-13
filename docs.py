from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI
import os

class KaiaDocAgent:
    def __init__(self, api_key):
        # Initialize OpenAI API key
        os.environ["OPENAI_API_KEY"] = api_key
        self.embeddings = OpenAIEmbeddings()
        self.vector_store = None
        
    def load_docs(self, url="https://docs.kaia.io/"):
        # Load documentation from URL
        loader = WebBaseLoader(url)
        documents = loader.load()
        
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        splits = text_splitter.split_documents(documents)
        
        # Create vector store
        self.vector_store = Chroma.from_documents(
            documents=splits,
            embedding=self.embeddings
        )
        
    def create_qa_chain(self):
        # Create retrieval QA chain
        llm = OpenAI(temperature=0)
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever()
        )
        return qa_chain
    
    def query(self, question: str) -> str:
        if not self.vector_store:
            raise ValueError("Please load documents first using load_docs()")
        
        qa_chain = self.create_qa_chain()
        response = qa_chain.run(question)
        return response
    
# Initialize the agent
agent = KaiaDocAgent(api_key="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")

# Load and process the documentation
agent.load_docs()

# Create an interactive query loop
while True:
    # Get user input
    user_query = input("\nEnter your question about Kaia (or 'quit' to exit): ")
    
    # Check if user wants to quit
    if user_query.lower() in ['quit', 'exit', 'q']:
        print("Goodbye!")
        break
    
    # Query the documentation
    try:
        response = agent.query(user_query)
        print("\nAnswer:", response)
    except Exception as e:
        print(f"\nError: {str(e)}")