import typing
import unittest
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from appCore.commands import AddDocumentCommand
from appCore.commands import AddDocumentCommand
from appCore.documentServices import DocumentServices
from appCore.documentServices import DocumentRepository
from appCore.commands import GetDocumentsQuery
from appCore.commands import GetDocumentQuery
from appCore.responses import GetRecordsResponse

import uuid

class DocumentServicesTests(unittest.TestCase):

    def test_DocumentServices__AddDocument__ReturnValidResponseWithGoodInput(self):
        # arrange
        id = '62ab14c7-9e57-4655-ac4d-777ba710c65f'

        data = {
            'title': "post title",
            'content': "content"
        }
        createdBy = 'test'
        command = AddDocumentCommand(data=data, userId=createdBy, id=id, collection="c1", name="name1")  

        repo = DocumentRepository()      
        service = DocumentServices(repo)
        
        # act
        response = service.addDocument(command)

        # assert
        self.assertTrue(response.status == 200)

    def test_DocumentServices__AddDocument__FailIdNotValid(self):
        # arrange
        data = {
            'title': "post title",
            'content': "content"
        }
        createdBy = 'test'
        command = AddDocumentCommand(data=data, userId=createdBy, id="foo", collection="c1", name="name1")  

        repo = DocumentRepository()      
        service = DocumentServices(repo)
        
        # act
        response = service.addDocument(command)

        # assert
        self.assertTrue(response.status == 400)


    def test_DocumentServices__DeleteDocument__ReturnValidResponseWithGoodInput(self):
        # arrange
        id = "93c93977-8ecd-4794-8a7a-71f93ae4b176"
        repo = DocumentRepository()      
        service = DocumentServices(repo)
        
        # act
        response = service.deleteDocument(GetDocumentQuery(id=id, userId='me'))

        # assert
        self.assertTrue(response.status == 200)

    def test_DocumentServices__GetDocuments__ReturnValidResponseWithGoodInput(self):
        # arrange
        query = GetDocumentsQuery(userId='system')

        repo = DocumentRepository()      
        service = DocumentServices(repo)
        
        # act
        response = service.getDocuments(query)

        # assert
        self.assertTrue(response.status == 200)

    # def test_AddValidator__ValidateAddDocumentCommand(self):
    #     # arrange
    #     id = '62ab14c7-9e57-4655-ac4d-777ba710c65f'
    #     userId = 'mrosario'
    #     data = { 'text': 'foo' }
    #     command = AddDocumentCommand(data, 'mrosario', id)

    #     # act
    #     response = AddDocumentCommandSchema().validate(command.__dict__)

    #     # assert
    #     self.assertTrue(response == {})

    # def test_AddValidator__ValidateAddDocumentCommand__HandleBadUserId(self):
    #     # arrange
    #     id = '62ab14c7-9e57-4655-ac4d-777ba710c65f'
    #     userId = ''
    #     data = { 'text': 'foo' }
    #     command = AddDocumentCommand(data, userId, id)

    #     # act
    #     response = AddDocumentCommandSchema().validate(command.__dict__)
  
    #     # assert
    #     self.assertTrue(response['createdBy'] != None)

    # def test_AddValidator__ValidateAddDocumentCommand__HandleBadId(self):
    #     # arrange
    #     id = ''
    #     userId = 'mrosario'
    #     data = { 'text': 'foo' }
    #     command = AddDocumentCommand(data, 'mrosario', id)

    #     # act
    #     response = AddDocumentCommandSchema().validate(command.__dict__)

    #     # assert
    #     self.assertTrue(response['id'] != None)


if __name__ == '__main__':
    unittest.main()