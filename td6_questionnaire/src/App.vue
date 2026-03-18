<script setup>
import { ref, provide } from "vue";

import { QuizProvider } from "./services/QuizProvider";
import { API_ENDPOINT } from "./config.js";
const provider = new QuizProvider(API_ENDPOINT);
provide("quizProvider", provider);

import QuestionnaireView from "./views/QuestionnaireView.vue";
</script>

<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
      <div class="container">
        <span class="navbar-brand">Quiz App</span>
        <div class="navbar-nav mx-auto">
          <RouterLink class="nav-link" active-class="active" to="/questionnaires">Questionnaires</RouterLink>
        </div>
        <span class="navbar-text text-grey">
          {{ $route.name || $route.path }}
        </span>
      </div>
    </nav>
  </header>
  <main class="container">
    <RouterView />
  </main>
</template>

<style scoped></style>
