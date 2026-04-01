<script setup>
const props = defineProps({
  score: {
    type: Number,
    required: true
  },
  total: {
    type: Number,
    required: true
  }
});
</script>

<template>
  <div class="card mb-4 shadow-sm text-center">
    <div class="card-body py-5">
      <h2 class="card-title text-success mb-4">Quiz terminé !</h2>
      <h4 class="display-4 font-weight-bold">
        Score : {{ score }} / {{ total }}
      </h4>
      <p class="text-muted mt-3">Merci d'avoir participé.</p>
      <router-link to="/questionnaires" class="btn btn-primary mt-4">Retourner à l'accueil</router-link>
    </div>
  </div>
</template>
