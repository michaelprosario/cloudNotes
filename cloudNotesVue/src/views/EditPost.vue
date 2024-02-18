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
    <button type="button" class="btn btn-primary" @click="onSave()">Save</button>
  </form>
</template>

<script setup>
import { ref } from "vue";
import { useRoute } from "vue-router";
import Post from "../core/entities/post";
import { v4 as uuidv4 } from 'uuid';

// setup initial state of component ...
const route = useRoute();

let recordId = route.params.id;

let post = ref(new Post());
if(!recordId)
{
  alert('id not defined');
}
else if(recordId !== "new")
{
  /*
  - https://github.com/sbkwgh/forum/blob/master/frontend/src/components/AdminCategories.vue
  - how to do a vue on click
  - create a class for http operations
  - how does vue handle dependency injection
  - implement save new record operation

  */
  post = new Post()
  post.id = str(uuidv4())
  post.abstract = "abstract goes here."
  post.title = "test title";
  post.content = "content goes here.";
  post.tags = "tag 1, tag 2, tag 3"
}

function onSave()
{
  
  let url = "/api/store-document";

  let body = {
    "collection": "notes",
    "userId": "sys",
    "name": this.post.title,
    "tags": this.post.tags,
    "data": this.post,
    "id": this.post.id
  }

const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: body
};

fetch(url, requestOptions)
    .then(async response => {
        const isJson = response.headers.get('content-type')?.includes('application/json');
        const data = isJson && await response.json();
        console.log(data)
        
        if (!response.ok) {
            // get error message from body or default to response status
            const error = (data && data.message) || response.status;
            return Promise.reject(error);
        }

        alert("record saved");

        
    })
    .catch(error => {
        errorMessage.value = error;
        console.error("There was an error!", error);
    });

}



</script>
