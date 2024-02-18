<template>
  <form @submit.prevent="createPost">
    <div>
      <label for="title">Title:</label>
      <input type="text" id="title" v-model="post.title" required />
    </div>
    <div>
      <label for="slug">Slug:</label>
      <input type="text" id="slug" v-model="post.slug" required />
    </div>
    <div>
      <label for="abstract">Abstract (Optional):</label>
      <textarea id="abstract" v-model="post.abstract"></textarea>
    </div>
    <div>
      <label for="content">Content:</label>
      <textarea id="content" v-model="post.content" required></textarea>
    </div>
    <div>
      <label for="tags">Tags (comma-separated):</label>
      <input type="text" id="tags" v-model="post.tags" />
    </div>
    <button type="submit">Create Post</button>
  </form>
</template>

<script setup>
import { ref } from "vue";
import { useRoute } from "vue-router";
import Post from "../core/entities/post";

// setup initial state of component ...
const route = useRoute();

let recordId = route.params.id;

let post = ref(new Post());
if(!recordId)
{
  alert('id not defined');
}
else if(recordId === "new")
{
  alert('new record case');
}



</script>
