# Rapport

## Lancement du client

```bash
cd td6_questionnaire/
npm install
npm run dev
```

### Lancement de l'api

```bash
cd td2_bd
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run
```

## Les différents composants et leurs rôle

### QuestionnairePlay.vue

Ce composant est la vue qui permet de jouer à un questionnaire, il contient les fonctions qui permettent de naviguer dans le questionnaire. Ces fonctions sont appelées quand
