from application_code import semantic_search
import pinecone

'''
Query the vector database and return top five matching documents for the given query.
'''
def get_query_results(query):
	ss_obj = semantic_search()
	ss_obj.init_pinecone()
	index = pinecone.Index(ss_obj.index_name)
	model = semantic_search.model_creation(ss_obj)	
	xq = model.encode(query).tolist()
	return index.query(xq, top_k=5, include_metadata=True)
