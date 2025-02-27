# OCR-REST-API
This repository contains a simple OCR REST API built with FastAPI, Hugging Face Transformers, and PyTorch. The API exposes a single endpoint /ocr that accepts an image file and returns the extracted text.

## Installation & Running Locally

   ### Clone the Repository:

git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

### Set Up a Virtual Environment (Optional but Recommended):

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

## Install Dependencies:

pip install -r requirements.txt

### Run the API:

    uvicorn app:app --reload

    The API will be accessible at http://127.0.0.1:8000 with interactive documentation available at http://127.0.0.1:8000/docs.

## Using the /ocr Endpoint

  ###  Via Swagger UI:
    Visit http://127.0.0.1:8000/docs and use the interactive interface to upload an image and get the extracted text.

   ### Via cURL:

    curl -X POST "http://127.0.0.1:8000/ocr" -F "file=@/path/to/your/image.jpg"

    Replace /path/to/your/image.jpg with the actual path to your image file.

## Containerizing the API with Docker

This repository includes a sample Dockerfile to containerize the OCR API.
Building the Docker Image

   ### Open a terminal and navigate to the project directory:

cd <your-repo-name>

### Build the Docker image:

    docker build -t ocr-api .

    This command uses the provided Dockerfile to build an image tagged as ocr-api.

## Running the Docker Container

Run the container with:

docker run -p 8000:8000 ocr-api

The API will now be accessible at http://localhost:8000.

## Testing the Containerized API

    Swagger UI:
    Open http://localhost:8000/docs in your web browser.

    cURL:

curl -X POST "http://localhost:8000/ocr" -F "file=@/path/to/your/image.jpg"
