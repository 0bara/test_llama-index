# llama-index を利用して、RAG動作について理解を深めていきたいと思います。

- data
dataには、個人情報保護委員会（PPC）にある<a href="https://www.ppc.go.jp/personalinfo/contact/">FAQ</a>にある「金融機関における個人情報保護に関するQ&A」のPDF版を利用

- requirements.txt
 上記pdfを読み出す際に、cryptograpyが必要

- この状態での動作は以下の通り
+ data以下にあるファイルを読み出し、埋め込みモデルを利用してベクトル化
  というのが以下の２行
    ```python
    documents = SimpleDirectoryReader("./data/").load_data()
    index = VectorStoreIndex.from_documents(documents)
    ```
+ 問い合わせする文章を埋め込みモデルを利用してベクトル化する。
　そのベクトルと、上記で計算したベクトル全てに対して（default）cos類似度を計算する
+ 大きいものから順にk個取得し、その情報を元に LLMを利用して回答を生成する
　この２行のことを、以下の１行で実施している　
    ```python
    response = query_engine.query(qmsg)
    ```
