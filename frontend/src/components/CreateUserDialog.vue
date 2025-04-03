<script setup>
import { ref, defineEmits } from "vue";
import axios from "axios";
import Dialog from "primevue/dialog";
import InputText from "primevue/inputtext";
import Button from "primevue/button";
import MultiSelect from "primevue/multiselect";

const visible = defineModel("visible");
const emit = defineEmits(["refresh"]);

const username = ref("");
const password = ref("");
const roles = ref([]);
const timezone = ref("");

const roleOptions = ["admin", "manager", "user"];

const createUser = async () => {
  await axios.post("http://127.0.0.1:5000/users", {
    username: username.value,
    password: password.value,
    roles: roles.value,
    preferences: { timezone: timezone.value },
    created_ts: new Date().toISOString(),
  });

  visible.value = false;
  emit("refresh");
};
</script>

<template>
  <Dialog v-model:visible="visible" header="Create User" modal>
    <div>
      <label>Username</label>
      <InputText v-model="username" class="w-full mb-2" />

      <label>Password</label>
      <InputText v-model="password" type="password" class="w-full mb-2" />

      <label>Roles</label>
      <MultiSelect v-model="roles" :options="roleOptions" placeholder="Select roles" class="w-full mb-2" />

      <label>Timezone</label>
      <InputText v-model="timezone" class="w-full mb-2" />

      <Button label="Create" icon="pi pi-check" @click="createUser" class="p-button-success w-full" />
    </div>
  </Dialog>
</template>
