class Movies:
    """
    Analyzing data from movies.csv
    """
    def __init__(self, path_to_the_file):
        self.__file_name = path_to_the_file

    def __parse_data(self, line):
        line = line.strip()
        index_first = line.find(',')
        index_last = line.rfind(',')
        return int(line[0 : index_first]), line[index_first + 1 : index_last], line[index_last + 1:] 

    def read_file(self):
        with open(self.__file_name, 'r') as file_input:
            if file_input.readline().strip() != 'movieId,title,genres':
                raise Exception('Not valid header in file')
            self.__data = [self.__parse_data(i) for i in file_input.readlines()]

    def dist_by_release(self):
        release_years = {}
        for i in self.__data:
            try:
                date = int(i[1].split('(')[-1].split(')')[0])
            except ValueError:
                print(f"ID {i[0]} haven't date")
            if date in release_years:
                release_years[date] += 1
            else:
                release_years[date] = 1
        return dict(sorted(release_years.items(), key=lambda x: x[1], reverse=True))
    
    def dist_by_genres(self):
        genres = {}
        for i in self.__data:
            for j in i[2].split('|'):
                if j in genres:
                    genres[j] += 1
                else:
                    genres[j] = 1
        return dict(sorted(genres.items(), key=lambda x: x[1], reverse=True))
        
    def most_genres(self, n):
        movies = {}
        for i in self.__data:
            movies[i[0]] = (i[1], len(i[2].split('|')))
        return dict(sorted(movies.values(), key=lambda x: x[1], reverse=True)[:n])

class Links:
    """
    Analyzing data from links.csv
    """
    def __init__(self, path_to_the_file):
        self.__file_name = path_to_the_file
   
    def __parse_data(self, line):
        try:
            data = line.strip().split(',')
            if len(data[0]) == 0 :
                flag = 0
                raise Exception("No MovieID")
            elif len(data[1]) == 0:
                flag = 1
                raise Exception("No ImdbID")
            elif len(data[2]) == 0:
                flag = 1
                raise Exception("No TmdbID")
        except Exception as some:
            print(some)
            if not flag:
                return None
        return data[0], data[1], data[2]

    def read_file(self):
        with open(self.__file_name, 'r') as file_input:
            if file_input.readline().strip() != 'movieId,imdbId,tmdbId':
                raise Exception('Not valid header in file')
            self.__data = [self.__parse_data(i) for i in file_input.readlines()]

    def get_imdb(list_of_movies, list_of_fields):

        """
# The method returns a list of lists [movieId, field1, field2, field3, ...] for the list of movies given as the argument (movieId).
    #     For example, [movieId, Director, Budget, Cumulative Worldwide Gross, Runtime].
    #     The values should be parsed from the IMDB webpages of the movies.
    #  Sort it by movieId descendingly.
    #     """
        return imdb_info
        
    # def top_directors(self, n):
    #     """
    #     The method returns a dict with top-n directors where the keys are directors and 
    #     the values are numbers of movies created by them. Sort it by numbers descendingly.
    #     """
    #     return directors
        
    # def most_expensive(self, n):
    #     """
    #     The method returns a dict with top-n movies where the keys are movie titles and
    #     the values are their budgets. Sort it by budgets descendingly.
    #     """
    #     return budgets
        
    # def most_profitable(self, n):
    #     """
    #     The method returns a dict with top-n movies where the keys are movie titles and
    #     the values are the difference between cumulative worldwide gross and budget.
    #  Sort it by the difference descendingly.
    #     """
    #     return profits
        
    # def longest(self, n):
    #     """
    #     The method returns a dict with top-n movies where the keys are movie titles and
    #     the values are their runtime. If there are more than one version â€“ choose any.
    #  Sort it by runtime descendingly.
    #     """
    #     return runtimes
        
    # def top_cost_per_minute(self, n):
    #     """
    #     The method returns a dict with top-n movies where the keys are movie titles and
