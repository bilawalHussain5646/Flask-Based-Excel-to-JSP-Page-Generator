# Flask Excel to JSP Page Generator

## Overview

This project is a Flask-based web application that processes Excel files to generate structured JSP Page content, primarily for Adobe Experience Manager (LG CMS) integration. The application supports English and Arabic content and dynamically structures JSP Page based on predefined Excel templates.

## Features

- Upload Excel files via a web interface.
- Extract metadata from the "Main Data" sheet.
- Parse structured content from the "Content" sheet.
- Dynamically generate JSP Page components including text, images, and review sections.
- Support English and Arabic content.
- Provide the generated JSP Page file for download.

## System Architecture

```
+-------------------+
|  User Uploads    |
|  Excel File      |
+-------------------+
        |
        v
+-------------------+
|  Flask App       |
|  Parses Data     |
+-------------------+
        |
        v
+-------------------+
|  JSP Page Generator  |
|  Builds Template |
+-------------------+
        |
        v
+-------------------+
|  LG CMS Integration |
|  Deploy Content  |
+-------------------+
```

## Installation

### Prerequisites

- Python 3.8+
- Flask
- Pandas
- openpyxl

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/repository-name.git
   cd repository-name
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Access the application at `http://localhost:5000`

## Usage

1. Open the web application.
2. Upload an Excel file with the predefined structure.
3. The system processes the data and generates an JSP Page file.
4. Download the generated JSP Page file for LG CMS integration.

## File Structure

```
project-root/
│── app.py  # Main Flask application
│── templates/
│   ├── index.html  # Upload page
│── static/
│── uploads/  # Temporary storage for uploaded files
│── output/   # Generated JSP Page files
│── requirements.txt  # Dependencies
│── README.md
```

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

## License

This project is licensed under the MIT License.

## Contact

For any issues, please open an issue on GitHub or reach out to the maintainer.
