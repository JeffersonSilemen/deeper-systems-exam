<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
import Button from "primevue/button";
import EditUserDialog from "../components/EditUserDialog.vue";
import DeleteUserDialog from "../components/DeleteUserDialog.vue";

const route = useRoute();
const router = useRouter();
const user = ref(null);
const showEdit = ref(false);
const showDelete = ref(false);

const fetchUser = async () => {
  const userId = route.params.id;
  const response = await axios.get(`http://127.0.0.1:5000/users/${userId}`);
  user.value = response.data;
};

const goBack = () => {
  router.push("/");
};

onMounted(fetchUser);
</script>


<template>
  <div class="user-container">
    <h2>User Details</h2>
    
    <div class="user-info">
      <p><strong>Username:</strong> {{ user?.username }}</p>
      <p><strong>Roles:</strong> {{ user?.roles.join(", ") }}</p>
      <p><strong>Timezone:</strong> {{ user?.preferences.timezone }}</p>
      <p><strong>Active:</strong> 
        <i v-if="user?.active" class="pi pi-check text-green-500"></i>
        <i v-else class="pi pi-times text-red-500"></i>
      </p>
      <p><strong>Created At:</strong> {{ user?.created_ts }}</p>
      <p><strong>Last Updated At:</strong> {{ user?.last_updated_at || "Not Edited" }}</p>
    </div>

    <div class="button-group">
      <Button label="Edit" icon="pi pi-pencil" class="p-button-warning" @click="showEdit = true" />
      <Button label="Delete" icon="pi pi-trash" class="p-button-danger ml-2" @click="showDelete = true" />
    </div>

    <!-- Modais de edição e exclusão -->
    <EditUserDialog v-model:visible="showEdit" :user="user" @refresh="fetchUser" />
    <DeleteUserDialog v-model:visible="showDelete" :user="user" @refresh="goBack" />
  </div>
</template>
