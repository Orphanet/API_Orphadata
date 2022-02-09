import os
import api


application = api.create_app(config_name=os.getenv('FLASK_ENV', 'production'))


if __name__ == '__main__':
    application.run(debug=True)
