#!/usr/bin/env python3

import argparse
import json
import string

def search_movies(query: str):
    data = {}
    with open('./data/movies.json', 'r') as file:
        data = json.load(file)       

    translator = str.maketrans('', '', string.punctuation)
    hits = 0
    for movie in data['movies']:
        query_clean = query.lower().translate(translator)
        title_clean = movie['title'].lower().translate(translator)
        if query_clean in title_clean:
            print(movie['title'])
            hits += 1

        if hits >= 5:
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