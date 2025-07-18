from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware #Cross-Orgin Resource Sharing

app = FastAPI(
    title = "Choose your Own Adventure Game API",
    description = "api to generate stories",
    version = "0.1.0", 
    #path to API documentation (fastAPI automatically creates documentation page)
    docs_url = "/docs", #interactive documentation page (you can click on url paths)
    redoc_url = "/redoc", #read-only documentation page (better for reference)
)

#middleware controls which external orgins (websites) are allowed to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #allowing every website/domain to access this API (avoiding project complication)
    allow_credentials=True,
    allow_methods=["*"], #allow all HTTP methods to be used in requests to this API (GET, POST, PUT, etc.)
    allow_headers=["*"] #allows requests to include any headers (headers carry metadata; ex: Content-Type)
)

if __name__ == "__main__": 
    import uvicorn #web server
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)