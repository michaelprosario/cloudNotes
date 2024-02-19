<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>

<div class="container">
  <div class="row">
    <div class="col-2">
      <ul>
        <li><RouterLink to="/">Home</RouterLink></li>
        <li><RouterLink to="/list-posts">List Posts</RouterLink></li>
        <li><RouterLink to="/edit-post/new">New post</RouterLink></li>
      </ul>
    </div>
    <div class="col-10">
      <RouterView />
    </div>
  </div>
</div>

  
</template>

<style scoped>
</style>
