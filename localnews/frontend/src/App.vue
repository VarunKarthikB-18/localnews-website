<script setup>
import Header from './components/Header.vue'
</script>

<template>
  <Header />
  <main class="container mx-auto p-4">
    <router-view />
  </main>
</template>

<style>
/* Basic reset/styles if not using Tailwind */
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  margin: 0;
  background-color: #f3f4f6;
}
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}
</style>
