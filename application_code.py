from sentence_transformers import SentenceTransformer
import torch
import pinecone
from tqdm.auto import tqdm

class semantic_search:
	def __init__(self):
		self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
		self.api_key = "your_api_key"
		self.env = "your_env_name"
		self.index_name = 'your_index_name'
		
		
	def main(self):
		# creating sequence_transformer model
		model = model_creation(self)
		
		# creating vector database instance
		init_pinecone(self)
		create_index(self, model)
		
		# reading text documents from the specified directory
		folder_name = "Your_folder_name"
		documents = read_documents(self, folder_name)
		
		# Inserting the encodings of the documents into the vector database.
		index = insert_encodings(self, documents, model)
		
	
	def model_creation(self):
		if self.device != 'cuda':
			print(f"You are using {self.device}. This is much slower than using "
		  		"a CUDA-enabled GPU. If on Colab you can change this by "
		  		"clicking Runtime > Change runtime type > GPU.")

		model = SentenceTransformer('all-MiniLM-L6-v2', device=self.device)
		return model
	
	def init_pinecone(self):
		pinecone.init(api_key=self.api_key, environment=self.env)
	
	def create_index(self, model):
		# only create index if it doesn't exist
		if index_name not in pinecone.list_indexes():
			pinecone.create_index(
			name=self.index_name,
			dimension=model.get_sentence_embedding_dimension(),
			metric='cosine')
	
	def read_documents(self, required_folder):
		documents = []

		for doc in os.listdir(required_folder):
			my_file = open(required_folder + "/" + doc, "r")
			data = my_file.read()
			documents.append(data)
			
		return documents

	'''
	Uses the sequence_transformer model to generate encodings of the documents and inserts the encodings along with the metadata into 		the vector database.
	'''	
	def insert_encodings(self, documents, model):
		#Connecting to index
		index = pinecone.Index(self.index_name)
		records = []
		for i in tqdm(range(0, len(documents))):
			metadata = {'text': documents[i]}
			# create embeddings
			xc = model.encode(documents[i])
			# create records list for upsert
			records.append((str(i), xc.tolist(), metadata))
	    
		# upsert to Pinecone
		index.upsert(vectors=records)
		return index
	







