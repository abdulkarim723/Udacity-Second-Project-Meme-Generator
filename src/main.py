import argparse
from meme import generate_meme

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, help="path to an image file")
    parser.add_argument("--body", type=str,
                        help="quote body to add to the image")
    parser.add_argument("--author", type=str,
                        help="quote author to add to the image")
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
