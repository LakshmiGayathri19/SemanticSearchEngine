from flask import Blueprint, render_template, request
from query import get_query_results


views = Blueprint(__name__, "views")

@views.route("/", methods=["Get", "Post"])
def home():
	query = None
	document_texts = None
	if request.method == "POST":
		query = request.form.get("query")
		document_texts = get_related_documents(query)
		    
	return render_template("index.html", query = query, document_texts = document_texts)
    

def get_related_documents(query):
	results = get_query_results(query)
	document_texts = []
	 
	for index in range(len(results['matches'])):
		text = results['matches'][index]['metadata']['text']
		score = results['matches'][index]['score']
		document_texts.append((text, score))
		
	
	return document_texts
	


	
    
