import api from './api'

export default {
    getNews(params) {
        return api.get('/news', { params })
    },
    getArticle(id) {
        return api.get(`/news/${id}`)
    },
    saveArticle(article) {
        return api.post('/user/saved-articles', article)
    },
    getSavedArticles() {
        return api.get('/user/saved-articles')
    },
    deleteSavedArticle(id) {
        return api.delete(`/user/saved-articles/${id}`)
    }
}
