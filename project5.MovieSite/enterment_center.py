import media
import fresh_tomatoes

toy_story=media.Movie("Toystory",
	"a story of boy",
	"http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print toy_story.storyline
#toy_story.show_trailer()

movie=[toy_story]
fresh_tomatoes.open_movies_page(movie)