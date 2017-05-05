<template lang="pug">
  div#app
    application-header
    router-view
</template>

<script>
import ApplicationHeader from '@/components/header/ApplicationHeader'

export default {
  name: 'app',
  components: {
    'application-header': ApplicationHeader,
  }
}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
