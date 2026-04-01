from flask import jsonify, abort, make_response, request, url_for, send_from_directory, render_template
from .app import app
from .models import (Questionnaire, Question, get_questionnaires as
                     get_all_questionnaires, get_questionnaire as
                     get_questionnaire_by_id, create_questionnaire as
                     create_questionnaire_db, delete_questionnaire as
                     delete_questionnaire_db, add_question as add_question_db)


@app.route('/docs')
def swagger_ui():
    return render_template('swagger_ui.html')


@app.route('/spec')
def get_spec():
    return send_from_directory(app.root_path, 'openapi.yaml')


@app.route('/')
@app.route('/quiz/api/v1.0/questionnaires', methods=['GET'])
def get_questionnaires():
    questionnaires = get_all_questionnaires()
    return jsonify({'questionnaires': [q.to_json() for q in questionnaires]})


@app.route('/quiz/api/v1.0/questionnaires/<int:questionnaire_id>',
           methods=['GET'])
def get_questionnaire(questionnaire_id):
    questionnaire = get_questionnaire_by_id(questionnaire_id)
    if questionnaire is None:
        abort(404)
    return jsonify({
        "titre_questionnaire":
        questionnaire.Title,
        'questions': [{
            'id':
            question.Id,
            'numero':
            question.Numero,
            'enonce':
            question.Enonce,
            'type':
            question.Type,
            'Reponse':
            question.Reponse if hasattr(question, 'Reponse') else None,
            'Proposition1':
            question.Proposition1
            if hasattr(question, 'Proposition1') else None,
            'Proposition2':
            question.Proposition2
            if hasattr(question, 'Proposition2') else None,
            'BonneReponse':
            question.BonneReponse
            if hasattr(question, 'BonneReponse') else None
        } for question in questionnaire.get_questions()]
    })


@app.route('/quiz/api/v1.0/questionnaires', methods=['POST'])
def create_questionnaire():
    # vérification des données reçues
    if not request.json or not 'title' in request.json or not isinstance(
            request.json['title'], str):
        abort(400)
    # création du nouveau questionnaire dans la BD
    create_questionnaire_db(request.json['title'])
    # récupération du questionnaire créé (le dernier)
    questionnaires = get_all_questionnaires()
    questionnaire = questionnaires[-1] if questionnaires else None
    # retour du nouveau questionnaire
    return jsonify({'questionnaire': questionnaire.to_json()}), 201


@app.route('/quiz/api/v1.0/questionnaires/<int:questionnaire_id>',
           methods=['PUT'])
def update_questionnaire(questionnaire_id):
    # Recherche du questionnaire à modifier avec son id
    questionnaire = get_questionnaire_by_id(questionnaire_id)
    # le questionnaire avec cette id n’existe pas
    if questionnaire is None:
        abort(404)
    #la requête n’est pas au format json
    if not request.json:
        abort(400)
    # Verification des types
    if 'title' in request.json and not isinstance(request.json['title'], str):
        abort(400)
    # mise à jour des champs du questionnaire
    from .app import db
    questionnaire.Title = request.json.get('title', questionnaire.Title)
    db.session.commit()
    return jsonify({'questionnaire': questionnaire.to_json()})


@app.route('/quiz/api/v1.0/questionnaires/<int:questionnaire_id>',
           methods=['DELETE'])
def delete_questionnaire(questionnaire_id):
    # Recherche du questionnaire à supprimer avec son id
    questionnaire = get_questionnaire_by_id(questionnaire_id)
    # le questionnaire avec cette id n'existe pas
    if questionnaire is None:
        abort(404)
    # suppression du questionnaire dans la BD
    delete_questionnaire_db(questionnaire_id)
    return jsonify({'result': True})


@app.route('/quiz/api/v1.0/questionnaires/<int:questionnaire_id>/questions',
           methods=['POST'])
