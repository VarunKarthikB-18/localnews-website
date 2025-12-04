<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import newsService from '../services/newsService'

const route = useRoute()
const article = ref(null)
const loading = ref(true)

onMounted(async () => {
  try {
    const id = route.params.id
    // In a real app, we might need to fetch by ID from backend if we don't have it
    // But our backend mock just returns a generic detail for any ID
    const response = await newsService.getArticle(id)
    article.value = response.data
  } catch (err) {
    console.error(err)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div v-if="loading" class="text-center py-8">Loading...</div>
  <div v-else-if="article" class="max-w-3xl mx-auto bg-white p-8 rounded shadow">
    <h1 class="text-3xl font-bold mb-4">{{ article.title }}</h1>
    <div class="text-gray-600 mb-6">{{ article.source_name }}</div>
    <div class="prose max-w-none">
      {{ article.content }}
    </div>
    <div class="mt-8 pt-4 border-t">
      <a :href="article.url" target="_blank" class="text-blue-500 hover:underline">Read full article at source</a>
    </div>
  </div>
  <div v-else class="text-center py-8">Article not found</div>
</template>
