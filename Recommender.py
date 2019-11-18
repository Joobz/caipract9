import csv
import math as math

"""implements a recommender system built from
   a movie list name
   a listing of userid+movieid+rating"""
class Recommender(object):

    #"""initializes a recommender from a movie file and a ratings file"""
    def __init__(self,movie_filename,rating_filename):

        # read movie file and create dictionary _movie_names
        self._movie_names = {}
        with open(movie_filename,"r",encoding="utf8") as david:
            alex = csv.reader(david)
            next(alex, None)
            for line in alex:
                movieid = line[0]
                moviename = line[1]
                # ignore line[2], genre
                self._movie_names[movieid] = moviename
                
            # read rating file and create _movie_ratings (ratings for a movie)
            # and _user_ratings (ratings by a user) dicts
        with open(rating_filename,"r",encoding="utf8") as david:
            alex = csv.reader(david)
            next(alex, None)
            self._movie_ratings = {}
            self._user_ratings = {}
            self._movie_ratings_dict = {}
            self._user_ratings_dict = {}

            for line in alex:
                userid = line[0]
                movieid = line[1]
                rating = line[2]
                # ignore line[3], timestamp
                if userid in self._user_ratings:
                    userrats = self._user_ratings[userid]
                else:
                    userrats = []
                    self._user_ratings_dict = {}
                userrats.append((movieid,rating))
                self._user_ratings[userid] = userrats
                
                if movieid in self._movie_ratings:
                    movierats = self._movie_ratings[movieid]
                else:
                    movierats = []
                    self._movie_raings_dict = {}
                movierats.append((userid,rating))
                self._movie_ratings[movieid] = movierats

                self._user_ratings_dict[userid][movieid] = rating
                self._movie_ratings_dict[movieid][userid] = rating
 
            
    """returns a list of pairs (userid,rating) of users that
       have rated movie movieid"""
    def get_movie_ratings(self,movieid):
        if movieid in self._movie_ratings:
            return self._movie_ratings[movieid]
        return None
    
    """returns a list of pairs (movieid,rating) of movies
       rated by user userid"""
    def get_user_ratings(self,userid):
        if userid in self._user_ratings:
            return self._user_ratings[userid]
        return None

    """returns the list of user id's in the dataset"""
    def userid_list(self):
        return self._user_ratings.keys()

    """returns the list of movie id's in the dataset"""
    def movieid_list(self):
        return self._movie_ratings.keys()

    """returns the name of movie with id movieid"""
    def movie_name(self,movieid):
        if movieid in self._movie_names:
            return self._movie_names[movieid]
        return None

    def user_similarity(self,userida,useridb):
        ratingsa = self.get_user_ratings(userida)
        ratingsa.sort(key = lambda x: x[1])
        meana = sum(float(x[1]) for x in ratingsa.values())/len(ratingsa)

        ratingsb = self.get_user_ratings(useridb)
        ratingsb.sort(key = lambda x: x[1])
        meanb = sum(float(x[1]) for x in ratingsb.values())/len(ratingsb)
        num = 0
        vara = 0
        varb = 0
        for id in self.movieid_list():
            if id in self._user_ratings_dict[userida] and id in self._user_ratings_dict[useridb]:
                num += ((float(self._user_ratings_dict[userida][id])-meana)*
                        (float(self._user_ratings_dict[useridb][id])-meanb))
                vara += (float(self._user_ratings_dict[userida][id])-meana)**2
                varb += (float(self._user_ratings_dict[userida][id])-meana)**2

        vara = math.sqrt(vara)
        varb = math.sqrt(varb)


        num = sum()

    """returns a list of at most k pairs (movieid,predicted_rating)
       adequate for a user whose rating list is rating_list"""
    def recommend_user_to_user(self,rating_list,k):
        pass

    """returns a list of at most k pairs (movieid,predicted_rating)
       adequate for a user whose rating list is rating_list"""
    def recommend_item_to_item(self,rating_list,k):
        pass

def main():
    r = Recommender("ml-latest-small/movies.csv","ml-latest-small/ratings.csv")
    print(len(r.movieid_list())," movies with ratings from ",len(r.userid_list()),"different users")
    print("The name of movie 5 is: ",r.movie_name("5"))
    #print("movie 5 was recommended by ",r.get_movie_ratings("5"))
    #print("user 1 recommended movies ",r.get_user_ratings("1"))

main()

