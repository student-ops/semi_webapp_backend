import os
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index import StorageContext, load_index_from_storage
from llama_index import (
    GPTVectorStoreIndex,
    LLMPredictor,
    ServiceContext,
    StorageContext,
    load_index_from_storage,
)
from src.llama import utils

def InitIndex(bot_name):
    print("init index")
    print(os.getenv("INDEX_PATH"))
    index_path = os.getenv("INDEX_PATH")
    index_path = index_path + "/" + bot_name
    print(index_path)
    
    # indexが存在する場合
    if os.path.isfile(index_path + "/vector_store.json"):
        print("index exists")
        storage_context = StorageContext.from_defaults(
            persist_dir=index_path)
        index = load_index_from_storage(storage_context)
    else:
        print("index not found")
        data_path = os.getenv("DATA_PATH") +"/" + bot_name
        print(data_path)
        documents = SimpleDirectoryReader(data_path).load_data()

        index = GPTVectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=index_path)
    return index


def LlamaChat(bot_name, question):
    model_name = "text-davinci-003"
    model_temperature = 0

    api_key = os.getenv("OPENAI_API_KEY")

    print("Before calling InitIndex")
    index = InitIndex(bot_name=bot_name)
    print("After calling InitIndex")

    print(index)
    llm = utils.get_llm(model_name, model_temperature, api_key)
    service_context = ServiceContext.from_defaults(
        llm_predictor=LLMPredictor(llm=llm))
    if (index == None):
        yield f"BOT not found eorror"
        return

    query_engine = index.as_query_engine(
        streaming=True,
        similarity_top_k=2,
        service_context=service_context
    )
    response = query_engine.query(question)
    for text in response.response_gen:
        yield text
if __name__ == "__main__":
    question = "どのような人材を目指していますか"
    question += " 日本語で回答して"
    bot_name = "faculty"
    try:
        response = LlamaChat(bot_name, question)
        print(response)
        for response in response:
            print(response, end="", flush=True)
    except Exception as e:
        print("An error occurred: ", str(e))
    # InitIndex("faculty")
