<template lang="pug">
  div#addStock
    input(type="text" v-model="stock.name")
    input(type="text" v-model="stock.code")
    div {{ stock.name }}
    div {{ stock.code }}
    div {{ stock.type }}
    div {{ stock.createdDateTime }}
    div {{ stock.deleted }}
    button(v-on:click="addStock") Add
</template>

<script>
export default {
  data () {
    return {
      stock: {
        name: '',
        code: '',
        type: 'individual',
        createdDateTime: Date.now(),
        deleted: 'FALSE'
      }
    }
  },
  methods: {
    addStock: function () {
      this.axios.post('/api/stock/save', JSON.stringify(this.stock)).then((res) => {
        console.log(res)
      })
    }
  }
}
</script>

<style lang="css">
</style>
