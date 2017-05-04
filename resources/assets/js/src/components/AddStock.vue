<template lang="pug">
  section.wrapper
    h1 {{ stockName }}
    canvas#canvas
</template>

<script>
import Chart from 'chart.js'
export default {
  data () {
    return {
      chart: '',
      chartData: {},
      stockName: 'Sony'
    }
  },
  methods: {
    getData () {
      this.chartData = {
        type: 'line',
        data:  {
          labels: ["January", "February", "March", "April", "May", "June", "July"],
          datasets: [{
            label: "My First dataset",
            fill: false,
            lineTension: 0.1,
            backgroundColor: "rgba(75,192,192,0.4)",
            borderColor: "rgba(75,192,192,1)",
            borderCapStyle: 'butt',
            borderDash: [],
            borderDashOffset: 0.0,
            borderJoinStyle: 'miter',
            pointBorderColor: "rgba(75,192,192,1)",
            pointBackgroundColor: "#fff",
            pointBorderWidth: 1,
            pointHoverRadius: 5,
            pointHoverBackgroundColor: "rgba(75,192,192,1)",
            pointHoverBorderColor: "rgba(220,220,220,1)",
            pointHoverBorderWidth: 2,
            pointRadius: 1,
            pointHitRadius: 10,
            data: [65, 59, 80, 81, 56, 55, 40],
            spanGaps: false,
          }]
        },
      }
    }
  },
  created () {
    this.getData()
  },
  mounted () {
    this.$nextTick(() => {
      const ctx = this.$el.querySelector('#canvas').getContext('2d')
      this.chart = new Chart(ctx, this.chartData)
    })
  }
}
</script>

<style>
.wrapper {
  width: 90vw;
  height: 80vh;
}
.button-area {
  display: flex;
  justify-content: space-between;
}
button {
  padding: 1em 2.617em;
  background-color: transparent;
  border: 1px solid hsla(200, 15%, 73%, 1);
  border-radius: 2px;
  color: hsla(200, 15%, 73%, 1);
  transition-duration: 0.35s;
  transition-property: background-color, border-color, color;
}
button:hover {
  background-color: hsla(200, 15%, 73%, 0.2);
  border-color: hsla(200, 15%, 73%, 0.7);
  color: hsla(200, 15%, 63%, 1);
}
</style>
