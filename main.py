
from fastapi import FastAPI
from pydantic import BaseModel , Field


class CampaignCreate(BaseModel):
    client_name: str = Field(..., description="Name of the client")
    name: str = Field(..., description="Name of the campaign")
    platform: str = Field(..., description="Platform for the campaign (e.g., Facebook, Google Ads)")
    budget: float = Field(..., description="Budget allocated for the campaign")

class websiteanalysis(BaseModel):
    url: str = Field(..., description="URL of the website to analyze")
    business_type: str = Field(..., description="Type of business for the website")
    industry: str = Field(..., description="Industry of the business")


app = FastAPI(
    title="Digital Marketing Automation API",
    description="Backend for AI-powered digital marketing automation",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Digital Marketing Automation Backend is Running",
        "status": "Success"
    }

@app.get("/health")
def health_check():
    return {
        "application": "Digital Marketing AI",
        "status": "Healthy"
    }

@app.get("/campaigns")
def get_campaigns():
    return {
        "message": "Campaign API is working",
        "campaigns": []
    }

@app.get("/about")
def about():
    return {
        "project": "Digital Marketing AI",
        "purpose": "Automating marketing workflows Like Seo, Content Creation, Social Media Management, and Email Marketing using AI",
        "backend": "FastAPI"
    }

@app.post("/campaigns")
def create_campaign(campaign: CampaignCreate):
    return {
        "message": "Campaign created successfully",
        "client_name": campaign.client_name,
        "campaign_name": campaign.name,
        "platform": campaign.platform,
        "budget": campaign.budget,
        "status": "Success"
    }

@app.post("/website-analysis")
def analyze_website(analysis: websiteanalysis):
    return {
        "message": "Website analysis initiated",
        "url": analysis.url,
        "business_type": analysis.business_type,
        "industry": analysis.industry,
        "status": "Success"
    }