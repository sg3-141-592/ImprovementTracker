import connexion

import improvements

if __name__ == "__main__":
    app = connexion.App(__name__)
    app.add_api('apiSpec.yaml')
    app.run(port=8080, debug=True)