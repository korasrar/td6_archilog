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
flask cleardb
flask syncdb
flask run
```

## Les différents composants et leurs rôle

### Les Vues (Views)

- App.vue : C'est le composant racine qui englobe toute l'application.
- Login.vue : Page permettant à l'utilisateur de se connecter.
- QuestionnaireView.vue : Page listant l'ensemble des questionnaires disponibles.
- QuestionnaireDetail.vue et QuestionnaireEdit.vue : Pages pour consulter ou modifier un questionnaire spécifique.

### Les Composants réutilisables (Components)

- QuestionnaireItem.vue : Affiche un aperçu d'un questionnaire, souvent utilisé dans la liste globale.
- QuestionItem.vue : Gère l'affichage ou l'édition d'une question.
- QuestionnairePlayItem.vue : S'occupe de l'affichage de la question en cours pendant qu'un utilisateur y joue.
- QuestionnaireScore.vue et QuestionnaireSummary.vue : Affichent le score et le récapitulatif à la fin d'une partie.

### Relations et logique ( Routeur )

L'application fonctionne de la manière suivante : **App.vue** charge les "Vues" en fonction de l'URL grâce au **Vue Router**. Le routeur permet de naviguer fluidement entre les différentes pages (comme passer de la connexion à la liste des questionnaires) sans avoir à recharger la page dans le navigateur.

Ces Vues s'appuient ensuite sur les "Composants" pour construire l'interface de manière modulaire. Par exemple, la vue QuestionnairePlay va utiliser QuestionnairePlayItem pour afficher chaque question.

### Pinia

Pour stocker des informations accessibles partout dans l'application (comme l'état de connexion de l'utilisateur), l'application utilise **Pinia** (le gestionnaire d'état). Ces données de session sont conservées dans le store **auth.js**.

### Provider

Enfin, les accès aux données (les communications avec l'API Flask) sont centralisés dans le service **QuizProvider.js**, ce qui permet de séparer la logique de l'interface.
