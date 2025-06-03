from dotenv import load_dotenv
load_dotenv()
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import OpenAIEmbeddings

def load_vectorstore():
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local("faiss_index", embeddings)

def create_qa_chain():
    llm = ChatOpenAI(temperature=0)

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
あなたは「AIたけあき」です。
以下の文脈に基づいて、誠実かつやさしく、わかりやすく回答してください。
必要に応じて、Takeakiさんの価値観やスタイルも大切にしてください。

【文脈】
{context}

【質問】
{question}

【回答】
"""
    )

    vectorstore = load_vectorstore()

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=False
    )

    return qa

def ask_ai(query):
    qa = create_qa_chain()
    response = qa.run(query)
    return response