# the values are the budgets divided by their runtime. The budgets can be in different currencies â€“ do not pay attention to it. 
    #  The values should be rounded to 2 decimals. Sort it by the division descendingly.
    #     """
    #     return costs

# class Tags:
    # """
    # Analyzing data from tags.csv
    # """
    # def __init__(self, path_to_the_file):
    #     """
    #     Put here any fields that you think you will need.
    #     """
    # def most_words(self, n):
    #     """
    #     The method returns top-n tags with most words inside. It is a dict 
 # where the keys are tags and the values are the number of words inside the tag.
 # Drop the duplicates. Sort it by numbers descendingly.
    #     """
    #     return big_tags

    # def longest(self, n):
    #     """
    #     The method returns top-n longest tags in terms of the number of characters.
    #     It is a list of the tags. Drop the duplicates. Sort it by numbers descendingly.
    #     """
    #     return big_tags

    # def most_words_and_longest(self, n):
    #     """
    #     The method returns the intersection between top-n tags with most words inside and 
    #     top-n longest tags in terms of the number of characters.
    #     Drop the duplicates. It is a list of the tags.
    #     """
    #     return big_tags
        
    # def most_popular(self, n):
    #     """
    #     The method returns the most popular tags. 
    #     It is a dict where the keys are tags and the values are the counts.
    #     Drop the duplicates. Sort it by counts descendingly.
    #     """
    #     return popular_tags
        
    # def tags_with(self, word):
    #     """
    #     The method returns all unique tags that include the word given as the argument.
    #     Drop the duplicates. It is a list of the tags. Sort it by tag names alphabetically.
    #     """
    #     return tags_with_word

# class Ratings:
    # """
    # Analyzing data from ratings.csv
    # """
    # def __init__(self, path_to_the_file):
    #     """
    #     Put here any fields that you think you will need.
    #     """
    # class Movies:    
    #     def dist_by_year(self):
    #         """
    #         The method returns a dict where the keys are years and the values are counts. 
    #         Sort it by years ascendingly. You need to extract years from timestamps.
    #         """
    #         return ratings_by_year
        
    #     def dist_by_rating(self):
    #         """
    #         The method returns a dict where the keys are ratings and the values are counts.
    #      Sort it by ratings ascendingly.
    #         """
    #         return ratings_distribution
        
    #     def top_by_num_of_ratings(self, n):
    #         """
    #         The method returns top-n movies by the number of ratings. 
    #         It is a dict where the keys are movie titles and the values are numbers.
    #  Sort it by numbers descendingly.
    #         """
    #         return top_movies
        
    #     def top_by_ratings(self, n, metric=average):
    #         """
    #         The method returns top-n movies by the average or median of the ratings.
    #         It is a dict where the keys are movie titles and the values are metric values.
    #         Sort it by metric descendingly.
    #         The values should be rounded to 2 decimals.
    #         """
    #         return top_movies
        
    #     def top_controversial(self, n):
    #         """
    #         The method returns top-n movies by the variance of the ratings.
    #         It is a dict where the keys are movie titles and the values are the variances.
    #       Sort it by variance descendingly.
    #         The values should be rounded to 2 decimals.
    #         """
    #         return top_movies

    # class Users:
    #     """
    #     In this class, three methods should work. 
    #     The 1st returns the distribution of users by the number of ratings made by them.
    #     The 2nd returns the distribution of users by average or median ratings made by them.
    #     The 3rd returns top-n users with the biggest variance of their ratings.
    #  Inherit from the class Movies. Several methods are similar to the methods from it.
    #     """

def test_movies():
    movies = Movies("ml-latest-small/movies.csv")
    movies.read_file()
    print(movies.dist_by_release())
    print(movies.dist_by_genres())
    print(movies.most_genres(10))

def test_links():
    links = Links('ml-latest-small/links.csv')
    links.read_file()
    print()

if __name__ == '__main__':
    print("start")
    # test_movies()
    test_links()

