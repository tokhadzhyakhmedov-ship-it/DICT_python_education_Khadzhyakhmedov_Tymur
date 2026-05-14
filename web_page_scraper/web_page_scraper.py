import os
import string
import requests
from bs4 import BeautifulSoup


while True:
    try:
        pages = int(input("> "))
        break
    except ValueError:
        print("Please enter a number")

article_type = input("> ")

headers = {"Accept-Language": "en-US,en;q=0.5"}

for page in range(1, pages + 1):
    folder_name = f"Page_{page}"

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

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

                        clean_title = title.translate(
                            str.maketrans("", "", string.punctuation)
                        )
                        clean_title = clean_title.replace(" ", "_")

                        file_path = os.path.join(folder_name, f"{clean_title}.txt")

                        file = open(file_path, "w", encoding="utf-8")
                        file.write(article_text)
                        file.close()

print("Saved all articles.")