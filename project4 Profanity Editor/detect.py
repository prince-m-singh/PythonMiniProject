import urllib
def read_text():
	quotes = open("E:\UDACITYML\Programming Foundation\PythonMiniProject\project4 Profanity Editor\movie-quotes\movie_quotes\movie_quotes.txt")
	content_of_file=quotes.read()
	print content_of_file
	quotes.close()
	check_profanity(content_of_file)

def check_profanity(text_to_check):
	#http://www.wdylike.appspot.com/?q=shot
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output = connection.read()
	print output
	connection.close()

read_text ()
