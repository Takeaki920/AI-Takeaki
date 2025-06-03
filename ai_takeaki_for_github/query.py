from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings

import os

def load_vectorstore():
    return FAISS.load_local("faiss_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True)

def create_qa_chain():
    llm = ChatOpenAI(temperature=0)

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
あなたは「AIたけあき」です。以下の文脈に基づいて、誠実かつやさしく回答してください。

{context}

質問: {question}
"""
    )

    vectorstore = load_vectorstore()

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": prompt}
    )

    return qa

def ask_ai(query):
    qa = create_qa_chain()
    return qa.run(query)
