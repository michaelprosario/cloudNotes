
from appCore.commands import StoreDocumentCommand
from appCore.documentServices import DocumentServices
from appCore.commands import GetDocumentQuery
from appCore.commands import GetDocumentsQuery
from appCore.environmentHelper import checkForRequiredEnvironmentVariables
#from appInfra.documentPgRepository import DocPgRepository
from appInfra.documentSqlLiteRepository import DocSqlLiteRepository
import uuid

from fastapi import FastAPI

def getService():
    repo = DocSqlLiteRepository()
    repo.setupAppDatabase()
    service = DocumentServices(repo)
    return service

#checkForRequiredEnvironmentVariables()
service = getService()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server ok"}

@app.post("/api/store-document")
async def storeDocument(command: StoreDocumentCommand):      
    return service.storeDocument(command)

@app.post("/api/get-documents")
async def getDocuments(query: GetDocumentsQuery):
    return service.getDocuments(query)

@app.post("/api/get-document")
async def getDocument(query: GetDocumentQuery):
    return service.getDocument(query)

@app.post("/api/delete-document")
async def deleteDocument(query: GetDocumentQuery):
    return service.deleteDocument(query)
