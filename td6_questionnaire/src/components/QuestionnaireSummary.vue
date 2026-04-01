<script setup>
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

const getBonneReponse = (q) => {
  return q.Reponse || q.BonneReponse || q.bonne_reponse || '';
};
</script>

<template>
  <div class="mt-5">
    <h4 class="mb-3 border-bottom pb-2">Résumé de vos réponses</h4>
    
    <div class="list-group">
      <div 
        class="list-group-item list-group-item-action flex-column align-items-start mb-2"
        v-for="(q, index) in questions"
        :key="q.id"
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
  </div>
</template>
