# OCR REST API

This repository contains a FastAPI-based OCR REST API that leverages the [GOT-OCR 2.0](https://huggingface.co/stepfun-ai/GOT-OCR-2.0-hf) model to extract text from images. The API exposes a single endpoint (`/ocr`) that accepts an image file and returns the extracted text.


## Installation & Running Locally

1. **Clone the repository:**

   ```bash
   git clone https://github.com/stathoubas/OCR-REST-API.git
   cd your-repo

2. **Set up a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   
3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt

4. **Run the API server with Uvicorn:**

   ```bash
   uvicorn app:app --reload
   The API will be available at http://127.0.0.1:8000

## Using the /ocr Endpoint

1. **Via Swagger UI:**

   ```bash
   Visit http://127.0.0.1:8000/docs and use the interactive interface to upload an image and get the extracted text.

2. **Via cURL:**

   ```bash
   curl -X POST "http://127.0.0.1:8000/ocr" -F "file=@/path/to/your/image.jpg"
   Replace /path/to/your/image.jpg with the actual path to your image file.


## Containerizing the API with Docker

1. **Build the Docker image:**

   ```bash
   In the repository root (where your Dockerfile is located), build the image:
   docker build -t ocr-api .
   This command uses the provided Dockerfile to build an image tagged as ocr-api.

2. **Run the Docker Container:**

   ```bash
   docker run -p 8000:8000 ocr-api
   The API will be accessible at http://localhost:8000.

3. **Verify the API:**
   Open your web browser and navigate to:
   ```bash
   http://localhost:8000/docs
   Test the /ocr endpoint using the Swagger UI.
   The API will be accessible at http://localhost:8000.



   
