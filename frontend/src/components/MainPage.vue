<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import Button from "primevue/button";
import Dialog from "primevue/dialog";
import CreateUserDialog from "./CreateUserDialog.vue";
import EditUserDialog from "./EditUserDialog.vue";
import DeleteUserDialog from "./DeleteUserDialog.vue";

const users = ref([]);
const router = useRouter();
const showCreateDialog = ref(false);
const selectedUser = ref(null);
const showEditDialog = ref(false);
const showDeleteDialog = ref(false);

const fetchUsers = async () => {
  const response = await axios.get("http://127.0.0.1:5000/users");
  users.value = response.data;
};

onMounted(fetchUsers);
</script>

<template>
  <div>
    <Button label="New User" icon="pi pi-plus" @click="showCreateDialog = true" />

    <DataTable :value="users">
      <Column field="username" header="Username">
        <template #body="{ data }">
          <router-link :to="'/user/' + data._id">{{ data.username }}</router-link>
        </template>
      </Column>
      <Column field="roles" header="Roles" />
      <Column field="preferences.timezone" header="Timezone" />
      <Column field="active" header="Active">
        <template #body="{ data }">
          <span :class="{ 'text-green-500': data.active, 'text-red-500': !data.active }">
            {{ data.active ? "Yes" : "No" }}
          </span>
        </template>
      </Column>
      <Column field="last_updated_at" header="Last Updated">
        <template #body="{ data }">
          {{ data.last_updated_at ? data.last_updated_at : "Not Edited" }}
        </template>
      </Column>
      <Column field="created_ts" header="Created At"/>
      <Column header="Action">
        <template #body="{ data }">
          <Button icon="pi pi-pencil" class="p-button-text" @click="selectedUser = data; showEditDialog = true" />
          <Button icon="pi pi-trash" class="p-button-text p-button-danger" @click="selectedUser = data; showDeleteDialog = true" />
        </template>
      </Column>
    </DataTable>

    <CreateUserDialog v-model:visible="showCreateDialog" @refresh="fetchUsers" />
    <EditUserDialog v-if="selectedUser" v-model:visible="showEditDialog" :user="selectedUser" @refresh="fetchUsers" />
    <DeleteUserDialog v-if="selectedUser" v-model:visible="showDeleteDialog" :user="selectedUser" @refresh="fetchUsers" />
  </div>
</template>
