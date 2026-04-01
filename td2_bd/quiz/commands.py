from .app import app, db
from .models import create_questionnaire, add_question

@app.cli.command()
def syncdb():
    db.create_all()
    create_questionnaire("Culture Générale")
    create_questionnaire("Informatique")
    create_questionnaire("Géographie")

    # Questionnaire 1: Culture Générale
    add_question(1, "Quelle est la capitale du Japon ?", type='question_ouverte', bonne_reponse="Tokyo")
    add_question(1, "Quel est le plus grand océan du monde ?", type='question_fermee', proposition1="Océan Atlantique", proposition2="Océan Pacifique", bonne_reponse="Océan Pacifique")

    # Questionnaire 2: Informatique
    add_question(2, "Que signifie l'acronyme HTML ?", type='question_ouverte', bonne_reponse="HyperText Markup Language")
    add_question(2, "Python est un langage compilé.", type='question_fermee', proposition1="Vrai", proposition2="Faux", bonne_reponse="Faux")
    add_question(2, "Combien de bits y a-t-il dans un octet ?", type='question_ouverte', bonne_reponse="8")

    # Questionnaire 3: Géographie
    add_question(3, "Quel est le plus grand pays du monde en superficie ?", type='question_ouverte', bonne_reponse="Russie")
    add_question(3, "Sur quel continent se trouve l'Égypte ?", type='question_fermee', proposition1="Afrique", proposition2="Asie", bonne_reponse="Afrique")

    print("Database synchronized and sample data added.")

@app.cli.command()
def cleardb():
    db.drop_all()
    print("Database cleared.")