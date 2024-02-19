<template>

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
      <textarea
        id="content"
        class="form-control"
        v-model="post.content"
        required
      ></textarea>
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
import axios from 'axios';

// setup initial state of component ...
const route = useRoute();

let recordId = route.params.id;

let newRecord = new Post()
newRecord.id = uuidv4()
let post = ref(newRecord);
let errors = ref([]);

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
  post.id = uuidv4()
  post.abstract = "abstract goes here."
  post.title = "test title";
  post.content = "content goes here.";
  post.tags = "tag 1, tag 2, tag 3"
}

function formIsOkay()
{

  this.errors = []
  // check title
  if(this.post.title.length === 0)
  {
    this.errors.push("Title is required")
  }

  // check content
  if(this.post.content.length === 0)
  {
    this.errors.push("Content is required")
  }

  // make sure id is populated
  if(this.post.id.length === 0)
  {
    this.errors.push("Id is required")
  }

  return this.errors.length === 0
}

async function onSave()
{

  if(this.formIsOkay())
  {
    let url = "/api/store-document";

    let postData = {
      "collection": "notes",
      "userId": "sys",
      "name": this.post.title,
      "tags": this.post.tags,
      "data": {...this.post},
      "id": this.post.id
    }

    try {
      const response = await axios.post('/api/store-document', postData);
      console.log(response)
    } catch (error) {
      console.error('Error sending POST request:', error);
    }
  }else{
    alert("Validation errors : " + JSON.stringify(this.errors))
  }





}
</script>
