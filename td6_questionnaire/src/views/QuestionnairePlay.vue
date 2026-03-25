<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { QuizProvider } from '../services/QuizProvider';
import { API_ENDPOINT } from '../config';
import QuestionnairePlayItem from '../components/QuestionnairePlayItem.vue';

const route = useRoute();
const router = useRouter();
const quizProvider = new QuizProvider(API_ENDPOINT);

const questionnaireId = route.params.id;

const questionnaire = ref({ title: '' });
const questions = ref([]);

// Index de la question courante basé sur l'URL
const currentQuestionIndex = computed(() => {
  if (!route.params.questionId) return -1;
  const qId = route.params.questionId;
  return questions.value.findIndex(q => String(q.id) === String(qId));
});

const currentQuestion = computed(() => {
  if (currentQuestionIndex.value === -1 || questions.value.length === 0) return null;
  return questions.value[currentQuestionIndex.value];
});

const loadData = async () => {
  if (!questionnaireId) return;
  try {
    const qData = await quizProvider.getQuestionnaire(questionnaireId);
    questionnaire.value = qData.questionnaire || qData;
    
    const qsData = await quizProvider.getQuestions(questionnaireId);
    questions.value = qsData.questions || qsData;
    
    // Si l'id dans l'URL est manquant ou invalide (et qu'il y a des questions)
    if (questions.value.length > 0 && currentQuestionIndex.value === -1) {
      router.replace(`/questionnaires/${questionnaireId}/play/questions/${questions.value[0].id}`);
    }
  } catch (e) {
    console.error('Erreur lors du chargement', e);
  }
};

const goToNextQuestion = () => {
  if (currentQuestionIndex.value >= 0 && currentQuestionIndex.value < questions.value.length - 1) {
    const nextId = questions.value[currentQuestionIndex.value + 1].id;
    router.push(`/questionnaires/${questionnaireId}/play/questions/${nextId}`);
  }
};

const goToPreviousQuestion = () => {
  if (currentQuestionIndex.value > 0) {
    const prevId = questions.value[currentQuestionIndex.value - 1].id;
    router.push(`/questionnaires/${questionnaireId}/play/questions/${prevId}`);
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
      <h1 class="mb-0">Jouer : {{ questionnaire.titre_questionnaire || questionnaire.title }}</h1>
    </div>

    <div class="mb-4">
      <h2 class="mb-3">Question {{ currentQuestionIndex + 1 }} / {{ questions.length }}</h2>
      <div v-if="questions.length === 0" class="alert alert-info">Aucune question dans ce questionnaire.</div>
      
      <QuestionnairePlayItem 
        v-else-if="currentQuestion"
        :key="currentQuestion.id" 
        :question="currentQuestion" 
        :index="currentQuestionIndex + 1"
      />
      
      <div class="d-flex justify-content-between mt-4" v-if="questions.length > 0">
        <button 
          class="btn btn-secondary" 
          @click="goToPreviousQuestion" 
          :disabled="currentQuestionIndex === 0">
          Question précédente
        </button>
        <button 
          class="btn btn-primary" 
          @click="goToNextQuestion" 
          :disabled="currentQuestionIndex === questions.length - 1">
          Question suivante
        </button>
      </div>
    </div>
  </div>
</template>