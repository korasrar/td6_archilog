<script setup>
import { ref, provide } from "vue";

import { QuizProvider } from "./services/QuizProvider";
import { API_ENDPOINT } from "./config.js";
const provider = new QuizProvider(API_ENDPOINT);
provide("quizProvider", provider);

import QuestionnaireView from "./views/QuestionnaireView.vue";
</script>

<template>
  <div class="container py-4">
    <QuestionnaireView />
  </div>
</template>

<style scoped>
</style>
