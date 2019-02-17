<template>
  <div class="hello">


    <!--<v-layout row wrap>-->



      <!--<v-flex xs12 sm4>-->
        <!--<CommitChart label="X coordinates" colour="red"/>-->


      <!--</v-flex>-->

      <!--<v-flex xs12 sm4>-->
        <!--<CommitChart label="Y coordinates" colour="green" />-->
      <!--</v-flex>-->
      <!--<v-flex xs12 sm4>-->
        <!--<CommitChart label="Z coordinates" colour="blue"/>-->
      <!--</v-flex>-->

      <!---->
    <!--</v-layout>-->


    <v-container>
<center>
    <img src="../assets/logo.png">

    <h1>{{this.listener_data}}</h1>

</center>
      </v-container>


  </div>
</template>

<script>
import ROS from "../ros_build/roslib.js";
import CommitChart from "./commitChart.js";

var ros = new ROSLIB.Ros({ url: "ws://localhost:9090" });

var listener = new ROSLIB.Topic({
  ros: ros,
  name: "/chatter",
  messageType: "std_msgs/String"
});

export default {
  name: "HelloWorld",
  data() {
    return {
      listener_data: "",
      listener: ""
    };
  },
  mounted() {
    this.init();
  },

  methods: {
    init() {
      ros.on("connection", function() {
        console.log("Connected to websocket server.");
      });

      ros.on("error", function(error) {
        console.log("Error connecting to websocket server: ", error);
      });

      ros.on("close", function() {
        console.log("Connection to websocket server closed.");
      });

      var self = this;

      listener.subscribe(function(message) {
        console.log(
          "Received message on " + listener.name + ": " + message.data
        );
        self.listener_data = message.data;
      });
    }
  },
  computed: {
    binding() {
      const binding = {};

      if (this.$vuetify.breakpoint.mdAndUp) binding.column = true;

      return binding;
    }
  },
  props: {
    msg: String
  },
  components: {
    CommitChart
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
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
</style>
