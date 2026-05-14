import os
import string
import requests
from bs4 import BeautifulSoup


headers = {"Accept-Language": "en-US,en;q=0.5"}
base_dir = os.path.dirname(os.path.abspath(__file__))


def get_user_input():
    print("Enter number of pages, for example: 4")
    while True:
        try:
            pages = int(input("> "))
            break
        except ValueError:
            print("Please enter a number")

    print("Enter article type, for example:")
    print("News")
    print("Nature Briefing")
    print("Research Highlight")
    article_type = input("> ")

    return pages, article_type


def create_folder(page):
    folder_name = f"Page_{page}"
    folder_path = os.path.join(base_dir, folder_name)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    return folder_path


def clean_file_name(title):
    clean_title = title.translate(str.maketrans("", "", string.punctuation))
    clean_title = clean_title.replace(" ", "_")
    return clean_title + ".txt"


def save_article(folder_path, title, text):
    file_name = clean_file_name(title)
    file_path = os.path.join(folder_path, file_name)

    file = open(file_path, "w", encoding="utf-8")
    file.write(text)
    file.close()


def parse_pages(pages, article_type):
    for page in range(1, pages + 1):
        folder_path = create_folder(page)

        url = f"https://www.nature.com/nature/articles?sort=PubDate&year=2022&page={page}"
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article")

        for article in articles:
            article_type_tag = article.find("span", {"data-test": "article.type"})

            if article_type_tag:
                current_type = article_type_tag.text.strip()

                if current_type == article_type:
                    link_tag = article.find("a", {"data-track-action": "view article"})

                    if link_tag:
                        article_link = "https://www.nature.com" + link_tag.get("href")
                        article_response = requests.get(article_link, headers=headers)

                        article_soup = BeautifulSoup(article_response.text, "html.parser")

                        title_tag = article_soup.find("title")

                        if title_tag:
                            title = title_tag.text.strip()
                        else:
                            title = "article"

                        body = article_soup.find("div", class_=lambda x: x and "body" in x)

                        if body:
                            article_text = body.text.strip()
                            save_article(folder_path, title, article_text)


pages, article_type = get_user_input()
parse_pages(pages, article_type)

print("Saved all articles.")