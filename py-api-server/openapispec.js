{
    "openapi": "3.1.0",
        "info": {
        "title": "FastAPI",
            "version": "0.1.0"
    },
    "paths": {
        "/": {
            "get": {
                "summary": "Root",
                    "operationId": "root__get",
                        "responses": {
                    "200": {
                        "description": "Successful Response",
                            "content": {
                            "application/json": {
                                "schema": { }
                            }
                        }
                    }
                }
            }
        },
        "/store-document": {
            "post": {
                "summary": "Storedocument",
                    "operationId": "storeDocument_store_document_post",
                        "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/StoreDocumentCommand"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                            "content": {
                            "application/json": {
                                "schema": { }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                            "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/get-documents": {
            "post": {
                "summary": "Getdocuments",
                    "operationId": "getDocuments_get_documents_post",
                        "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/GetDocumentsQuery"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                            "content": {
                            "application/json": {
                                "schema": { }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                            "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/get-document": {
            "post": {
                "summary": "Getdocument",
                    "operationId": "getDocument_get_document_post",
                        "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/GetDocumentQuery"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                            "content": {
                            "application/json": {
                                "schema": { }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                            "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/delete-document": {
            "post": {
                "summary": "Deletedocument",
                    "operationId": "deleteDocument_delete_document_post",
                        "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/GetDocumentQuery"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                            "content": {
                            "application/json": {
                                "schema": { }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                            "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "components": {
        "schemas": {
            "GetDocumentQuery": {
                "properties": {
                    "id": {
                        "type": "string",
                            "title": "Id"
                    },
                    "userId": {
                        "type": "string",
                            "title": "Userid"
                    }
                },
                "type": "object",
                    "required": [
                        "id",
                        "userId"
                    ],
                        "title": "GetDocumentQuery"
            },
            "GetDocumentsQuery": {
                "properties": {
                    "keyword": {
                        "type": "string",
                            "title": "Keyword",
                                "default": ""
                    },
                    "collection": {
                        "type": "string",
                            "title": "Collection",
                                "default": ""
                    },
                    "userId": {
                        "type": "string",
                            "title": "Userid"
                    }
                },
                "type": "object",
                    "required": [
                        "userId"
                    ],
                        "title": "GetDocumentsQuery"
            },
            "HTTPValidationError": {
                "properties": {
                    "detail": {
                        "items": {
                            "$ref": "#/components/schemas/ValidationError"
                        },
                        "type": "array",
                            "title": "Detail"
                    }
                },
                "type": "object",
                    "title": "HTTPValidationError"
            },
            "StoreDocumentCommand": {
                "properties": {
                    "collection": {
                        "type": "string",
                            "title": "Collection"
                    },
                    "userId": {
                        "type": "string",
                            "title": "Userid"
                    },
                    "name": {
                        "type": "string",
                            "title": "Name"
                    },
                    "tags": {
                        "type": "string",
                            "title": "Tags",
                                "default": ""
                    },
                    "data": {
                        "type": "object",
                            "title": "Data"
                    },
                    "id": {
                        "type": "string",
                            "title": "Id"
                    }
                },
                "type": "object",
                    "required": [
                        "collection",
                        "userId",
                        "name",
                        "data",
                        "id"
                    ],
                        "title": "StoreDocumentCommand"
            },
            "ValidationError": {
                "properties": {
                    "loc": {
                        "items": {
                            "anyOf": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "integer"
                                }
                            ]
                        },
                        "type": "array",
                            "title": "Location"
                    },
                    "msg": {
                        "type": "string",
                            "title": "Message"
                    },
                    "type": {
                        "type": "string",
                            "title": "Error Type"
                    }
                },
                "type": "object",
                    "required": [
                        "loc",
                        "msg",
                        "type"
                    ],
                        "title": "ValidationError"
            }
        }
    }
}