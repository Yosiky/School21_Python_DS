from collections import Counter, defaultdict
from datetime import datetime
import statistics
import re

class Movies:
    """
    analyzing data from movies.csv
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
            if file_input.readline().strip() != 'movieid,title,genres':
                raise exception('not valid header in file')
            self.__data = [self.__parse_data(i) for i in file_input.readlines()]

    def dist_by_release(self):
        release_years = {}
        for i in self.__data:
            try:
                date = int(i[1].split('(')[-1].split(')')[0])
            except valueerror:
                print(f"id {i[0]} haven't date")
            if date in release_years:
                release_years[date] += 1
            else:
                release_years[date] = 1
        return dict(sorted(release_years.items(), key=lambda x: x[1], reverse=true))
    
    def dist_by_genres(self):
        genres = {}
        for i in self.__data:
            for j in i[2].split('|'):
                if j in genres:
                    genres[j] += 1
                else:
                    genres[j] = 1
        return dict(sorted(genres.items(), key=lambda x: x[1], reverse=true))
        
    def most_genres(self, n):
        movies = {}
        for i in self.__data:
            movies[i[0]] = (i[1], len(i[2].split('|')))
        return dict(sorted(movies.values(), key=lambda x: x[1], reverse=true)[:n])

class Links:
    """
    Analyzing data from links.csv
    """
    def __init__(self, path_to_the_file):
        self.__file_name = path_to_the_file

    def __parse_data(self, line):
        try:
            data = line.strip().split(',')
            if len(data[0]) == 0:
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

    def get_imdb(self, list_of_movies, list_of_fields):

        imdb_info = [self.__get_imdb_movie_info(data, list_of_fields)
                     for data in self.get_next_data_line()
                     if data[0] in list_of_movies]
        return list(sorted(imdb_info, key=lambda fields: fields[0]))
    def top_directors(self, n):

     directors_list = [self.__get_imdb_movie_info(data, ['Director'])
                       for data in self.get_next_data_line()]
     directors_list = map(lambda pair: pair[1], directors_list)
     directors_counter = Counter(directors_list)
     return dict(directors_counter.most_common(n))

    def most_expensive(self, n):
        budgets = [self.__get_imdb_movie_info(data, ['Budget'])
                   for data in self.get_next_data_line()]
        budgets = map(lambda item: (
            self.movies_cls.get_movie_title(self.__csv_types[0](item[0])),
            item[1] if item[1] is not None else ''
        ), budgets)
        return dict(sorted(budgets, key=lambda item: item[1], reverse=True)[:n])

    def most_profitable(self, n):
        profits = []
        for data in self.get_next_data_line():
            info = self.__get_imdb_movie_info(data, ['Gross worldwide', 'Budget'])

            if info[1] is None or info[2] is None:
                profits.append([self.movies_cls.get_movie_title(data[0]), float('NaN')])
                continue

            values = (float(re.sub(r'[^\d.]', '', info[1])), float(re.sub(r'[^\d.]', '', info[2])))
            profits.append([
                self.movies_cls.get_movie_title(data[0]),
                round(values[0] - values[1], 2)])

        return dict(sorted(profits, key=lambda item: item[1] if item[1] is not None else '', reverse=True)[:n])

    def longest(self, n):

        runtimes = [self.__get_imdb_movie_info(data, ['Runtime'])
                    for data in self.get_next_data_line()]
        runtimes = map(lambda item: (
                        self.movies_cls.get_movie_title(self.__csv_types[0](item[0])),
                        item[1]
                    ), runtimes)

    def top_cost_per_minute(self, n):

        costs = []
        for data in self.get_next_data_line():
            info = self.__get_imdb_movie_info(data, ['Budget', 'Runtime'])

            if info[1] is None or info[2] is None:
                costs.append([self.movies_cls.get_movie_title(data[0]), float('NaN')])
                continue

            budget_value = float(re.sub(r'[^\d.]', '', info[1]))
            runtime_value = info[2].split()
            runtime_value = int(runtime_value[0]) * 60 + int(runtime_value[2])
            costs.append([
                self.movies_cls.get_movie_title(data[0]),
                round(budget_value / runtime_value, 2)])

        return dict(sorted(costs, key=lambda item: item[1] if item[1] is not None else '', reverse=True)[:n])

class Tags:
    """
    analyzing data from tags.csv
    """
    def __init__(self, path_to_the_file):
        self.__file_name = path_to_the_file

    def __parse_data(self, line):
        line = line.strip().split(',')
        line[2] = line[2].lower()
        line[2] = " ".join(list(sorted(re.findall("\w+[-*\w+]{0,}", line[2]))))
        return int(line[0]), int(line[1]), line[2], line[3]

    def read_file(self):
        with open(self.__file_name, 'r') as file_input:
            if file_input.readline().strip() != 'userId,movieId,tag,timestamp':
                raise exception('not valid header in file')
            self.__data = [self.__parse_data(i) for i in file_input.readlines()]

    def most_words(self, n):
        #mb rewrite parser tag
        """
        The method returns top-n tags with most words inside. It is a dict 
 where the keys are tags and the values are the number of words inside the tag.
 Drop the duplicates. Sort it by numbers descendingly.
        """
        big_tags = defaultdict(int)
        for i in self.__data:
            big_tags[i[2]] = max(big_tags[i[2]], len(i[2].split(' ')))
        return dict(list(sorted(big_tags.items(), key=lambda x : x[1], reverse=True))[:n])

    def longest(self, n):
        """
        The method returns top-n longest tags in terms of the number of characters.
        It is a list of the tags. Drop the duplicates. Sort it by numbers descendingly.
        """
        big_tags = defaultdict(int)
        for i in self.__data:
            big_tags[i[2]] = max(big_tags[i[2]], len(i[2]))
        return dict(list(sorted(big_tags.items(), key=lambda x: x[1], reverse=True))[:n])

    def most_words_and_longest(self, n):
        """
        The method returns the intersection between top-n tags with most words inside and 
        top-n longest tags in terms of the number of characters.
        Drop the duplicates. It is a list of the tags.
        """
        one = set(self.most_words(n).keys())
        two = set(self.longest(n).keys())
        return sorted(list(one & two), key=len, reverse=True)
        
        
    def most_popular(self, n):
        """
        The method returns the most popular tags. 
        It is a dict where the keys are tags and the values are the counts.
        Drop the duplicates. Sort it by counts descendingly.
        """
        popular_tags = defaultdict(int)
        for i in self.__data:
            popular_tags[i[2]] += 1
        return dict(list(sorted(popular_tags.items(), key=lambda x : x[1], reverse=True))[:n])

        
    def tags_with(self, word):
        return list(sorted(list(set(re.findall("\w+[-*\w+]{0,}", word)))))

class Ratings:
    """
    Analyzing data from ratings.csv
    """
    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        self.__file_name = path_to_the_file

    def __parse_data(self, line):
        line = line.strip().split(',')
        return int(line[0]), int(line[1]), float(line[2]), int(line[3])

    def read_file(self):
        with open(self.__file_name, 'r') as file_input:
            if file_input.readline().strip() != 'userId,movieId,rating,timestamp':
                raise exception('not valid header in file')
            self.__data = [self.__parse_data(i) for i in file_input.readlines()]

    class Movies:
        def dist_by_year(self):
            """
            The method returns a dict where the keys are years and the values are counts. 
            Sort it by years ascendingly. You need to extract years from timestamps.
            """
            ratings_by_year = defaultdict(int)
            for i in self.__data:
                year = datetime.fromtimestamp(i[3]).date.year
                ratings_by_year[year] += 1
            return dict(sorted(ratings_by_year.items()))
        
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

# class Users(Movies):

#     def dist_by_ratings_number(self):
#         ratings_distribution = Counter()

#         for data in self.ratings.get_next_data_line():
#             ratings_distribution[data[0]] += 1

#         return dict(sorted(ratings_distribution.items(), key=lambda item: item[1]))

#     def dist_by_ratings_values(self, metric=statistics.average):

#         all_ratings = defaultdict(list)

#         for data in self.ratings.get_next_data_line():
#             all_ratings[data[0]].append(data[2])

#         for user in all_ratings:
#             all_ratings[user] = round(metric(all_ratings[user]), 2)

#         return dict(sorted(all_ratings.items(), key=lambda item: item[1]))

#     def top_by_variance(self, n: int):

#         all_ratings = defaultdict(list)

#         for data in self.ratings.get_next_data_line():
#             all_ratings[data[1]].append(data[2])

#         for user in all_ratings:
#             all_ratings[user] = round(statistics.variance(all_ratings[user]), 2)

#         return dict(sorted(all_ratings.items(), key=lambda item: item[1], reverse=True)[:n])

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

def test_tags():
    tags = Tags("ml-latest-small/tags.csv")
    tags.read_file()
    some = tags.most_words(10)
    print(some)
    print(tags.longest(10))
    print(tags.most_words_and_longest(10))
    print(tags.most_popular(10))
    print(tags.tags_with(list(some.keys())[0]))

def test_ratings():
    ratings = Ratings("ml-latest-small/ratings.csv")
    ratings.read_file()
    print(ratings.Movies.dist_by_year())


if __name__ == '__main__':
    print("start")
    # test_movies()
    # test_links()
    # test_tags()
    test_ratings()

