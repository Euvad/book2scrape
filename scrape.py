import os
import csv
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"


def get_soup(url):
    """
    Obtient l'objet BeautifulSoup à partir de l'URL fournie.

    Args:
        url (str): L'URL à partir de laquelle obtenir l'objet BeautifulSoup.

    Returns:
        BeautifulSoup: L'objet BeautifulSoup représentant le contenu HTML de la page.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, "html.parser")
    else:
        print("Erreur de requête :", response.status_code, "Url:", url)
        return None


def get_category_links(soup):
    """
    Obtient les liens des catégories à partir de l'objet BeautifulSoup et de l'URL de base.

    Args:
        soup (BeautifulSoup): L'objet BeautifulSoup de la page.

    Returns:
        list: Une liste de liens de catégories.
    """
    category_links = [
        BASE_URL + link_element["href"]
        for link_element in soup.select('ul:not([class]) a')
    ]
    return category_links


def get_books_links(category_link):
    """
    Obtient les liens des livres d'une catégorie spécifique.

    Args:
        category_link (str): L'URL de la catégorie de livres.

    Returns:
        list: Une liste de liens de livres.
    """
    page_number = 1
    books_links = []
    while True:
        page_url = (
            category_link.replace("index.html", f"page-{page_number}.html")
            if page_number > 1
            else category_link
        )
        soup = get_soup(page_url)
        if soup:
            link_elements = soup.select("h3 > a")
            books_links.extend(
                [
                    urljoin(
                        page_url,
                        link_element["href"],
                    )
                    for link_element in link_elements
                ]
            )
            page_number += 1
        else:
            break

    return books_links


def download_image(image_url, dir_folder, book_title):
    """
    Télécharge une image à partir de son URL et l'enregistre dans le répertoire spécifié.

    Args:
        image_url (str): L'URL de l'image à télécharger.
        category_dir (str): Le répertoire de destination où l'image sera enregistrée.

    Returns:
        None
    """
    image_data = requests.get(image_url).content
    image_filename = f"{book_title}.jpg"
    with open(dir_folder + image_filename, "wb") as image_file:
        image_file.write(image_data)


def extract_product_data(product_page_url):
    """
    Extrait les données d'un livre à partir de son URL.

    Args:
        product_page_url (str): L'URL de la page du produit.

    Returns:
        list: Une liste contenant les données du produit.
    """
    soup = get_soup(product_page_url)

    upc = soup.find("th", string="UPC").find_next("td").text
    title = soup.find("h1").text.replace("/", "-")
    price_including_tax_element = (
        soup.find("th", string="Price (incl. tax)").find_next("td").text
    )
    price_including_tax = price_including_tax_element.replace("£", "").strip()
    price_excluding_tax_element = (
        soup.find("th", string="Price (excl. tax)").find_next("td").text
    )
    price_excluding_tax = price_excluding_tax_element.replace("£", "").strip()
    availability_element = (
        soup.find("th", string="Availability").find_next_sibling("td").text
    )
    availability = (
        availability_element.replace("In stock (", "")
        .replace(" available)", "")
        .strip()
    )
    product_description_element = soup.find("div", id="product_description")
    product_description = (
        product_description_element.find_next("p").get_text(strip=True)
        if product_description_element
        else ""
    )
    category = soup.find("ul", class_="breadcrumb").find_all("a")[-1].text
    review_rating = soup.find("p", class_="star-rating")["class"][1]
    image_url = urljoin(
        product_page_url, soup.find("div", id="product_gallery").find("img")["src"]
    )
    category_dir = "pictures/" + category.replace("/", "-") + "/"
    os.makedirs(category_dir, exist_ok=True)

    download_image(image_url, category_dir, title)

    return [
        product_page_url,
        upc,
        title,
        price_including_tax,
        price_excluding_tax,
        availability,
        product_description,
        category,
        review_rating,
        image_url,
    ]


def write_to_csv(data, filename):
    """
    Écrit les données dans un fichier CSV.

    Args:
        data (list): Les données à écrire dans le fichier CSV.
        filename (str): Le nom du fichier CSV de sortie.
    """
    data_dir = "data/"
    os.makedirs(data_dir, exist_ok=True)
    with open(data_dir + filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "product_page_url",
                "universal_product_code (upc)",
                "title",
                "price_including_tax",
                "price_excluding_tax",
                "number_available",
                "product_description",
                "category",
                "review_rating",
                "image_url",
            ]
        )
        writer.writerows(data)


def main():
    soup = get_soup(BASE_URL)
    if soup:
        category_links = get_category_links(soup)
        books_data = {}
        for category_link in category_links:
            books_links = get_books_links(category_link)
            books_data[category_link] = [
                extract_product_data(book_link) for book_link in books_links
            ]
            filename = f"{category_link.split('/')[-2]}.csv"
            write_to_csv(books_data[category_link], filename)


if __name__ == "__main__":
    main()
