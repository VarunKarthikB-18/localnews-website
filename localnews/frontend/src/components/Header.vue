<script setup>
import { useUserStore } from '../store'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
const router = useRouter()

function logout() {
  userStore.logout()
  router.push('/login')
}
</script>

<template>
  <header class="bg-white/80 backdrop-blur-md sticky top-0 z-50 border-b border-gray-100">
    <div class="container mx-auto px-4 h-16 flex justify-between items-center">
      <router-link to="/" class="text-2xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-indigo-600 hover:opacity-80 transition">
        LocalNews
      </router-link>
      
      <nav class="flex gap-6 items-center font-medium">
        <router-link to="/feed" class="text-gray-600 hover:text-blue-600 transition-colors">News Feed</router-link>
        
        <template v-if="userStore.isAuthenticated">
          <router-link to="/saved" class="text-gray-600 hover:text-blue-600 transition-colors">Saved</router-link>
          <router-link to="/preferences" class="text-gray-600 hover:text-blue-600 transition-colors">Preferences</router-link>
          <button @click="logout" class="text-red-500 hover:text-red-700 transition-colors font-semibold">Logout</button>
        </template>
        
        <template v-else>
          <router-link to="/login" class="text-gray-600 hover:text-blue-600 transition-colors">Login</router-link>
          <router-link to="/register" class="bg-blue-600 text-white px-5 py-2 rounded-full hover:bg-blue-700 transition-all shadow-md hover:shadow-lg transform hover:-translate-y-0.5">
            Get Started
          </router-link>
        </template>
      </nav>
    </div>
  </header>
</template>

<style scoped>
/* Add some basic styling for nav if tailwind not fully present */
nav a {
  text-decoration: none;
}
</style>
