<template lang="pug">
  div.hello
    h1 {{ msg }}
    div
      h2 GET data from Django API (/api/test)
      div.wrapper
        p /api/test
          span foo:
          span {{ testData.data.foo }}
        p add tod api test
          span add:
          span {{ additional.data.message }}
</template>

<script>

export default {
  name: 'hello',
  data () {
    return {
      msg: 'Stock Manager',
      testData: {},
      additional: {}
    }
  },
  mounted () {
    console.log('mounted')

    // axiosの疎通テスト
    // エラー吐くかも
    this.axios.get('/api/test').then((res) => {
      console.log(res)
      this.testData = res
    })

    this.axios.post ('/api')

    this.axios.get('/api/do_something').then((res) => {
      console.log(res)
      this.additional = res
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

.wrapper{
  padding: 20px 40px;
  border: 1px solid #c0c0c0;
  max-width: 400px;
  margin: 0 auto;
  background: orange;
}
</style>
