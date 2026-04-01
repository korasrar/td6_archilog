from flask import url_for
from .app import db

questionnaire_id = 0
questionnaires = []

question_id = 0


class Question(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Numero = db.Column(db.Integer)
    Enonce = db.Column(db.String(200))
    Type = db.Column(db.String(200))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.Id'))

    __mapper_args__ = {
        "polymorphic_identity": "question",
        "polymorphic_on": Type,
    }

    def __init__(self, enonce, numero=None, questionnaire=None):
        self.Enonce = enonce
        self.Numero = numero
        if questionnaire:
            self.questionnaire_id = questionnaire

    def get_id(self):
        return self.Id


class QuestionOuverte(Question):
    Reponse = db.Column(db.String(200))

    __mapper_args__ = {
        "polymorphic_identity": "question_ouverte",
        "polymorphic_load": "inline"
    }

    def __init__(self, enonce, numero=None, questionnaire=None, reponse=None):
        super().__init__(enonce, numero, questionnaire)
        self.Reponse = reponse


class QuestionFermee(Question):
    Proposition1 = db.Column(db.String(200))
    Proposition2 = db.Column(db.String(200))
    BonneReponse = db.Column(db.String(200))

    __mapper_args__ = {
        "polymorphic_identity": "question_fermee",
        "polymorphic_load": "inline"
    }

    def __init__(self,
                 enonce,
                 numero=None,
                 questionnaire=None,
                 proposition1=None,
                 proposition2=None,
                 bonne_reponse=None):
        super().__init__(enonce, numero, questionnaire)
        self.Proposition1 = proposition1
        self.Proposition2 = proposition2
        self.BonneReponse = bonne_reponse


class Questionnaire(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100))
    questions = db.relationship('Question',
                                backref='questionnaire',
                                lazy='dynamic')

    def to_json(self):
        return {
            'id':
            self.Id,
            'title':
            self.Title,
            'uri':
            url_for('get_questionnaire',
                    questionnaire_id=self.Id,
                    _external=True)
        }

    def get_questions(self):
        questions = db.session.query(Question).filter_by(
            questionnaire_id=self.Id).all()
        return questions

    def delete_question(self, question_id):
        question = Question.query.get(question_id)
        db.session.delete(question)
        db.session.commit()

    def get_id(self):
        return self.Id

    def update_question(self,
                        question_id,
                        enonce=None,
                        type=None,
                        bonne_reponse=None,
                        proposition1=None,
                        proposition2=None):
        question = Question.query.get(question_id)
        if not question:
            return None

        if enonce is not None:
            question.Enonce = enonce
        if type is not None:
            question.Type = type

        if bonne_reponse is not None:
            if isinstance(question, QuestionOuverte):
                question.Reponse = bonne_reponse
            elif isinstance(question, QuestionFermee):
                question.BonneReponse = bonne_reponse

        if proposition1 is not None and isinstance(question, QuestionFermee):
            question.Proposition1 = proposition1
        if proposition2 is not None and isinstance(question, QuestionFermee):
            question.Proposition2 = proposition2

        db.session.commit()
        return question


def get_questionnaires():
    return Questionnaire.query.all()


def get_questionnaire(questionnaire_id):
    return Questionnaire.query.get(questionnaire_id)


def create_questionnaire(nom):
    questionnaire = Questionnaire(Title=nom)
    db.session.add(questionnaire)
    db.session.commit()


def delete_questionnaire(questionnaire_id):
    questionnaire = Questionnaire.query.get(questionnaire_id)
    if questionnaire:
        db.session.delete(questionnaire)
        db.session.commit()


def add_question(questionnaire_id,
                 enonce,
                 type='question_ouverte',
                 bonne_reponse=None,
                 proposition1=None,
                 proposition2=None):
    # scalar ( none si rien, sinon valeur )
    # https://stackoverflow.com/questions/55662957/what-is-the-difference-between-one-and-scalar
    max_numero = db.session.query(db.func.max(Question.Numero)).filter_by(
        questionnaire_id=questionnaire_id).scalar()
    numero = (max_numero or 0) + 1

    question = None
    if type == 'question_ouverte':
        question = QuestionOuverte(enonce,
                                   numero=numero,
                                   questionnaire=questionnaire_id,
                                   reponse=bonne_reponse)
    elif type == 'question_fermee':
        question = QuestionFermee(enonce,
                                  numero=numero,
                                  questionnaire=questionnaire_id,
                                  proposition1=proposition1,
                                  proposition2=proposition2,
                                  bonne_reponse=bonne_reponse)
    db.session.add(question)
    db.session.commit()
    return question
