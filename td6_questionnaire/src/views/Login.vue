<script setup>
import { ref } from "vue";
import { useRouter, useRoute } from "vue-router";
import { useAuthStore } from "../stores/auth";

const router = useRouter();
const route = useRoute();
const authStore = useAuthStore();

const password = ref("");
const errorMessage = ref("");

const handleLogin = () => {
  const success = authStore.login(password.value);

  if (success) {
    const redirect = route.query.redirect || "/questionnaires";
    router.push(redirect);
  } else {
    errorMessage.value = "Mot de passe incorrect";
    password.value = "";
  }
};
</script>

<template>
  <div class="container my-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card shadow">
          <div class="card-body p-5">
            <h2 class="text-center mb-4">Connexion</h2>

            <div v-if="errorMessage" class="alert alert-danger">
              {{ errorMessage }}
            </div>

            <form @submit.prevent="handleLogin">
              <div class="mb-3">
                <label for="password" class="form-label">Mot de passe :</label>
                <input
                  id="password"
                  v-model="password"
                  type="password"
                  class="form-control"
                  placeholder="Entrez le mot de passe"
                  required
                  autofocus
                />
                <div class="form-text">
                  Indice : le mot de passe est "admin123"
                </div>
              </div>

              <button type="submit" class="btn btn-primary w-100">
                Se connecter
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
