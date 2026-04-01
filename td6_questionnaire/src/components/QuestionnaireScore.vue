<script setup>
import { computed } from 'vue';

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

const getBonneReponse = (q) => {
  return q.Reponse || q.BonneReponse || q.bonne_reponse || '';
};
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

      <h4 class="mt-5 mb-3 border-bottom pb-2">Résumé de vos réponses</h4>
      
      <div class="list-group">
        <div 
          class="list-group-item list-group-item-action flex-column align-items-start mb-2 rounded border"
          v-for="(q, index) in questions"
          :key="q.id"
          :class="answers[q.id]?.isCorrect ? 'border-success' : 'border-danger'"
        >
          <div class="d-flex w-100 justify-content-between">
            <h6 class="mb-1 fw-bold">Question {{ index + 1 }}</h6>
            <span v-if="answers[q.id]?.isCorrect" class="badge bg-success rounded-pill d-flex align-items-center">
               Correct
            </span>
            <span v-else class="badge bg-danger rounded-pill d-flex align-items-center">
               Incorrect
            </span>
          </div>
          
          <p class="mb-2 mt-2">{{ q.enonce }}</p>
          
          <div class="p-2 rounded bg-light">
            <p class="mb-1">
              <strong>Votre réponse : </strong> 
              <span :class="answers[q.id]?.isCorrect ? 'text-success' : 'text-danger'">
                 {{ answers[q.id]?.answer || 'Aucune réponse' }}
              </span>
            </p>
            
            <p class="mb-0 text-success" v-if="!answers[q.id]?.isCorrect">
              <strong>Bonne réponse : </strong> {{ getBonneReponse(q) }}
            </p>
          </div>
        </div>
      </div>
      
      <div class="text-center mt-5">
        <router-link to="/questionnaires" class="btn btn-primary px-4 py-2">Retourner à l'accueil</router-link>
      </div>
    </div>
  </div>
</template>
