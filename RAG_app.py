import os
import sys
import logging
from dotenv import load_dotenv

# mac
dotenv_path = "/".join([os.path.dirname(__file__), ".env"])
load_dotenv(dotenv_path)

def logon():
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
#logon()

if 1:
    from llama_index.core import SimpleDirectoryReader
    from llama_index.core import VectorStoreIndex

    documents = SimpleDirectoryReader("./data/").load_data()
    index = VectorStoreIndex.from_documents(documents)

if 1:
    retriever = index.as_retriever(verbose=True)
    qmsg = "新聞で公表されている情報でも「個人情報」に当たりますか？"
    from llama_index.core.query_engine import RetrieverQueryEngine
    query_engine = RetrieverQueryEngine.from_args(
        retriever,
    )
    print(f"Q: {qmsg}")
    response = query_engine.query(qmsg)
    print("A: " + str(response))