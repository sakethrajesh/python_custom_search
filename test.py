from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader
import os

os.environ['OPENAI_API_KEY'] = ''

documents = SimpleDirectoryReader('data').load_data()

index = GPTSimpleVectorIndex.from_documents(documents)

while True:
    prompt = input("Type prompt...\n")
    response = index.query(prompt)
    print(response)
    print('_______________________')
