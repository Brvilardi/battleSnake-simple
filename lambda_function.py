import src.main as main
from mangum import Mangum

app = main.app

handler = Mangum(app=app)

