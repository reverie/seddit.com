from bs4 import BeautifulSoup
import urllib3

from redditchat.core.models import Room

from script_log import make_logger, log

logger = make_logger('seed_rooms')

#URL = 'http://subredditfinder.com/redditor.php?sort=top&max=1250'
#
#
#def fetch_top_rooms_html():
#    # XXX doesn't work, we get 400, probably a Referer check
#    http = urllib3.PoolManager(headers={'User-Agent': 'Seddit.com - contact andrewbadr@gmail.com'})
#    r = http.request('GET', URL)
#    if r.status != 200:
#        log(logger, 'error', 'Request got error:', r.status, "on url", URL)
#        raise Exception(r.status, URL)
#    return r.data
#
#def extract_room_names(html):
#    result = [] # Use a list to preserve priority
#    soup = BeautifulSoup(html)
#    top = soup.find('a').nextSibling.nextSibling.nextSibling.nextSibling.text
#    result.append(top)
#    for br in soup.find_all('br'):
#        try:
#            result.add(br.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text)
#        except AttributeError:
#            break
#
#    return result

def add_rooms(room_names):
    for n in room_names:
        log(logger, 'debug', 'get or create', n)
        Room.get_or_create_by_shortname(n)

def main():
    #html = fetch_top_rooms_html()
    #room_names = extract_room_names(html)
    room_names = set([u'nyc', u'WikiLeaks', u'DoesAnybodyElse', u'fffffffuuuuuuuuuuuu', u'futurama', u'Military', u'jailbait', u'japan', u'relationships', u'linguistics', u'Diablo', u'Documentaries', u'writing', u'blog', u'woahdude', u'WTF', u'soccer', u'MensRights', u'australia', u'YouShouldKnow', u'opensource', u'webcomics', u'food', u'photography', u'howto', u'trees', u'lolcats', u'geek', u'Jokes', u'newreddits', u'Fitness', u'Demotivational', u'cogsci', u'freebies', u'arresteddevelopment', u'gifs', u'Art', u'motorcycles', u'nfl', u'Marijuana', u'magicTCG', u'WeAreTheMusicMakers', u'4chan', u'AskReddit', u'compsci', u'zombies', u'javascript', u'Libertarian', u'Health', u'economy', u'StarWars', u'google', u'unitedkingdom', u'energy', u'sex', u'books', u'dubstep', u'TwoXChromosomes', u'PS3', u'Android', u'hockey', u'wallpaper', u'canada', u'humor', u'psychology', u'entertainment', u'skeptic', u'wow', u'wikipedia', u'Freethought', u'malefashionadvice', u'Ubuntu', u'gamedev', u'cars', u'worldnews', u'Sexy', u'Astronomy', u'guns', u'math', u'tattoos', u'biology', u'bestof', u'techsupport', u'business', u'ronpaul', u'Metal', u'Economics', u'circlejerk', u'answers', u'Frugal', u'news', u'doctorwho', u'lgbt', u'recipes', u'programming', u'personalfinance', u'creepy', u'pics', u'itookapicture', u'anime', u'Bad_Cop_No_Donut', u'GameDeals', u'battlestations', u'software', u'learnprogramming', u'apple', u'TrueReddit', u'drunk', u'todayilearned', u'coding', u'Graffiti', u'community', u'Buddhism', u'Music', u'startrek', u'rpg', u'linux', u'harrypotter', u'pokemon', u'xkcd', u'tf2', u'environment', u'Drugs', u'Physics', u'seduction', u'Homebrewing', u'sports', u'Guitar', u'Autos', u'beer', u'cats', u'iphone', u'WebGames', u'web_design', u'investing', u'happy', u'tipofmytongue', u'collapse', u'swtor', u'shittyadvice', u'somethingimade', u'relationship_advice', u'xbox360', u'IndieGaming', u'Christianity', u'PhilosophyofScience', u'obama', u'hardware', u'worldpolitics', u'science', u'offbeat', u'movies', u'socialism', u'video', u'MMA', u'history', u'Design', u'videos', u'FoodPorn', u'Cooking', u'gadgets', u'engineering', u'conspiracy', u'DIY', u'politics', u'technology', u'nba', u'starcraft', 'funny', u'netsec', u'electronicmusic', u'bicycling', u'Python', u'self', u'IAmA', u'zelda', u'comics', u'scifi', u'announcements', u'wallpapers', u'gaming', u'sysadmin', u'Anarchism', u'reddit.com', u'aww', u'askscience', u'philosophy', u'running', u'Games', u'comicbooks', u'Minecraft', u'photos', u'space', u'atheism', u'AMA', u'secretsanta', u'listentothis', u'chemistry', u'tldr', u'travel'])
    add_rooms(room_names)


if __name__ == '__main__':
    main()
