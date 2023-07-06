import os
import requests


def download_pdf(url, folder):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to download: {url} - {e}")
        return

    filename = os.path.join(folder, url.split("/")[-1])
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded: {filename}")


def main():
    prefix = "https://www.chandamama.in/resources/teluguNew/{}/Chandamama-{}-{}.pdf"

    folder = "pdf_files"
    if not os.path.exists(folder):
        os.makedirs(folder)

    failed_urls = []
    url = ""
    for year in range(1991, 2013):
        for month in range(1, 13):
            try:
                url = prefix.format(year, year, month)
                download_pdf(url, folder)
            except Exception:
                failed_urls.append(url)

    if failed_urls:
        print("The following URLs failed to download:")
        for url in failed_urls:
            print(url)


if __name__ == "__main__":
    main()
