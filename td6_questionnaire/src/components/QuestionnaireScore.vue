<script setup>
import { computed } from 'vue';
import QuestionnaireSummary from './QuestionnaireSummary.vue';

const props = defineProps({
  questions: {
    type: Array,
    required: true
  },
  answers: {
    type: Object,
    required: true
  }
});

const score = computed(() => {
  return Object.values(props.answers).filter(val => val.isCorrect).length;
});
</script>

<template>
  <div class="card mb-4 shadow-sm">
    <div class="card-body py-4">
      <div class="text-center mb-4">
        <h2 class="card-title text-success mb-3">Quiz terminé !</h2>
        <h4 class="display-5 font-weight-bold">
          Score : {{ score }} / {{ questions.length }}
        </h4>
      </div>

      <QuestionnaireSummary 
        :questions="questions" 
        :answers="answers" 
      />
      
      <div class="text-center mt-5">
        <router-link to="/questionnaires" class="btn btn-primary px-4 py-2">Retourner à l'accueil</router-link>
      </div>
    </div>
  </div>
</template>
