from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from load_and_embed import load_vectorstore

def create_qa_chain():
    llm = ChatOpenAI(temperature=0)

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
あなたは「AIたけあき」です。以下の文脈に基づいて、誠実かつやさしく回答してください。

文脈:
{context}

質問:
{question}
""")

    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever()

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    )

    return qa

def ask_ai(query):
    qa = create_qa_chain()
    return qa.run(query)
