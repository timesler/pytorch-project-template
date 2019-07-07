from fastapi import FastAPI, File, UploadFile
import torch

## Load model, for example:
# from models.model import Model
# device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
# model = Model(pretrained=True).eval().to(device)

app = FastAPI()

@app.post('/predict')
async def predict(input_file: UploadFile = File(...)):
    ## E.g., for an image input, we can use PIL.Image directly
    # img = Image.open(input_file)

    return {
        'filename': input_file.filename,
        'content_type': input_file.content_type
    }
