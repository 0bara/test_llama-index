# はじめに
## llama-index を利用して、RAG動作について理解を深めていきたいと思います。

### first step
単純に外部情報から情報検索するだけのコード
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
### second step
情報源を毎回ベクトル化するのはコスト・時間がかかるため、ベクトル化したものを保存し、検索時に読み出す形に
※ ちなみに、回答は日本語でなく、英語で返却されている状態です。
- save_index
  文書を読み込み、指定されたディレクトリ（persist_dir）に保存する
- load_index
  指定されたディレクトリ（persist_dir）に保存されたベクトル情報を読み出し、VectorStoreIndexに格納して返却する
