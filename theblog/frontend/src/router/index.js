import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import calender from '../components/calender.vue'
import letters from '../components/letters.vue'
import home from '../components/home.vue'
import markdown from '../components/markdown.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },

       {
      path: '/letters',
      name: 'letters',
      component: letters
    },
    {
      path: '/calender',
      name: 'calender',
      component: calender
    },
      {
      path: '/markdown',
      name: 'markdown',
      component: markdown
    },
  ]
})

export default router
