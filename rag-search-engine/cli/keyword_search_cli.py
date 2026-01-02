#!/usr/bin/env python3

import argparse
import json


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

    #code added for simple search
    data = {}
    with open('./data/movies.json', 'r') as file:
        data = json.load(file)       

    hits = 0
    for movie in data['movies']:
        if args.query in movie['title']:
            print(movie['title'])
            hits += 1

        if hits >= 5:
            break

if __name__ == "__main__":
    main()