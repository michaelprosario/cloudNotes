<template>
  <h3>List of notes</h3>
  <button type="button" class="btn btn-primary" @click="onNew()">New note</button>

  <table>
    <tr>
      <td>Name</td>
    </tr>
    <tr v-for="(record, index) in records"
          :key="index"
          >
          <td>
            <a @click="onSelect(record)">{{ record.name }}</a> 
          </td>
          <td></td>
    </tr>  
  </table>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import Post from "../core/entities/post";
import { v4 as uuidv4 } from 'uuid';
import axios from 'axios';

function onSelect(record)
{
  console.log(record.id)
  this.router.push("/edit-post/" + record.id)
}

function onNew(){
  this.router.push("/edit-post/new")
}

function getRecordsFromServer()
{
  let url = "/api/get-documents";
  const requestData = {
    "keyword": "",
    "collection": "notes",
    "userId": "sys"
  }
  axios.post(url, requestData).then(response => {
    console.log(response)
    if(response.status === 200)
      records.value = response.data.data;
    else
      alert('Error getting records from server.')
  })
}

// setup new record ......................
let recordsArray = [];
let records = ref(recordsArray);
const router = useRouter();

getRecordsFromServer()

</script>
