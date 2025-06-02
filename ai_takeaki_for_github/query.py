
import os
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

load_dotenv()

def create_qa_chain():
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma(persist_directory="chroma_store", embedding_function=embeddings)
    retriever = vectorstore.as_retriever()

    prompt_template = """あなたは「晴田武陽」の思想や文章を学んだ分身AI『AIたけあき』です。

以下の質問に対しては、和の心や協調性、人間同士のつながりを大切にする視点から、
「明るい未来」「理想の社会」「日本人の本質」などに関する考察を込めて答えてください。

文体は、やさしく語りかけるように丁寧に。
論理と感性のバランスを意識してください。

参考文書:
{context}

質問: {question}
"""

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=prompt_template
    )

    llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
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

if __name__ == "__main__":
    question = input("質問をどうぞ：")
    print("AIたけあきの回答：", ask_ai(question))
