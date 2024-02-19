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

<script setup lang="ts">
import { ref } from "vue";
import { useRoute } from "vue-router";
import Post from "../core/entities/post";
import { v4 as uuidv4 } from 'uuid';
import axios from 'axios';


function getRecordFromServer(recordId: string, post: Post)
{
  let url = "/api/get-document";
  const postData = {
    "id": recordId,
    "userId": "system"
  }
  axios.post(url, postData).then(response => {
    if(response.status === 200)
      post.value = response.data.record;
    else
      alert('Error getting record from server.')
  })
}

// get url params .......................
const route = useRoute();
let recordId = route.params.id;

// setup new record ......................
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
  getRecordFromServer(recordId, post)
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

function getFormData(){
  let postData = {
    "collection": "notes",
    "userId": "sys",
    "name": this.post.title,
    "tags": this.post.tags,
    "data": {...this.post},
    "id": this.post.id
  }

  return postData;
}

async function onSave()
{

  if(this.formIsOkay())
  {
    const postData = this.getFormData();
    try {
      let url = "/api/store-document";
      const response = await axios.post(url, postData);
      if(response.status === 200){
        alert('Record saved');
      }else{
        alert('Error saving record');
        console.error(response);
      }
    } catch (error) {
      console.error('Error sending POST request:', error);
    }
  }else{
    alert("Validation errors : " + JSON.stringify(this.errors))
  }
}
</script>
