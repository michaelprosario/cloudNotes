import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/edit-post/:id',
      name: 'editPost',
      component: () => import('../views/EditPost.vue')
    },
    {
      path: '/list-posts',
      name: 'listPosts',
      component: () => import('../views/ListPosts.vue')
    },
  ]
})

export default router
