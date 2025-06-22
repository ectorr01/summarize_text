from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from transformers import pipeline
import torch 

app = FastAPI()

templates = Jinja2Templates(directory="templates")

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

MAX_INPUT_LENGTH = 1024  

@app.post("/summarize", response_class=HTMLResponse)
def summarize(request: Request, text: str = Form(...)):
    text = text.strip()

    if not text:
        return templates.TemplateResponse("result.html", {"request": request, "summary": "Error: the text is empty."})

    if len(text.strip().split()) < 20:
        return templates.TemplateResponse("result.html", {"request": request, "summary": "Error: The text is too short to generate an effective summary."})

    if len(text) > MAX_INPUT_LENGTH:
        return templates.TemplateResponse("result.html", {"request": request, "summary": f"Error: Text is too long (max {MAX_INPUT_LENGTH} characters)."})

    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]["summary_text"]
    return templates.TemplateResponse("result.html", {"request": request, "summary": summary})
