from mangum import Mangum
from asgiref.wsgi import WsgiToAsgi
from app import app

handler = Mangum(WsgiToAsgi(app), lifespan="off")
