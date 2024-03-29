#!/usr/bin/python3
"""
technical challengese
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    commits = get(url).json()
    try:
        for i in range(10):
            print(
                "{}: {}".format(
                    commits[i].get("sha"),
                    commits[i].get("commit").get("author").get("name"),
                )
            )
    except IndexError:
        pass
