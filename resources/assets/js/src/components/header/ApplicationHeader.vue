<template lang="pug">
  header.application-header
    div.logo
      h1 Shijo
      h1 Karasuma
    div.nav
      div.links
        router-link(v-for="route in this.$router.options.routes" tag="li" :to="route.path")
          a {{ route.name }}
    div.current
      div.line
    div.pagename(v-model="currentRoute") {{ currentRoute.name }}
</template>

<script>
export default {
  name: 'app-header',
  computed: {
    currentRoute: function() {
      return this.$router.currentRoute
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Montserrat+Subrayada');

.application-header {
  height: 120px;
  align-content: flex-start;
  background-color: #fff;
  display: block;
  position: relative;
}

h1 {
  padding-top: 8px;
  padding-left: 13px;
  margin: 0;
  margin-bottom: -18px;
  font-family: 'Montserrat Subrayada';
  font-size: 20pt;
}

.logo {
  margin: 10px;
  background-color: rgb(99, 174, 215);
  width: 190px;
  height:70px;
  display: flex;
  flex-wrap: wrap;
  align-content: space-evenly;
  color: rgba(44, 47, 45, 30%);
  z-index: 3;
  position: absolute;
  top: 0;
  left: 0;
}

.nav {
  background-color: rgb(223, 223, 223);
  width: 100vw;
  height: 60px;
  line-height: 60px;
  position: absolute;
  top: 0;
  left: 0;
  padding-left: 250px;
  align-content: space-between;
  justify-content: center;
  white-space: nowrap;
}

.nav li {
  display: inline-block;
  width: 25%;
}

.current {
  position: absolute;
  top: 72px;
  width: 100vw;
  vertical-align: middle;
  text-align: center;
}

.line {
  position: absolute;
  top: 25px;
  height: 5px;
  width: 100vw;
  background-color: rgb(99, 174, 215);
  z-index: 0;
}
.pagename {
  position: absolute;
  top: 88px;
  /*text-align: center;*/
  /*vertical-align: middle;*/
  z-index: 5;
  padding-left: 10px;
  padding-right: 10px;
  height: 20px;
  background-color: #fff;
  display: flex;
  vertical-align: middle;
  align-items: center;
  align-content: center;
  align-self: center;
  flex-wrap: center;
}
</style>
