<template>
  <v-app>
    <homePage/>
  </v-app>
</template>

<script>

import homePage from "./components/homePage"

export default {
  name: 'App',
  components: {
   homePage
  },

  data: () => ({
    //
  }),
};
</script>

<style  scoped>

</style>
