<template lang="pug">
  div.hello
    h1 {{ msg }}
    h2 Essential Links
    div
      h2 GET data from Django API (/api/test)
      div.wrapper
        p /api/test
          span foo:
          span {{ testData.data.foo }}
        p add tod api test
          span add:
          span {{ additional.data.message }}
    //- canvas#myChart(v-load-data="chartData")
</template>

<script>
// import Chart from 'chart.js'
// //
// var ctx = document.getElementById("myChart")
// var myChart = new Chart(ctx, {
//     type: 'bar',
//     data: {
//         labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
//         datasets: [{
//             label: '# of Votes',
//             data: [12, 19, 3, 5, 2, 3],
//             backgroundColor: [
//                 'rgba(255, 99, 132, 0.2)',
//                 'rgba(54, 162, 235, 0.2)',
//                 'rgba(255, 206, 86, 0.2)',
//                 'rgba(75, 192, 192, 0.2)',
//                 'rgba(153, 102, 255, 0.2)',
//                 'rgba(255, 159, 64, 0.2)'
//             ],
//             borderColor: [
//                 'rgba(255,99,132,1)',
//                 'rgba(54, 162, 235, 1)',
//                 'rgba(255, 206, 86, 1)',
//                 'rgba(75, 192, 192, 1)',
//                 'rgba(153, 102, 255, 1)',
//                 'rgba(255, 159, 64, 1)'
//             ],
//             borderWidth: 1
//         }]
//     },
//     options: {
//         scales: {
//             yAxes: [{
//                 ticks: {
//                     beginAtZero:true
//                 }
//             }]
//         }
//     }
// });

export default {
  name: 'hello',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
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
