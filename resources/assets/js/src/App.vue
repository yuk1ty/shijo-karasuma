<template lang="pug">
  div#app
    application-header
    div#page
      router-view.rv
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
html, body {
  height: 100vh;
  width: 100vw;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#page {
  display: flex;
  flex-wrap: nowrap;
}

.rv {
  padding: 15px 0 0 15px;
  background-color: rgb(244, 244, 244);
  min-height: 100vh;
  min-width: 100vw;
  overflow-y: scroll;
}

</style>
