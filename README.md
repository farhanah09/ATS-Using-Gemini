# ATS Resume Scanner

This repository contains the code for an ATS (Applicant Tracking System) Resume Scanner. This application allows users to upload a resume in PDF format and evaluate it against a job description using the Google Generative AI Gemini model.

## Features

- Upload a resume in PDF format.
- Scan the resume against a provided job description.
- Receive a professional evaluation or a percentage match for the resume's alignment with the job description.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/ats-resume-scanner.git
    cd ats-resume-scanner
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Get your API key for the Google Generative AI Gemini model. Follow the instructions [here](https://ai.google.dev/gemini-api/docs/api-key) to obtain your API key.

2. Create a `.env` file in the root directory of the project and add your API key:

    ```sh
    echo "GOOGLE_API_KEY=your_api_key_here" > .env
    ```

3. Run the Streamlit application:

    ```sh
    streamlit run app.py
    ```

### Credits - 

Made using guidance from youtube video of Krish Naik - [YouTube](https://www.youtube.com/watch?v=EECUXqFrwbc)

<a href="https://app.commanddash.io/agent?github=https://github.com/farhanah09/ATS-Using-Gemini"><img src="https://img.shields.io/badge/AI-Code%20Gen-EB9FDA"></a>
