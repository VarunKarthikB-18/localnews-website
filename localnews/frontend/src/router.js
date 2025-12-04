import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from './components/LandingPage.vue'
import HomeFeed from './components/HomeFeed.vue'
import Login from './components/Login.vue'
import Register from './components/Register.vue'
import ArticleDetail from './components/ArticleDetail.vue'
import SavedArticles from './components/SavedArticles.vue'
import Preferences from './components/Preferences.vue'

const routes = [
    { path: '/', component: LandingPage },
    { path: '/feed', component: HomeFeed },
    { path: '/login', component: Login },
    { path: '/register', component: Register },
    { path: '/saved', component: SavedArticles },
    { path: '/preferences', component: Preferences },
    { path: '/article/:id', component: ArticleDetail, props: true }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
