<template lang="pug">
  div#app
    application-header
    div#page
      router-view.rv
    canvas#zodiac
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

#zodiac {
  position: absolute;
  top: 0;
  left: 0;
  height: 100vh;
  width: 100vw;
  z-index: -1;
}

#page {
  display: flex;
  flex-wrap: nowrap;
}

.rv {
  padding: 15px 0 0 15px;
  // background-color: transparent;
  min-height: 100vh;
  min-width: 100vw;
  overflow-y: scroll;
}

*::selection {
  background: rgba(254, 123, 211, 0.25);
}
</style>
