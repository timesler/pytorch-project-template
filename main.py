from fastapi import FastAPI, File, UploadFile
import torch
import io

import config

# Load model
model = config.model['cls'](**config.model['params']).eval().to(config.device)

app = FastAPI()

@app.post('/predict')
async def predict(input_file: UploadFile = File(...)):
    input_file = io.BytesIO(input_file)

    ## E.g., for an image input, we can use PIL.Image directly
    # img = Image.open(input_file)

    return {
        'filename': input_file.filename,
        'content_type': input_file.content_type
    }
