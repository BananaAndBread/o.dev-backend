swagger = {
    "openapi":"3.0.0",
    "info": {
        "title": "Currencies"
    },
    "paths": {
        "/api/currencies/all_statistics":{
            "get": {
                "summary": "Get all statistics",
                'parameters': [
                    {
                        "name": "date_start",
                        "in": "query",
                        "schema" : {
                            "type": "string",
                            "format": "date"
                        }

                    },
                    {
                        "name": "date_end",
                        "in": "query",
                        "schema": {
                            "type": "string",
                            "format": "date"
                        }
                    },
                    {
                        "name": "currency",
                        "in": "query",
                        "schema": {
                            "type": "string",
                        }
                    }
                ],
                "responses": {
                    200:{
                        "description": "Currency statistics",
                        "content": {
                            "application/json" : {
                                "schema": {
                                    "type":"object",
                                    "properties": {
                                        "RUB": {
                                            "type": "object",
                                            "properties": {
                                                "std_dev": {
                                                    "type": "number"

                                                },
                                                "avg": {
                                                    "type": "number"
                                                },
                                                "cor": {
                                                    "type": "object",
                                                    "properties":{
                                                        "USD": {
                                                            "type" : "number"
                                                        }

                                                    },
                                                    "additionalProperties": True
                                                }

                                            }
                                        }
                                    },
                                    'additionalProperties': True
                                }
                            }
                        }
                    }
                }
            }
        }
    }

}