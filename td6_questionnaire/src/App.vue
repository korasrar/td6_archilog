<script setup>
import { ref, provide } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "./stores/auth";

import { QuizProvider } from "./services/QuizProvider";
import { API_ENDPOINT } from "./config.js";

const provider = new QuizProvider(API_ENDPOINT);
provide("quizProvider", provider);

const authStore = useAuthStore();
const router = useRouter();

authStore.initAuth();

const handleLogout = () => {
  authStore.logout();
  router.push("/login");
};
</script>

<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
      <div class="container">
        <span class="navbar-brand">Quiz App</span>
        <div class="navbar-nav mx-auto">
          <RouterLink
            class="nav-link"
            active-class="active"
            to="/questionnaires"
            >Questionnaires</RouterLink
          >
        </div>
        <div class="d-flex align-items-center">
          <span
            v-if="authStore.isAuthenticated"
            class="navbar-text text-light me-3"
          >
            Connecté
          </span>
          <RouterLink
            v-if="!authStore.isAuthenticated"
            to="/login"
            class="btn btn-sm btn-outline-light"
          >
            Se connecter
          </RouterLink>
          <button
            v-if="authStore.isAuthenticated"
            @click="handleLogout"
            class="btn btn-sm btn-outline-light"
          >
            Déconnexion
          </button>
        </div>
      </div>
    </nav>
  </header>
  <main class="container">
    <RouterView />
  </main>
</template>

<style scoped></style>
