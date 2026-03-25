<script setup>
import { ref } from 'vue';

const props = defineProps({
  question: Object
});

const emit = defineEmits(['update', 'delete']);

const isEditing = ref(false);
const editData = ref({});

const startEdit = () => {
    // mes nom d'attributs sont un peu incohérents entre les différentes truc, je gère les différentes possibilités ici
  isEditing.value = true;
  editData.value = { 
    ...props.question, 
    bonne_reponse: props.question.Reponse || props.question.BonneReponse || props.question.bonne_reponse,
    proposition1: props.question.Proposition1 || props.question.proposition1,
    proposition2: props.question.Proposition2 || props.question.proposition2
  };
};

const cancelEdit = () => {
  isEditing.value = false;
  editData.value = {};
};

const saveEdit = () => {
  emit('update', editData.value);
  isEditing.value = false;
};
</script>

<template>
  <div class="card mb-3 shadow-sm">
    <div class="card-body">
      <div v-if="isEditing">
        <div class="mb-3">
          <label class="form-label">Énoncé :</label>
          <input v-model="editData.enonce" type="text" class="form-control" />
        </div>
        <div class="mb-3">
          <label class="form-label">Type :</label>
          <select v-model="editData.type" class="form-select">
            <option value="question_ouverte">Ouverte</option>
            <option value="question_fermee">Fermée</option>
          </select>
        </div>

        <div v-if="editData.type === 'question_ouverte'" class="mb-3">
          <label class="form-label">Réponse attendue :</label>
          <input v-model="editData.bonne_reponse" type="text" class="form-control" />
        </div>

        <div v-if="editData.type === 'question_fermee'">
          <div class="mb-3">
            <label class="form-label">Proposition 1 :</label>
            <input v-model="editData.proposition1" type="text" class="form-control" />
          </div>
          <div class="mb-3">
            <label class="form-label">Proposition 2 :</label>
            <input v-model="editData.proposition2" type="text" class="form-control" />
          </div>
          <div class="mb-3">
            <label class="form-label">Bonne réponse :</label>
            <input v-model="editData.bonne_reponse" type="text" class="form-control" />
          </div>
        </div>

        <button class="btn btn-primary me-2" @click="saveEdit">Sauvegarder</button>
        <button class="btn btn-secondary" @click="cancelEdit">Annuler</button>
      </div>

      <div v-else>
        <h5 class="card-title">N°{{ question.numero}} - {{ question.enonce }}</h5>
        <h6 class="card-subtitle mb-3 text-muted">
          {{ question.type === 'question_ouverte' ? 'Ouverte' : 'Fermée' }}
        </h6>
        
        <div v-if="question.type === 'question_ouverte'">
          <p class="card-text"><strong>Réponse :</strong> {{ question.Reponse || question.reponse }}</p>
        </div>
        <div v-if="question.type === 'question_fermee'">
          <p class="card-text mb-1"><strong>Prop 1 :</strong> {{ question.Proposition1 || question.proposition1 }}</p>
          <p class="card-text mb-1"><strong>Prop 2 :</strong> {{ question.Proposition2 || question.proposition2 }}</p>
          <p class="card-text"><strong>Bonne rep :</strong> {{ question.BonneReponse || question.bonne_reponse }}</p>
        </div>

        <div class="mt-3">
          <button class="btn btn-warning me-2" @click="startEdit">Modifier</button>
          <button class="btn btn-danger" @click="$emit('delete', question.id)">Supprimer</button>
        </div>
      </div>
    </div>
  </div>
</template>