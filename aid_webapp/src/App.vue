<template>
  <v-app>


    <v-content>
      <dwm1001 />
    </v-content>



      <v-footer class="pa-3">
    <v-spacer></v-spacer>
    <div>Hadi Elmekawi w1530819 &copy; {{ new Date().getFullYear() }} </div>
  </v-footer>



  </v-app>
</template>

<script>
import dwm1001 from './components/dmw1001_network'

export default {
  name: 'App',
  components: {
      dwm1001
  }
}
</script>
