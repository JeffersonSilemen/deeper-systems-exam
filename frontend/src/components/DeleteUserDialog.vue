<script setup>
import { defineProps, defineEmits } from "vue";
import axios from "axios";
import Dialog from "primevue/dialog";
import Button from "primevue/button";

const visible = defineModel("visible");
const emit = defineEmits(["refresh"]);
const props = defineProps(["user"]);

const deleteUser = async () => {
  await axios.delete(`http://127.0.0.1:5000/users/${props.user._id}`);
  visible.value = false;
  emit("refresh");
};
</script>

<template>
  <Dialog v-model:visible="visible" header="Delete User" modal>
    <p>Are you sure you want to delete the user <strong>{{ user.username }}</strong>?</p>

    <div class="flex justify-content-end mt-4">
      <Button label="Cancel" icon="pi pi-times" class="p-button-text" @click="visible = false" />
      <Button label="Delete" icon="pi pi-trash" class="p-button-danger" @click="deleteUser" />
    </div>
  </Dialog>
</template>
