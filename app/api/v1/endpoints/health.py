from fastapi import APIRouter
from pydantic import BaseModel

from common.api.base import BaseAPI

class HealthDTO(BaseModel):
    message : str = "Health Checked"



class HealthAPI(BaseAPI):

    def __init__(self):
        self.router = APIRouter()
        self._register_routes()


    def _register_routes(self):
        self.router.add_api_route(
            "/health-check",
            self.health_check,
            methods = ["GET"],
            description= "endpoint to check health of backend service",
            summary = "List all routes",
            response_model = HealthDTO
        )
    
    def health_check(self):
        try:
            return HealthDTO(message = "Health check successfull")
        except Exception as exc:
            return HealthDTO(message = "Health check failed")
        

health_api = HealthAPI()
health_router = health_api.router