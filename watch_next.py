import spacy


movies = {}
with open("movies.txt", "r") as read_movies:
    # Read the file
    movie_list = read_movies.readlines()

    # Remove any newline characters.
    movie_list = [i.replace("\n", "") for i in movie_list]

    # {Movie: Description}
    movies = {i.split(" :", 1)[0]: i.split(" :", 1)[1] for i in movie_list}


def find_similar_movie(input_description):
    # Load the English language NLP
    nlp = spacy.load('en_core_web_md')

    # Find a similar movie based on the input description.
    nlp_desc = nlp(input_description)
    
    # get token of all movies.
    all_movie_tokens = {i: nlp(x) for i, x in movies.items()}
    
    # Compare input to movies and sort by most/ least similar.
    most_similar_title = None
    most_similar_similarity = 0
    for title, token in all_movie_tokens.items():
        # Set most similar if not set yet.
        if not most_similar_title:
            most_similar_title = title
        # Compare.
        # If similarity is higher, replace
        similarity = nlp_desc.similarity(token)
        if similarity > most_similar_similarity:
            most_similar_similarity = similarity
            most_similar_title = title
            
    return most_similar_title
    
    
    
# Task description and title.
user_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"

user_title = "Planet Hulk"

# See which movie is most similar!
most_similar_found = find_similar_movie(input_description=user_description)

print("'{}' is most similar to '{}'".format(user_title, most_similar_found))
print("\nDescription:\n")
print(movies.get(most_similar_found))
    