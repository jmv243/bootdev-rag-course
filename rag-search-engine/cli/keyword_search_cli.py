#!/usr/bin/env python3

import argparse
import json
import string

stop_words = []

def remove_stop_words(tokens: list[str]):
    if len(stop_words) < 1:
        with open('./data/stopwords.txt', 'r') as file:
            for line in file:
                stop_words.append(line.strip())
    
    for token in tokens:
        if token in stop_words:
            tokens.remove(token)

def search_movies(query: str):
    with open('./data/movies.json', 'r') as file:
        data = json.load(file)           

    translator = str.maketrans('', '', string.punctuation)
    

    #clean and get query tokens
    query_clean = query.lower().translate(translator)
    query_tokens = query_clean.split(' ')

    #remove stop words in memory 
    remove_stop_words(query_tokens)

    hits = 0
    for movie in data['movies']:
        if hits >= 5:
            return
        
        title_clean = movie['title'].lower().translate(translator)        

        for qt in query_tokens:
            if qt in title_clean:
                print(movie['title'])
                hits += 1 
                break

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            # print the search query here
            print('Searching for:', args.query)
            pass
        case _:
            parser.print_help()

    search_movies(args.query)

if __name__ == "__main__":
    main()