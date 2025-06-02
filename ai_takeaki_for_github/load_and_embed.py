
import os
import glob
import docx2txt
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

def load_documents_from_docs_folder(folder_path):
    documents = []
    for filepath in glob.glob(os.path.join(folder_path, "*.docx")):
        text = docx2txt.process(filepath)
        documents.append(text)
    return documents

def split_texts(texts):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.create_documents(texts)

def load_and_embed():
    docs_path = "docs"
    texts = load_documents_from_docs_folder(docs_path)
    documents = split_texts(texts)

    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(documents, embeddings, persist_directory="chroma_store")
    vectorstore.persist()
    print("✅ ベクトルDBの作成が完了しました。")

if __name__ == "__main__":
    load_and_embed()
