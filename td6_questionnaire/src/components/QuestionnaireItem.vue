<script setup>
const props = defineProps({
  questionnaire: Object,
});

const emit = defineEmits(["delete"]);

function deleteQuestionnaire() {
  emit("delete", props.questionnaire.id);
}
</script>

<template>
  <div class="card shadow-sm">
    <div class="card-body">
      <div class="d-flex justify-content-between align-items-center mb-3">
        <h3 class="card-title mb-0">{{ questionnaire.title }}</h3>
        <div>
          <router-link
            :to="`/questionnaires/${questionnaire.id}`"
            class="btn btn-info btn-sm me-2"
            >Voir</router-link
          >
          <router-link
            :to="`/questionnaires/${questionnaire.id}/edit`"
            class="btn btn-warning btn-sm me-2"
            >Modifier</router-link
          >
          <button class="btn btn-danger btn-sm" @click="deleteQuestionnaire">
            Supprimer
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
