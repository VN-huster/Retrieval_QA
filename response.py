from langchain.document_loaders import JSONLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings import CacheBackedEmbeddings
from langchain.vectorstores import FAISS
from langchain.storage import LocalFileStore

import pickle
import json
data = "ĐTĐH.json"

"""
loader = JSONLoader(
    file_path='ĐTĐH.json',
    jq_schema='.[].Question',
    text_content=False)
data = loader.load()




text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=50)

all_splits = text_splitter.split_documents(data)



store = LocalFileStore("./cache/")

model_name = "VoVanPhuc/sup-SimCSE-VietNamese-phobert-base"
model_kwargs = {"device": "cuda"}

embeddings = HuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs)

embedder = CacheBackedEmbeddings.from_bytes_store(
    embeddings,
    store,
)

# storing embeddings in the vector store
vectorstore = FAISS.from_documents(data, embedder)
with open('vectorstore.pickle', 'wb') as handle:
    pickle.dump(vectorstore, handle, protocol=pickle.HIGHEST_PROTOCOL)
"""
def make_question(json_file=data):
    # Read JSON from a file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # 'data' now contains the Python representation of the JSON data
    result_dict = {item["Question"]: item["Answer"] for item in data}
    return result_dict

QA = make_question()

with open('vectorstore.pickle', 'rb') as handle:
    vectorstore = pickle.load(handle)

def answer(query):
    search_result = vectorstore.similarity_search(query, k=1)
    return QA[search_result[0].page_content]


