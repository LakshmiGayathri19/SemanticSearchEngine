# Semantic Search Engine
A search engine build using AI technology to search for the text documents relevant to the input query. It uses `sentence transformer` model to encode the text documents. The embeddings of text documents are stored in vector database (`Pinecone` in this case) such that it is easy to find the relevant documents. Vector databases like Pinecone handle the embeddings by offering optimized storage and querying capabilities. Vector databases have the capabilities of a traditional database that are absent in standalone vector indexes and the specialization of dealing with vector embeddings, which traditional scalar-based databases lack.

When the user issues a query, the search engine uses the same embedding model to create embeddings for the query, and use those embeddings to query the database for similar vector embeddings. After the similar vector embeddings are returned by the vector database, the text documents of those embeddings are retrieved from the metadata associated with those embeddings. Later the text documents are displayed to the end user.

---

### How to run the code

Step 1) Create a [python virtual environment](https://docs.python.org/3/library/venv.html) in your project folder. 

Step 2) Install the required libraries. You can either follow Option-A or Option-B.

**Note:** It is assumed that python is already installed in your virtual environment.

*Option-A*

* `pip install pinecone-client` -> This installs `pinecone` client which is a vector database.
* `pip install sentence-transformers` -> This installs a python [framework](https://www.sbert.net/) which is used to encode text documents and produce embeddings.
* `pip install flask` -> This command installs a lightweight [web application framework](https://pypi.org/project/Flask/).

Or

*Option-B*

* `requirements.txt` can be executed directly with the command `pip install -r requirements.txt`.

Step 3) 
* Download the `Data` folder. After the data folder is downloaded, replace the folder name at this [line](https://github.com/LakshmiGayathri19/SemanticSearchEngine/blob/5eafae6d05b62682d4d9c3d2ad4446d628af90c7/application_code.py#L23) in `application_code.py`.
For example: If you have the `Data` folder under `folder_1` directory, replace the `folder_name` with `folder_1/Data/`. 
* Create an account in [Pinecone.io](https://app.pinecone.io/) to get the free API key and the enviroment name. After creating the account, copy the API key and enviroment name at this [line](https://github.com/LakshmiGayathri19/SemanticSearchEngine/blob/main/application_code.py#L9-L10).
* In order to store the data we need an index created in Pinecone. So give an index_name and place it at this [line](https://github.com/LakshmiGayathri19/SemanticSearchEngine/blob/main/application_code.py#L11), such that when the `application_code.py` is run the index with the specified name gets created.

Step 4) Run the `setup.py` file using the command `python setup.py`. `Setup.py` file makes a call to main method of `semantic_search` class present in `application_code.py`. The sequence of operation performed inside main method are
1) `SentenceTransformer` model is created. This model is imported from the `sentence-transformers` framework.
2) The pinecone is initialised.
3) With the help of the model created in the above step, a index is initialized in the pinecone.
4) Documents which are to be added to the vector database are read and the text is stored in the list named `documents`.
5) Each document text read in the step 4 are converted into embeddings using the model created in the step 1. The created embeddings along with the metadata(creation of metadata can be found [here](https://github.com/LakshmiGayathri19/SemanticSearchEngine/blob/main/application_code.py#L68)) is inserted into the vector database index created in step 3.

For example: The entry to the vector database will be of the form:
```
{
    'id': '99',
    'metadata': {'text': 'Day-Lewis set for Berlin honour....'},
    'score': 0.549687684,
    'value': [0.027540016919374466, -0.04051943123340607, -0.03708145394921303,...] #embeddings
}
```

After successfully cpompleting the above mentioned steps, the database is ready with all the document which can be queried by the user. Now in order to start the website run `python app.py`. This will start a local webserver at `port 8000`. The website looks like the below attached picture.

![searchEngine](https://github.com/LakshmiGayathri19/SemanticSearchEngine/blob/main/SearchEngine.png)


The resutls of the input query are shown in the cards along with the score of how accurately the document text matched with the input query. Currently the website returns five relevant text documents. We can customise this by chaning the value of `top_k` at this [line](https://github.com/LakshmiGayathri19/SemanticSearchEngine/blob/main/query.py#L13).

**Note:** For now the UI of the search engine is kept simple :")


