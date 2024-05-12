from flask import Blueprint, render_template
from app import create_app

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('Présentation.html')

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
