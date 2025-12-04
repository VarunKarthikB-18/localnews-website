<script setup>
import { ref, onMounted } from 'vue'
import newsService from '../services/newsService'

const savedArticles = ref([])
const loading = ref(true)

async function fetchSaved() {
  try {
    const response = await newsService.getSavedArticles()
    savedArticles.value = response.data
  } catch (err) {
    console.error(err)
  } finally {
    loading.value = false
  }
}

async function remove(id) {
  if (!confirm('Are you sure?')) return
  try {
    await newsService.deleteSavedArticle(id)
    savedArticles.value = savedArticles.value.filter(a => a.id !== id)
  } catch (err) {
    alert('Failed to delete')
  }
}

onMounted(fetchSaved)
</script>

<template>
  <div>
    <h2 class="text-2xl font-bold mb-6">Saved Articles</h2>
    <div v-if="loading" class="text-center">Loading...</div>
    <div v-else-if="savedArticles.length === 0" class="text-center text-gray-500">No saved articles yet.</div>
    <div v-else class="space-y-4">
      <div v-for="item in savedArticles" :key="item.id" class="bg-white p-4 rounded shadow flex justify-between items-start">
        <div>
          <h3 class="text-xl font-bold mb-2">
            <a :href="item.article.url" target="_blank" class="hover:text-blue-600">{{ item.article.title }}</a>
          </h3>
          <p class="text-gray-600 text-sm">{{ item.article.source_name }} • Saved on {{ new Date(item.saved_at).toLocaleDateString() }}</p>
          <div v-if="item.notes" class="mt-2 text-gray-700 italic">"{{ item.notes }}"</div>
        </div>
        <button @click="remove(item.id)" class="text-red-500 hover:text-red-700 ml-4">Delete</button>
      </div>
    </div>
  </div>
</template>
