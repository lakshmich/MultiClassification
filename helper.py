import contractions
from bs4 import BeautifulSoup
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import ToktokTokenizer


def process_and_save_data(text):

	# remove contractions
	data = contractions.fix(text)
	
	# remove html
	data = BeautifulSoup(data, "html.parser").get_text()
	
	# remove special characters
	pattern = r'[^a-zA-Z0-9]'
	data = re.sub(pattern, '', data)
	
	# remove punctuation
	data = ''.join([c for c in data if c is not in string.punctuation])
	
	# remove stopwords
	sw = stopwords.words("english")
	sw.remove("not")
	
	tokenizer = ToktokTokenizer()
	tokens = tokenizer.tokenize(data.lower())
	data = [word for word in tokens if not in sw]
	data = ' '.join(data)
	
	return data	
	