def add_question(questionnaire_id):
    # Recherche du questionnaire auquel ajouter une question
    questionnaire = get_questionnaire_by_id(questionnaire_id)
    # le questionnaire avec cette id n’existe pas
    if questionnaire is None:
        abort(404)
    # vérification des données reçues
    if not request.json or not 'enonce' in request.json:
        abort(400)

    if not request.json or not 'bonne_reponse' in request.json:
        abort(400)

    if not request.json or not 'type' in request.json:
        abort(400)
    # ajout de la question au questionnaire dans la BD
    add_question_db(questionnaire_id, request.json['enonce'],
                    request.json['type'], request.json['bonne_reponse'],
                    request.json.get('proposition1', None),
                    request.json.get('proposition2', None))
    return jsonify({
        'questions': [{
            'id':
            question.Id,
            'numero':
            question.Numero,
            'enonce':
            question.Enonce,
            'type':
            question.Type,
            'Reponse':
            question.Reponse if hasattr(question, 'Reponse') else None,
            'Proposition1':
            question.Proposition1
            if hasattr(question, 'Proposition1') else None,
            'Proposition2':
            question.Proposition2
            if hasattr(question, 'Proposition2') else None,
            'BonneReponse':
            question.BonneReponse
            if hasattr(question, 'BonneReponse') else None
        } for question in questionnaire.get_questions()]
    }), 201


@app.route(
    '/quiz/api/v1.0/questionnaires/<int:questionnaire_id>/questions/<int:question_id>',
    methods=['DELETE'])
def delete_question(questionnaire_id, question_id):
    # Recherche du questionnaire auquel supprimer une question
    questionnaire = get_questionnaire_by_id(questionnaire_id)
    # le questionnaire avec cette id n'existe pas
    if questionnaire is None:
        abort(404)
    # suppression de la question du questionnaire dans la BD
    questionnaire.delete_question(question_id)
    return jsonify({'result': True})


@app.route(
    '/quiz/api/v1.0/questionnaires/<int:questionnaire_id>/questions/<int:question_id>',
    methods=['PUT'])
def update_question(questionnaire_id, question_id):
    # Recherche du questionnaire auquel modifier une question
    questionnaire = get_questionnaire_by_id(questionnaire_id)
    # le questionnaire avec cette id n'existe pas
    if questionnaire is None:
        abort(404)
    #la requête n’est pas au format json
    if not request.json:
        abort(400)
    # Verification des types
    if 'enonce' in request.json and not isinstance(request.json['enonce'],
                                                   str):
        abort(400)
    if 'type' in request.json and not isinstance(request.json['type'], str):
        abort(400)
    if 'bonne_reponse' in request.json and not isinstance(
            request.json['bonne_reponse'], str):
        abort(400)
    # mise à jour des champs de la question dans la BD
    question = questionnaire.update_question(
        question_id, request.json.get('enonce', None),
        request.json.get('type', None),
        request.json.get('bonne_reponse', None),
        request.json.get('proposition1', None),
        request.json.get('proposition2', None))
    if question is None:
        abort(404)
    return jsonify({'result': True})


@app.route('/quiz/api/v1.0/questionnaires/<int:questionnaire_id>/questions',
           methods=['GET'])
def get_questions(questionnaire_id):
    # Recherche du questionnaire dont on veut les questions
    questionnaire = get_questionnaire_by_id(questionnaire_id)
    # le questionnaire avec cette id n'existe pas
    if questionnaire is None:
        abort(404)
    # retour des questions du questionnaire
    return jsonify({
        'questions': [{
            'id':
            question.Id,
            'numero':
            question.Numero,
            'enonce':
            question.Enonce,
            'type':
            question.Type,
            'Reponse':
            question.Reponse if hasattr(question, 'Reponse') else None,
            'Proposition1':
            question.Proposition1
            if hasattr(question, 'Proposition1') else None,
            'Proposition2':
            question.Proposition2
            if hasattr(question, 'Proposition2') else None,
            'BonneReponse':
            question.BonneReponse
            if hasattr(question, 'BonneReponse') else None
        } for question in questionnaire.get_questions()]
    })


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)
