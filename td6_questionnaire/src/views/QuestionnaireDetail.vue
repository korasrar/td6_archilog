<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { QuizProvider } from "../services/QuizProvider";
import { API_ENDPOINT } from "../config";
import QuestionItem from "../components/QuestionItem.vue";

const route = useRoute();
const quizProvider = new QuizProvider(API_ENDPOINT);

const questionnaireId = route.params.id;

const questionnaire = ref({ title: "" });
const questions = ref([]);

const loadData = async () => {
  if (!questionnaireId) return;
  try {
    const qData = await quizProvider.getQuestionnaire(questionnaireId);
    questionnaire.value = qData.questionnaire || qData;

    const qsData = await quizProvider.getQuestions(questionnaireId);
    questions.value = qsData.questions || qsData;
  } catch (e) {
    console.error("Erreur lors du chargement", e);
  }
};

onMounted(() => {
  loadData();
});
</script>

<template>
  <div class="container my-4">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <router-link to="/questionnaires" class="btn btn-outline-secondary"
        >← Retour aux questionnaires</router-link
      >
      <h1 class="mb-0">Vue du Questionnaire</h1>
      <router-link
        :to="`/questionnaires/${questionnaireId}/edit`"
        class="btn btn-warning"
      >
        Modifier
      </router-link>
    </div>

    <div class="card mb-4 shadow-sm">
      <div class="card-body">
        <h4 class="card-title mb-3">Informations du questionnaire</h4>
        <div class="mb-3">
          <label for="title" class="form-label">Titre du questionnaire :</label>
          <div class="input-group">
            <p class="form-control">{{ questionnaire.titre_questionnaire }}</p>
          </div>
        </div>
      </div>
    </div>

    <div class="mb-4">
      <h2 class="mb-3">Questions existantes</h2>
      <div v-if="questions.length === 0" class="alert alert-info">
        Aucune question dans ce questionnaire.
      </div>

      <QuestionItem v-for="q in questions" :key="q.id" :question="q" readonly />
    </div>
  </div>
</template>
