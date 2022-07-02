from distutils.version import LooseVersion
import ray
from ray import serve
from starlette.requests import Request
import logging

logger = logging.basicConfig(level=logging.INFO)

@serve.deployment
class Deployment2:
    async def __init__(self):
        logging.basicConfig(level=logging.INFO)
        pass
    async def __call__(self):
        logging.basicConfig(level=logging.DEBUG)
        return "test1"

@serve.deployment
class Deployment:
    async def __init__(self):
        pass
    async def __call__(self):
        logging.info("test-------------")
        # req  = request.json()
        return "test"
        

def deploy():
    ray.init(address="auto", namespace="serve")
    serve.start(derached=True,http_options={"location":"EveryNode","host": "0.0.0.0"})
    Deployment.options(route_prefix="/api").deploy()
    # Deployment2.options(route_prefix="/api1").deploy() 
    


if __name__ == "__main__":
    deploy()