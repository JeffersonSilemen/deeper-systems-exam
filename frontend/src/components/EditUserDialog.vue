<script setup>
import { ref, defineProps, defineEmits, watch } from "vue";
import axios from "axios";
import Dialog from "primevue/dialog";
import InputText from "primevue/inputtext";
import Button from "primevue/button";
import MultiSelect from "primevue/multiselect";
import Checkbox from "primevue/checkbox";

const visible = defineModel("visible");
const emit = defineEmits(["refresh"]);
const props = defineProps(["user"]);

const username = ref("");
const roles = ref([]);
const timezone = ref("");
const active = ref(true);

watch(
  () => props.user,
  (newUser) => {
    if (newUser) {
      username.value = newUser.username;
      roles.value = newUser.roles;
      timezone.value = newUser.preferences.timezone;
      active.value = newUser.active;
    }
  },
  { immediate: true }
);

const roleOptions = ["admin", "manager", "user"];

const updateUser = async () => {
  await axios.put(`http://127.0.0.1:5000/users/${props.user._id}`, {
    username: username.value,
    roles: roles.value,
    preferences: { timezone: timezone.value },
    active: active.value,
  });

  visible.value = false;
  emit("refresh");
};
</script>

<template>
  <Dialog v-model:visible="visible" header="Edit User" modal>
    <div>
      <label>Username</label>
      <InputText v-model="username" class="w-full mb-2" />

      <label>Roles</label>
      <MultiSelect v-model="roles" :options="roleOptions" placeholder="Selecione funções" class="w-full mb-2" />

      <label>Timezone</label>
      <InputText v-model="timezone" class="w-full mb-2" />

      <div class="flex align-items-center mb-2">
        <Checkbox v-model="active" :binary="true" />
        <label class="ml-2">Active</label>
      </div>

      <Button label="Save" icon="pi pi-check" @click="updateUser" class="p-button-primary w-full" />
    </div>
  </Dialog>
</template>
