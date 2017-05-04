<template>
  <div id="app">
    <p>Stock Code</p>
    <input v-model="code" placeholder="Stock Code">
    <p>Stock Name</p>
    <input v-model="name" placeholder="Stock Name">
    <p>Type</p>
    <select v-model="type">
      <option>Index</option>
      <option>Individual</option>
    </select>
    <!-- <span>Selected: {{ type }}</span> -->
    <button type="button" name="button" v-on:click="addIssue">Register</button>
    <!-- <input type="file" id="selfile"> -->
    {{ stock.code }}
    {{ stock.name }}
    {{ stock.type }}
    {{ stock.createdDateTime }}
    {{ stock.deleted }}
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      stock: {
        code: '',
        name: '',
        type: ''
      }
      // code: '',
      // name: '',
      // type: '',
      // stock: ''
    }
  },
  methods: {
    addIssue: function () {
      this.stock = {
        code: this.code,
        name: this.name,
        type: this.type,
        createdDateTime: new Date(),
        deleted: '0'
      }
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
