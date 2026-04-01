import { createApp } from "vue";
import { createPinia } from "pinia";
import "./style.css";
import App from "./App.vue";
import { createRouter, createWebHistory } from "vue-router";
import QuestionnaireView from "./views/QuestionnaireView.vue";
import QuestionnaireDetail from "./views/QuestionnaireDetail.vue";
import QuestionnaireEdit from "./views/QuestionnaireEdit.vue";
import LoginView from "./views/Login.vue";
import QuestionnairePlay from "./views/QuestionnairePlay.vue";

const routes = [
  { path: "/questionnaires", component: QuestionnaireView },
  { path: "/questionnaires/:id", component: QuestionnaireDetail },
  { 
    path: "/questionnaires/:id/edit", 
    component: QuestionnaireEdit,
    meta: { requiresAuth: true }
  }, 
  { path: "/login", component: LoginView },
  { path: "/questionnaires/:id/play/questions/:questionId", component: QuestionnairePlay },
  { path: "/", redirect: "/questionnaires" }
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App);
const pinia = createPinia();

app.use(pinia);
app.use(router);

import { useAuthStore } from "./stores/auth";

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  
  authStore.initAuth();
  
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next('/login');
  } else {
    next();
  }
});

app.mount("#app");
