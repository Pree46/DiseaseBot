# MediCheck: AI-powered Symptom Checker and Diagnosis Tool

MediCheck is a web-based application designed to assist users in identifying potential health conditions based on their reported symptoms. Leveraging machine learning techniques, MediCheck provides users with quick and accurate diagnostic insights.

## Features

- **Symptom Selection**: Users can select their symptoms from a comprehensive list provided by the application.
- **Search Functionality**: A search bar allows users to easily find and select their symptoms.
- **AI Diagnosis**: The selected symptoms are processed by an AI-powered decision tree classifier to predict potential health conditions.
- **Confidence Level**: MediCheck provides users with a confidence level indicating the accuracy of the diagnosis based on the matched symptoms.
- **User-friendly Interface**: The application offers a clean and intuitive user interface for ease of use.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/medicheck.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python app.py
    ```

4. Access the application in your web browser at `http://localhost:5000`.

## Usage

1. Open the application in your web browser.
2. Select your symptoms from the provided list or use the search bar to find specific symptoms.
3. Submit your selected symptoms to receive a diagnosis.
4. Review the predicted health condition and confidence level provided by the application.

## Dataset

The dataset used for training the AI model can be found in the `Training.csv` file. This file contains a list of symptoms and corresponding health conditions used to train the machine learning model.

## Contributors

- R Preethi
- T Pranav
- Fazlur Rehman
