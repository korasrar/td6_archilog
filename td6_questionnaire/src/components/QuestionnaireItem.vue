<script setup>
const props = defineProps({
  questionnaire: Object,
});

const emit = defineEmits(["delete", "update"]);

function deleteQuestionnaire() {
  emit("delete", props.questionnaire.id);
}

function updateQuestionnaire() {
  const newNom = prompt("Modifier le questionnaire", props.questionnaire.titre_questionnaire);
  if (newNom) {
    emit("update", {
      questionnaire: props.questionnaire,
      newNomquestionnaire: newNom,
    });
  }
}
</script>

<template>
  <div class="card shadow-sm">
    <div class="card-body">
      <div class="d-flex justify-content-between align-items-center mb-3">
        <h3 class="card-title mb-0">{{ questionnaire.title }}</h3>
        <div>
          <button class="btn btn-warning btn-sm me-2" @click="updateQuestionnaire">Modifier</button>
          <button class="btn btn-danger btn-sm" @click="deleteQuestionnaire">Supprimer</button>
        </div>
      </div>
      
      <h4>Les questions</h4>
      <!-- rien d'autre pour le moment (questions item dans un second temps) -->
    </div>
  </div>
</template>
