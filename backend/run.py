from app import create_app
from waitress import serve # waitress as WSGI

app = create_app()

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5001) # Waitress's serve function instead of Flask's built-in development server
