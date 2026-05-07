# Import FastAPI framework
from fastapi import FastAPI, Request, Form

# Used for returning HTML templates
from fastapi.templating import Jinja2Templates

# Used for serving static files like CSS, JS, images
from fastapi.staticfiles import StaticFiles

import numpy as np
from sklearn.preprocessing import StandardScaler


from src.pipeline.predict_pipeline import PredictPipeline, CustomData

# Create FastAPI app instance
app = FastAPI()

# Configure templates folder
# This folder will contain index.html and home.html
templates = Jinja2Templates(directory="templates")


# =========================================================
#  PAGE ROUTES
# =========================================================

# This route opens index.html
@app.get("/")
async def index(request: Request):
    # request object is required by Jinja templates
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
    



@app.post("/predict-data")
async def predict_data_post(
    request: Request,
    gender: str = Form(...),
    ethnicity: str = Form(...),
    parental_level_of_education: str = Form(...),
    lunch: str = Form(...),
    test_preparation_course: str = Form(...),
    reading_score: float = Form(...),
    writing_score: float = Form(...)
):
    # Create custom data object
    data = CustomData(
        gender=gender,
        race_ethnicity=ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )

    # Convert into dataframe
    pred_df = data.get_data_as_dataframe()
    print(pred_df)

    # Prediction pipeline
    predict_pipeline = PredictPipeline()

    # Predict result
    results = predict_pipeline.predict(pred_df)

    print(results)

    # Return prediction to frontend
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "results": results[0]
        }
    )

@app.get('/predict-data')
def predict_data_point(request: Request):
    return templates.TemplateResponse(
            "home.html",
            {"request": request})

        
        

    