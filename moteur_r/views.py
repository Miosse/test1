from flask import Flask

#from .models import MA_BASE
from .utils import get_df_value
import pprint

app = Flask(__name__)


# On ajoute les configurations du serveur 
app.config.from_object('config')

@app.route('/contents/')
@app.route('/')
def index():
	return "Hello World !"





@app.route('/recommend/<int:content_id>/')
def content(content_id):
     #return '%s' % content_id
     #pp = pprint.PrettyPrinter(indent=4)
     #pp.pprint(get_df_value(content_id))
     
     return (get_df_value(content_id))
     
     #return get_df_value(content_id)


if __name__ == "__main__":
	app.run()

