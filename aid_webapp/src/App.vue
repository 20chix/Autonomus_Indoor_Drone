<template>
  <v-app>
    <!--<v-toolbar app>-->
      <!--<v-toolbar-title class="headline text-uppercase">-->
        <!--<span class="font-weight-light">AID</span>-->
        <!--<span> Autonomus indoor drone</span>-->
        <!---->
      <!--</v-toolbar-title>-->
      <!--<v-spacer></v-spacer>-->
      <!--<v-btn-->
        <!--flat-->
        <!--href="https://github.com/20chix/Autonomus_Indoor_Drone_DWM1001"-->
        <!--target="_blank"-->
      <!--&gt;-->
        <!--<span class="mr-2">GitHub</span>-->
      <!--</v-btn>-->
    <!--</v-toolbar>-->




    <v-content>
      <HelloWorld />
    </v-content>



  </v-app>
</template>

<script>
//import TabsManager from './components/TabsManager'
import HelloWorld from './components/HelloWorld'

export default {
  name: 'App',
  components: {
      HelloWorld
  },
  data () {
    return {
      //
    }
  }
}
</script>
