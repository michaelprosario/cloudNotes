from appCore.commands import AddDocumentCommand
from appCore.commands import GetDocumentQuery
from appCore.commands import GetDocumentsQuery
from appCore.commands import StoreDocumentCommand
from appCore.responses import AppResponse
from appCore.responses import GetRecordResponse
from appCore.responses import GetRecordsResponse

from appCore.validators import StoreDocumentCommandValidator, GetDocumentQueryValidator, GetDocumentsQueryValidator
from pydantic import BaseModel,ValidationError
from typing import Optional, List
from appCore.documentRepository import DocumentRepository 

import datetime
import time
import re


class DocumentServices:
  def __init__(self, documentRepository : DocumentRepository ):
    self.documentRepository = documentRepository

  def isUUID(self,input):
    if input == None:
      return False

    guid_pattern = "^(?:\\{{0,1}(?:[0-9a-fA-F]){8}-(?:[0-9a-fA-F]){4}-(?:[0-9a-fA-F]){4}-(?:[0-9a-fA-F]){4}-(?:[0-9a-fA-F]){12}\\}{0,1})$"
    return re.match(guid_pattern, input) != None

  def makeAppResponse(self,message,statusCode, errors):
      appResponse = AppResponse()
      appResponse.message = message
      appResponse.status = statusCode
      appResponse.errors = errors

      return appResponse

  def addDocument(self,command):
    errors = StoreDocumentCommandValidator().validate(command)
    if(len(errors) > 0):
      return self.makeAppResponse('validation errors', 400, errors)

    if command == None:
      return self.makeAppResponse('command is none', 400, None)

    try:
      if not self.isUUID(command.id):
        return self.makeAppResponse('uuid not valid', 400, None)

      command.data['id'] = command.id
      command.data['name'] = command.name
      command.data['tags'] = command.tags
      response = self.documentRepository.addDocument(command)
      return response
    except ValidationError as e:
      errorResponse = self.makeAppResponse('validation error', 400, e)
      return errorResponse

  def storeDocument(self,command):
    if command == None:
      return self.makeAppResponse('command is none', 400, None)

    errors = StoreDocumentCommandValidator().validate(command)
    if(len(errors) > 0):
      return self.makeAppResponse('validation errors', 400, errors)

    try:
      if not self.isUUID(command.id):
        return self.makeAppResponse('uuid not valid', 400, None)

      command.data['id'] = command.id
      command.data['name'] = command.name
      command.data['tags'] = command.tags

      # check if record exists
      recordExistsQuery = GetDocumentQuery(userId = command.userId, id=command.id)
      recordExists = self.documentRepository.recordExists(recordExistsQuery)

      if recordExists:
        # update doc as needed
        response = self.documentRepository.updateDocument(command)
      else:
        # change doc as needed
        response = self.documentRepository.addDocument(command)

      return response
    except ValidationError as e:
      errorResponse = self.makeAppResponse('validation error', 400, e)
      return errorResponse

  def deleteDocument(self,query):
    if query == None:
      return self.makeAppResponse('query is none', 400, None)

    errors = GetDocumentQueryValidator().validate(query)
    if(len(errors) > 0):
      return self.makeAppResponse('validation errors', 400, errors)

    try:
      response = self.documentRepository.deleteDocument(query)
      return response
    except ValidationError as e:
      errorResponse = self.makeAppResponse('validation error', 400, e)
      return errorResponse

  def getDocuments(self,query):
    errors = GetDocumentsQueryValidator().validate(query)
    if(len(errors) > 0):
      return self.makeAppResponse('validation errors', 400, errors)


    if query == None:
      return self.makeAppResponse('query is none', 400, None)

    if query.userId == None:
      return self.makeAppResponse('query.userId should be defined', 400, None)

    response = self.documentRepository.getDocuments(query)
    return response

  def getDocument(self,query):
    errors = GetDocumentQueryValidator().validate(query)
    if(len(errors) > 0):
      return self.makeAppResponse('validation errors', 400, errors)

    if query == None:
      return self.makeAppResponse('query is none', 400, None)

    if(query.id == ''):
      return self.makeAppResponse('validation error: id required', 400, None)

    try:
      response = self.documentRepository.getDocument(query)
      return response
    except ValidationError as e:
      errorResponse = self.makeAppResponse('validation error', 400, e)
      return errorResponse

  def recordExists(self,query):
    if query == None:
      return self.makeAppResponse('query is none', 400, None)
    try:
      return self.documentRepository.recordExists(query)
    except ValidationError as e:
      errorResponse = self.makeAppResponse('validation error', 400, e)
      return errorResponse