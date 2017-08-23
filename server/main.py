from flask import Flask
import yaml

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    # read and return a yaml file (called 'config.yaml' by default) and give it
    # back as a dictionary
    with open( 'config.yaml' ) as f:
        config = yaml.load( f )

    app.run( host='0.0.0.0', port=config['port'] )
    app.debug = True
