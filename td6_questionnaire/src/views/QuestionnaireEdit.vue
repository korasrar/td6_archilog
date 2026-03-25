<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { QuizProvider } from '../services/QuizProvider';
import { API_ENDPOINT } from '../config';
import QuestionItem from '../components/QuestionItem.vue';
import { useAuthStore } from '../stores/auth';

const route = useRoute();
const quizProvider = new QuizProvider(API_ENDPOINT);
const authStore = useAuthStore();

const questionnaireId = route.params.id;

const questionnaire = ref({ title: '' });
const questions = ref([]);
const titleSaved = ref(false);

const newQuestion = ref({
  enonce: '',
  type: 'question_ouverte',
  bonne_reponse: '',
  proposition1: '',
  proposition2: ''
});

const loadData = async () => {
  if (!questionnaireId) return;
  try {
    const qData = await quizProvider.getQuestionnaire(questionnaireId);
    questionnaire.value = qData.questionnaire || qData;
    
    const qsData = await quizProvider.getQuestions(questionnaireId);
    questions.value = qsData.questions || qsData;
  } catch (e) {
    console.error('Erreur lors du chargement', e);
  }
};

const updateTitle = async () => {
  try {
    await quizProvider.updateQuestionnaire(questionnaireId, { title: questionnaire.value.title });
    titleSaved.value = true;
    setTimeout(() => { titleSaved.value = false; }, 3000);
  } catch (e) {
    console.error('Erreur lors de la mise à jour du titre', e);
  }
};

const addQuestion = async () => {
  if (!newQuestion.value.enonce) return;
  try {
    await quizProvider.addQuestion(questionnaireId, newQuestion.value);
    newQuestion.value = {
      enonce: '',
      type: 'question_ouverte',
      bonne_reponse: '',
      proposition1: '',
      proposition2: ''
    };
    await loadData();
  } catch (e) {
    console.error('Erreur lors de l\'ajout de la question', e);
  }
};

const deleteQuestion = async (qId) => {
  try {
    await quizProvider.deleteQuestion(questionnaireId, qId);
    await loadData();
  } catch (e) {
    console.error('Erreur lors de la suppression de la question', e);
  }
};

const saveQuestionEdit = async (qId, updatedData) => {
  try {
    await quizProvider.updateQuestion(questionnaireId, qId, updatedData);
    await loadData();
  } catch (e) {
    console.error('Erreur lors de la mise à jour de la question', e);
  }
};

onMounted(() => {
  loadData();
});
</script>

<template>
  <div class="container my-4">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <router-link to="/questionnaires" class="btn btn-outline-secondary">← Retour aux questionnaires</router-link>
      <h1 class="mb-0">Modifier le Questionnaire</h1>
    </div>

    <div class="card mb-4 shadow-sm">
      <div class="card-body">
        <h4 class="card-title mb-3">Informations du questionnaire</h4>
        <div class="mb-3">
          <label for="title" class="form-label">Titre du questionnaire :</label>
          <div class="input-group">
            <input id="title" v-model="questionnaire.titre_questionnaire" type="text" class="form-control" />
            <button class="btn btn-success" @click="updateTitle">Enregistrer le titre</button>
          </div>
          <div v-if="titleSaved" class="form-text text-success mt-1">Titre enregistré avec succès !</div>
        </div>
      </div>
    </div>

    <div class="mb-4">
      <h2 class="mb-3">Questions existantes</h2>
      <div v-if="questions.length === 0" class="alert alert-info">Aucune question dans ce questionnaire.</div>
      
      <QuestionItem 
        v-for="q in questions" 
        :key="q.id" 
        :question="q"
        :readonly="!authStore.isAuthenticated"
        @update="saveQuestionEdit(q.id, $event)"
        @delete="deleteQuestion"
      />
    </div>

    <div class="card mb-4 shadow-sm">
      <div class="card-body">
        <h3 class="card-title mb-4">Ajouter une question</h3>
        <div class="mb-3">
          <label class="form-label">Énoncé :</label>
          <input v-model="newQuestion.enonce" type="text" class="form-control" required />
        </div>
        <div class="mb-3">
          <label class="form-label">Type :</label>
          <select v-model="newQuestion.type" class="form-select">
            <option value="question_ouverte">Ouverte</option>
            <option value="question_fermee">Fermée</option>
          </select>
        </div>
        
        <div v-if="newQuestion.type === 'question_ouverte'" class="mb-3">
          <label class="form-label">Réponse attendue :</label>
          <input v-model="newQuestion.bonne_reponse" type="text" class="form-control" required />
        </div>
        
        <div v-if="newQuestion.type === 'question_fermee'">
          <div class="mb-3">
            <label class="form-label">Proposition 1 :</label>
            <input v-model="newQuestion.proposition1" type="text" class="form-control" required />
          </div>
          <div class="mb-3">
            <label class="form-label">Proposition 2 :</label>
            <input v-model="newQuestion.proposition2" type="text" class="form-control" required />
          </div>
          <div class="mb-3">
            <label class="form-label">Bonne réponse :</label>
            <input v-model="newQuestion.bonne_reponse" type="text" class="form-control" required />
          </div>
        </div>

        <button class="btn btn-primary" @click="addQuestion">Ajouter la question</button>
      </div>
    </div>
  </div>
</template>