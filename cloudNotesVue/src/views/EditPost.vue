<template>
<!--
  <div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Email address</label>
  <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
</div>
--> 
  <form>
    <div>
      <label for="title" class="form-label">Title:</label>
      <input type="text" class="form-control" id="title" v-model="post.title" required />
    </div>
    <div>
      <label for="abstract" class="form-label">Abstract (Optional):</label>
      <textarea id="abstract" class="form-control" v-model="post.abstract"></textarea>
    </div>
    <div>
      <label for="content" class="form-label">Content:</label>
      <textarea id="content" class="form-control" v-model="post.content" required></textarea>
    </div>
    <div>
      <label for="tags" class="form-label">Tags (comma-separated):</label>
      <input type="text" id="tags" class="form-control" v-model="post.tags" />
    </div>
    <button type="button" class="btn btn-primary">Create Post</button>
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
}else{
  post = new Post()
  post.abstract = "abstract goes here."
  post.title = "test title";
  post.content = "content goes here.";
  post.tags = "tag 1, tag 2, tag 3"
}



</script>
