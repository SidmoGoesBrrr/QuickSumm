from bs4 import BeautifulSoup
from text_summarizer import FrequencySummarizer
import requests
import sys

def getTextFromURL(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")
	text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
	return text

def summarizeURL(url, total_pars):
	url_text = getTextFromURL(url).replace(u"Â", u"").replace(u"â", u"")

	fs = FrequencySummarizer()
	final_summary = fs.summarize(url_text.replace("\n"," "), total_pars)
	return " ".join(final_summary)

