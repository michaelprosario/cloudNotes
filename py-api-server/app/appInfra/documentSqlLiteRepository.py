from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import select
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from typing import List
from typing import Optional
import time
import json
import sys
import os

sys.path.append('../appCore')
from appCore.responses import AppResponse
from appCore.responses import GetRecordResponse
from appCore.responses import GetRecordsResponse
from appCore.documentServices import GetDocumentQuery
sys.path.append('../appInfra')
from appInfra.doc import Doc
from appInfra.doc import Base

class DocSqlLiteRepository():
    def setupMemoryDatabase(self):
        self.engine = create_engine("sqlite://", echo=True)
        Base.metadata.create_all(self.engine)

    def setupAppDatabase(self):
        self.engine = create_engine("sqlite:///app.db", echo=True)
        Base.metadata.create_all(self.engine)        
    
    def addDocument(self,command):

        timeStamp = int(time.time()) 
        command.data['createdAt'] = timeStamp

        strData = json.dumps(command.data)

        with Session(self.engine) as session:
            record = Doc(
                id=command.id, 
                name=command.name, 
                collection=command.collection,
                content=strData,
                tags = command.tags,
                created_by='system',
                updated_by='system', 
                created_at=timeStamp, 
                updated_at=0
                )
            session.add_all([record])
            session.commit()

        response = AppResponse()
        return response

    def updateDocument(self,command):
        timeStamp = int(time.time()) 
        command.data['updatedAt'] = timeStamp

        strData = json.dumps(command.data)

        with Session(self.engine) as session:
            record = session.get(Doc, command.id)
            record.content = strData
            record.name = command.name
            record.tags = command.tags
            record.updated_at = timeStamp
            session.commit()

        response = AppResponse()
        return response

    def deleteDocument(self,query):
        if self.recordExists(query):
            with Session(self.engine) as session:
                record = session.get(Doc, query.id)
                session.delete(record)
                session.commit()
        
        response = AppResponse()
        return response

    def getDocuments(self,query):
        records = []
        print(query)

        with Session(self.engine) as session:
            if len(query.keyword) > 0:
                search = "%{}%".format(query.keyword)
                recordSet = session.query(Doc).filter(Doc.content.like(search))            
            elif len(query.collection) > 0:
                recordSet = session.query(Doc).filter(Doc.collection == query.collection)            
            else:
                recordSet = session.query(Doc).all()

            for record in recordSet:
                query = GetDocumentQuery(userId="system", id=record.id)
                getResponse = self.getDocument(query)
                if getResponse.status == 200:
                    records.append(getResponse.record)

        response = GetRecordsResponse(data=records, userId=query.userId)
        return response

    def getDocument(self,query):
        with Session(self.engine) as session:
            record = session.get(Doc, query.id)
            if( record == None):
                return AppResponse(status=404, message="Record not found")
            
            dictionary = json.loads(record.content)
            dictionary['createdAt'] = record.created_at
            dictionary['updatedAt'] = record.updated_at

            response = GetRecordResponse(record=dictionary, userId="system")
        return response

    def recordExists(self,query):
        if query == None:
            raise Exception("Query is not defined")

        with Session(self.engine) as session:
            record = session.get(Doc, query.id)

        return record != None

