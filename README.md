**ECLI Search and Highlight Tool**

This project is a Flask web application designed to search and highlight specific terms within XML documents identified by ECLI (European Case Law Identifier). The application fetches case law data from rechtspraak.nl based on ECLI-numbers, highlights search terms, and allows users to navigate through the search results. Additionally, it provides the ability to download search results in an Excel file.

**Features**

Search and Highlight: Users can input search terms to find and highlight within the text of case law documents.
Navigation: Navigate through previous and next search results for each ECLI.
Download: Download the search results as an Excel file.
Caching: Caches the XML data to improve performance and reduce redundant API calls.

**Installation**
Clone the repository:

sh
Copy code
git clone https://github.com/yourusername/ecli-search-tool.git
cd ecli-search-tool
Create a virtual environment:

sh
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required dependencies:

sh
Copy code
pip install -r requirements.txt
Run the application:

sh
Copy code
python app.py
Access the application:
Open your web browser and navigate to http://127.0.0.1:5000.

**Usage**

Main Page
Search Terms: Enter search terms separated by commas. Use | to separate synonyms for a term.
Submit: Click the search button to perform the search.

Navigation
Previous/Next: Navigate through the highlighted search results for each ECLI using the previous and next buttons.

Download Results
Download Excel: Click the download button to download the search results as an Excel file.

**Code Overview**
app.py: The main Flask application file containing routes and logic.

Routes:
/: Main page for inputting search terms and viewing results.
/previous/<ecli>: Route to view the previous search result for an ECLI.
/next/<ecli>: Route to view the next search result for an ECLI.
/delete/<ecli>: Route to delete the current search result for an ECLI.
/download/excel: Route to download the search results as an Excel file.

Functions:
highlight_term(text, term): Highlights search terms in the text.
api_request(ecli): Makes an API request to fetch the XML data for an ECLI.
update_excel_file(): Updates the Excel file with current search results.
remove_html_tags(text): Removes HTML tags from the text.
get_sibling_elements(ecli, index): Retrieves previous and next elements for a specific ECLI.

**Dependencies**
Flask
Requests
Pandas
lxml
openpyxl

**Contributing**
Fork the repository.
Create a new branch: git checkout -b my-feature-branch.
Make your changes.
Commit your changes: git commit -m 'Add new feature'.
Push to the branch: git push origin my-feature-branch.
Submit a pull request.

**License**
This project is licensed under the MIT License.
