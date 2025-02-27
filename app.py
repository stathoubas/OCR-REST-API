from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from transformers import AutoModelForImageTextToText, AutoProcessor
from PIL import Image
import torch
import io

app = FastAPI()

# Set device to CPU (or change to "cuda" if you have GPU support)
device = "cpu"

# Load the OCR model and processor globally at startup
model_name = "stepfun-ai/GOT-OCR-2.0-hf"
try:
    model = AutoModelForImageTextToText.from_pretrained(model_name)
    processor = AutoProcessor.from_pretrained(model_name)
    model.to(device)
except Exception as e:
    raise RuntimeError(f"Failed to load model or processor: {e}")

##############################################################################
# /ocr Endpoint:
#     The endpoint accepts an image file via a POST request.
#     It checks that the uploaded file is indeed an image.
#     The image is read into a PIL object.
#     The processor converts the image into the required tensor format.
#     The model generates text tokens, which are decoded into a human-readable string.
#     The result is returned in a JSON response.
##############################################################################

@app.post("/ocr")
async def ocr_endpoint(file: UploadFile = File(...)):
    # Ensure the uploaded file is an image
    if file.content_type.split('/')[0] != 'image':
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image.")

    # Read and load image data
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not process image file: {e}")

    # Process the image for the OCR model
    try:
        inputs = processor(image, return_tensors="pt").to(device)
        generate_ids = model.generate(
            **inputs,
            do_sample=False,
            tokenizer=processor.tokenizer,
            stop_strings="<|im_end|>",
            max_new_tokens=4096,
        )
        # Decode the output text
        # Exclude the tokens corresponding to the input prompt if any
        text = processor.decode(generate_ids[0, inputs["input_ids"].shape[1]:], skip_special_tokens=True)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OCR processing error: {e}")

    return JSONResponse(content={"extracted_text": text})
