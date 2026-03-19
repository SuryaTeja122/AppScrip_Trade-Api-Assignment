# Trade Opportunities API

## Overview

A FastAPI-based service that analyzes Indian market sectors and provides trade opportunity insights using AI.

## Features

* AI-powered analysis (Gemini API)
* Sector-based market insights
* Markdown report generation
* API key authentication
* Rate limiting

## Tech Stack

* FastAPI
* Python
* Gemini API
* Requests
* SlowAPI

## Setup

Install dependencies:
pip install fastapi uvicorn requests slowapi

Run server:
uvicorn main:app --reload

## API Endpoint

GET /analyze/{sector}

### Headers

x-api-key: 12345

### Example

/analyze/technology

## Output

Returns a structured markdown report including:

* Market Trends
* Opportunities
* Risks

## Author

B Surya Teja
