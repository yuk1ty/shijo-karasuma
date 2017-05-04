<template>
  <div id="app">
    <p>Stock Code</p>
    <input v-model="stock.code" placeholder="Stock Code">
    <p>Stock Name</p>
    <input v-model="stock.name" placeholder="Stock Name">
    <p>Type</p>
    <select v-model="stock.type">
      <option>Index</option>
      <option>Individual</option>
    </select>
    <button type="button" name="button" v-on:click="addIssue()">Register</button>
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
    }
  },
  methods: {
    addIssue: function () {
      const self = this
      let toSave = self.stock
      self.axios.post('/api/stock/save', JSON.stringify(toSave)).then((res) => {
        // TODO ちゃんとしたダイアログが立ち上がるようにするべき
        alert("登録が完了しました。")
      }).catch((res) => {
        console.log("error!: " + res)
      })
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
