from .app import app, db
from .models import create_questionnaire, add_question

@app.cli.command()
def syncdb():
    db.create_all()
    qs1 = create_questionnaire("Math Quiz")
    qs2 = create_questionnaire("test")
    question1 = add_question(1, "What is 2 + 2?")
    question2 = add_question(1, "What is the square root of 16?")
    question3 = add_question(2, "Sample question?")
    print("Database synchronized and sample data added.")

@app.cli.command()
def cleardb():
    db.drop_all()
    print("Database cleared.")