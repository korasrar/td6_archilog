<script setup>
import { ref, computed, onMounted } from 'vue';

const props = defineProps({
  question: Object,
  index: Number,
  savedState: {
    type: Object,
    default: null
  }
});

const emit = defineEmits(['answer']);

const userAnswer = ref('');
const answered = ref(false);
const isCorrect = ref(false);

const bonneReponse = computed(() => {
  return props.question.Reponse || props.question.BonneReponse || props.question.bonne_reponse || '';
});

const proposition1 = computed(() => {
  return props.question.Proposition1 || props.question.proposition1 || '';
});

const proposition2 = computed(() => {
  return props.question.Proposition2 || props.question.proposition2 || '';
});

onMounted(() => {
  if (props.savedState) {
    userAnswer.value = props.savedState.answer;
    answered.value = props.savedState.answered;
    isCorrect.value = props.savedState.isCorrect;
  }
});

const checkAnswer = () => {
  if (!userAnswer.value || answered.value) return;
  answered.value = true;
  isCorrect.value = userAnswer.value.toLowerCase().trim() === bonneReponse.value.toLowerCase().trim();
  
  emit('answer', {
    questionId: props.question.id,
    answer: userAnswer.value,
    isCorrect: isCorrect.value,
    answered: true
  });
};
</script>

<template>
  <div class="card mb-3 shadow-sm">
    <div class="card-body">
      <h5 class="card-title">Question {{ index }}</h5>
      <p class="card-text">{{ question.enonce }}</p>

      <div v-if="question.type === 'question_fermee'" class="mb-3">
        <div class="form-check">
          <input class="form-check-input" type="radio" :name="'q' + question.id" :id="'q' + question.id + 'prop1'" :value="proposition1" v-model="userAnswer" :disabled="answered">
          <label class="form-check-label" :for="'q' + question.id + 'prop1'">
            {{ proposition1 }}
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" :name="'q' + question.id" :id="'q' + question.id + 'prop2'" :value="proposition2" v-model="userAnswer" :disabled="answered">
          <label class="form-check-label" :for="'q' + question.id + 'prop2'">
            {{ proposition2 }}
          </label>
        </div>
      </div>

      <div v-else class="mb-3">
        <input type="text" class="form-control" v-model="userAnswer" placeholder="Votre réponse..." :disabled="answered" @keyup.enter="checkAnswer">
      </div>

      <button class="btn btn-primary mt-2" @click="checkAnswer" :disabled="answered || !userAnswer">
        Valider la réponse
      </button>

      <div v-if="answered" class="mt-3 p-2 rounded" :class="isCorrect ? 'bg-success text-white' : 'bg-danger text-white'">
        <p class="mb-0">
          <strong>{{ isCorrect ? 'Bonne réponse !' : 'Mauvaise réponse.' }}</strong>
        </p>
        <p v-if="!isCorrect" class="mb-0 mt-1">La bonne réponse était : {{ bonneReponse }}</p>
      </div>
    </div>
  </div>
</template>