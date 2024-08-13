import requests

# URL of the webpage
url = "https://2024.ieee-biocas.org/Conference-History"

# Send a GET request to the URL
response = requests.get(url)

# Get the HTML content
html_content = response.text

# Save the HTML content to a file (optional)
with open('conference_history.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print("HTML content fetched successfully.")
