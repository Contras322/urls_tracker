from fastapi import status

from app.presentation.api.schemas import ResponseErrorSchema

NOT_FOUND: dict = {
    status.HTTP_404_NOT_FOUND: {"description": "Not Found", "model": ResponseErrorSchema}
}
FORBIDDEN: dict = {
    status.HTTP_403_FORBIDDEN: {"description": "Forbidden", "model": ResponseErrorSchema}
}


SERVICE_UNAVAILABLE: dict = {
    status.HTTP_503_SERVICE_UNAVAILABLE: {
        "description": "Service Unavailable",
        "model": ResponseErrorSchema,
    }
}
INTERNAL_SERVER_ERROR: dict = {
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "description": "Internal Server Error",
        "model": ResponseErrorSchema,
    }
}
