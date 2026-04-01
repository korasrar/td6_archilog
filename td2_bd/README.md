# Quiz API

API REST pour gérer des questionnaires et leurs questions, construite avec Flask et SQLAlchemy.

---

## Lancer l'application

### 1. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Initialiser la base de données

```bash
flask syncdb
```

### 4. Démarrer le serveur

```bash
flask run
```

L'application est accessible sur `http://127.0.0.1:5000`.

> **Documentation OPENAPI** disponible sur `http://127.0.0.1:5000/docs`

---

## Commandes curl

### Questionnaires

#### Lister tous les questionnaires

```bash
curl http://127.0.0.1:5000/quiz/api/v1.0/questionnaires
```

#### Obtenir un questionnaire par ID

```bash
curl http://127.0.0.1:5000/quiz/api/v1.0/questionnaires/1
```

#### Créer un questionnaire

```bash
curl -X POST http://127.0.0.1:5000/quiz/api/v1.0/questionnaires \
  -H "Content-Type: application/json" \
  -d '{"title": "Mon nouveau quiz"}'
```

#### Modifier un questionnaire

```bash
curl -X PUT http://127.0.0.1:5000/quiz/api/v1.0/questionnaires/3 \
  -H "Content-Type: application/json" \
  -d '{"title": "Titre modifié"}'
```

#### Supprimer un questionnaire

```bash
curl -X DELETE http://127.0.0.1:5000/quiz/api/v1.0/questionnaires/3
```

---

### Questions

#### Lister les questions d'un questionnaire

```bash
curl http://127.0.0.1:5000/quiz/api/v1.0/questionnaires/3/questions
```

#### Ajouter une question ouverte

```bash
curl -X POST http://127.0.0.1:5000/quiz/api/v1.0/questionnaires/3/questions \
  -H "Content-Type: application/json" \
  -d '{"enonce": "Quelle est la capitale de la France ?", "type": "question_ouverte", "bonne_reponse": "Paris"}'
```

#### Ajouter une question fermée (QCM)

```bash
curl -X POST http://127.0.0.1:5000/quiz/api/v1.0/questionnaires/3/questions \
  -H "Content-Type: application/json" \
  -d '{"enonce": "Combien font 2 + 2 ?", "type": "question_fermee", "bonne_reponse": "4", "proposition1": "3", "proposition2": "4"}'
```

#### Supprimer une question

```bash
curl -X DELETE http://127.0.0.1:5000/quiz/api/v1.0/questionnaires/3/questions/1
```
