import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import { createRouter, createWebHistory } from "vue-router";
import QuestionnaireView from "./views/QuestionnaireView.vue";
import QuestionnaireDetail from "./views/QuestionnaireDetail.vue";

const routes = [
  { path: "/questionnaires", component: QuestionnaireView },
  { path: "/questionnaires/:id", component: QuestionnaireDetail }
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});

createApp(App).use(router).mount("#app");
