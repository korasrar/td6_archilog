<script setup>
import { inject, ref, onMounted } from "vue";
import QuestionnaireItem from "../components/QuestionnaireItem.vue";

const provider = inject("quizProvider");
const questionnaires = ref([]);
const newQuestionnaireTitle = ref("");

async function loadQuestionnaires() {
  const result = await provider.getQuestionnaires();
  questionnaires.value = result || [];
}

async function addQuestionnaire() {
  if (newQuestionnaireTitle.value.trim() !== "" && !(await checkDoublonNomQuestionnaire(newQuestionnaireTitle.value))) {
    await provider.addQuestionnaire({ title: newQuestionnaireTitle.value });
    newQuestionnaireTitle.value = "";
    await loadQuestionnaires();
  } else {
    alert("Le titre du questionnaire ne peut pas être vide ou déjà existant.");
  }
}

async function checkDoublonNomQuestionnaire(title) {
  const result = await provider.getQuestionnaires();
  const existing = result.find(q => q.titre_questionnaire === title);
  return !!existing;
}

async function deleteQuestionnaire(id) {
  await provider.deleteQuestionnaire(id);
  await loadQuestionnaires();
}

onMounted(() => {
  loadQuestionnaires();
});
</script>

<template>
  <div class="container mt-5">
    <h1 class="mb-4">Questionnaires</h1>

    <div class="input-group mb-4">
      <input
        v-model="newQuestionnaireTitle"
        type="text"
        class="form-control"
        placeholder="Nouveau questionnaire..."
        @keyup.enter="addQuestionnaire"
      />
      <button class="btn btn-primary" @click="addQuestionnaire">Ajouter</button>
    </div>

    <div class="row">
      <div
        class="col-12 mb-3"
        v-for="q in questionnaires"
        :key="q.id"
      >
        <QuestionnaireItem
          :questionnaire="q"
          @delete="deleteQuestionnaire"
        />
      </div>
    </div>
  </div>
</template>
