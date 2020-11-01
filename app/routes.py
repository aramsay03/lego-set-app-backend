from app import app

@app.route('/')
def index():
    return "Lego app back-end"