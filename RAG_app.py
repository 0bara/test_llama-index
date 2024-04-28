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

def save_index(doc_dir, id_str, persist_dir):
    """
    文書を読み込み、指定されたディレクトリ（persist_dir）に保存する
    """
    documents = SimpleDirectoryReader(doc_dir).load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.set_index_id(id_str)
    # default of vector_store is SimpleVectorStore
    index.storage_context.persist(persist_dir)

def load_index(id_str, persist_dir):
    """
    指定されたディレクトリ（persist_dir）に保存されたベクトル情報を読み出し、VectorStoreIndexに格納して返却する
    """
    from llama_index.core import (
        StorageContext,
        load_index_from_storage,
    )
    context = StorageContext.from_defaults(persist_dir=persist_dir)
    index = load_index_from_storage(context, id_str)
    return index

if 1:
    from llama_index.core import SimpleDirectoryReader
    from llama_index.core import VectorStoreIndex

    id_str = "vector_index"
    persist_dir = "./storage"

    # (save_indexは)外部文書に変更がある場合のみ実行する
    if 0:
        doc_dir = "./data/"
        save_index(doc_dir, id_str, persist_dir)
    index = load_index(id_str, persist_dir)

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