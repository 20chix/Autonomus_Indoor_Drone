<template>
<v-tabs
  fixed-tabs
>
  <v-tab ripple>
    Item 1
  </v-tab>
  <v-tab ripple>
    Item 2
  </v-tab>

  <v-tab-item>
      <HelloWorld/>
  </v-tab-item>


  <v-tab-item>
    <v-card flat>
      <v-card-text>Contents for Item 2 go here</v-card-text>
    </v-card>
  </v-tab-item>  

</v-tabs>


</template>




<script>
import HelloWorld from './HelloWorld'
  export default {
    name: "TabsManager",
    data () {
      return {
        active: null,
        text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
      }
    },
    methods: {
      next () {
        const active = parseInt(this.active)
        this.active = (active < 2 ? active + 1 : 0)
      }
    },
    components:{

        HelloWorld
    }
  }
</script>