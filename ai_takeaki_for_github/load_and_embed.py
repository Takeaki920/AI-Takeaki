from dotenv import load_dotenv
load_dotenv()
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import DirectoryLoader, Docx2txtLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def load_and_embed():
    # ドキュメントの読み込み（docxとtxtをサポート）
    loaders = [
        DirectoryLoader("docs", glob="**/*.docx", loader_cls=Docx2txtLoader),
        DirectoryLoader("docs", glob="**/*.txt", loader_cls=TextLoader),
    ]
    documents = []
    for loader in loaders:
        documents.extend(loader.load())

    # テキストを分割
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = splitter.split_documents(documents)

    # 埋め込み生成
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)

    # 保存
    vectorstore.save_local("faiss_index")

def load_vectorstore():
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
