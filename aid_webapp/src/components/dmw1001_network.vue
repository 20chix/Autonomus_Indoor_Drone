<template>
  <div class="hello">





    <v-container>


    <h1>Autonomus indoor Drone (AID)</h1>
      <p>Author: <b>Hadi Elmekawi</b></p>
      <br>

     <v-data-table
    :headers="headers"
    :items="dwm1001Network"
    class="elevation-1"
    hide-actions

  >
    <template v-slot:items="props">
      <td>{{ props.item.topic }}</td>
        <td class="text-xs-right">{{ props.item.id }}</td>
      <td class="text-xs-right">{{ props.item.x }}</td>
      <td class="text-xs-right">{{ props.item.y }}</td>
      <td class="text-xs-right">{{ props.item.z }}</td>
      <td class="text-xs-right">{{ props.item.distanceFromTag }}</td>
    </template>
  </v-data-table>

      </v-container>



  </div>
</template>

<script>
/*eslint-disable*/
import ROS from "../ros_build/roslib.js";

var ros = new ROSLIB.Ros({ url: "ws://192.168.0.32:9090" });
var ros_rds = new ROSLIB.Ros({ url: "ws://172.31.20.142:9090" });



var listener_chatter = new ROSLIB.Topic({
  ros: ros_rds,
  name: "/chatter",
  messageType: "std_msgs/String"
});

var listener_anchor0 = new ROSLIB.Topic({
  ros: ros,
  name: "/dwm1001/anchor0",
  messageType: "localizer_dwm1001/Anchor"
});


var listener_anchor1 = new ROSLIB.Topic({
  ros: ros,
  name: "/dwm1001/anchor1",
  messageType: "localizer_dwm1001/Anchor"
});


var listener_anchor2 = new ROSLIB.Topic({
  ros: ros,
  name: "/dwm1001/anchor2",
  messageType: "localizer_dwm1001/Anchor"
});


var listener_anchor3 = new ROSLIB.Topic({
  ros: ros,
  name: "/dwm1001/anchor3",
  messageType: "localizer_dwm1001/Anchor"
});



var listener_tag = new ROSLIB.Topic({
  ros: ros,
  name: "/dwm1001/tag",
  messageType: "localizer_dwm1001/Tag"
});



export default {
  name: "dwm1001_network",
  data() {
    return {
        listener_data: "",
        listener_chatter: "",
        listener_anchor0:"",
        listener_anchor0_data : "",
        listener_anchor1 : "",
        listener_anchor1_data : "",
        listener_anchor2 : "",
        listener_anchor2_data : "",
        listener_anchor3 : "",
        listener_anchor3_data : "",
        listener_tag : "",
        listener_tag_data : "",
        listener_ardrone_camera : "",
        listener_ardrone_camera_data : "",
        headers: [
          {
            text: 'Topics',
            align: 'left',
            sortable: false,
            value: 'name'
          },
            { text: 'Anchor id'         , value: 'id' },
            { text: 'X Coordinate'      , value: 'x' },
            { text: 'Y Coordinate'      , value: 'y' },
            { text: 'Z Coordinate'      , value: 'z' },
            { text: 'Distance from Tag' , value: 'distanceFromTag' },

        ],
        dwm1001Network: [
          {
              topic:'',
              id: '',
              x: 0,
              y: 0,
              z: 0,
              distanceFromTag: 0

          },

            {
              topic:'',
              id: '',
              x: 0,
              y: 0,
              z: 0,
              distanceFromTag: 0

          },

            {
              topic:'',
              id: '',
              x: 0,
              y: 0,
              z: 0,
              distanceFromTag: 0

          },

            {
              topic:'',
              id: '',
              x: 0,
              y: 0,
              z: 0,
              distanceFromTag: 0

          },
            {
              topic:'',
              id: 'NA',
              x: 0,
              y: 0,
              z: 0,
              distanceFromTag: 'NA'

          }
        ]



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

      listener_chatter.subscribe(function(message) {
        console.log(
         "Received message on " + listener_chatter.name + ": " + message
        );
        self.listener_data = message;

      });

      listener_anchor0.subscribe(function(message) {
        // console.log(
        //  "Received message on " + listener_anchor0.name + ": " + message.id
        // );
        self.listener_anchor0_data = message;
        self.dwm1001Network[0].id = self.listener_anchor0_data.id;
          self.dwm1001Network[0].x = self.listener_anchor0_data.x;
          self.dwm1001Network[0].y = self.listener_anchor0_data.y;
          self.dwm1001Network[0].z = self.listener_anchor0_data.z;
          self.dwm1001Network[0].distanceFromTag = self.listener_anchor0_data.distanceFromTag;
          self.dwm1001Network[0].topic = listener_anchor0.name;
      });

      listener_anchor1.subscribe(function(message) {
        // console.log(
        //  "Received message on " + listener_anchor1.name + ": " + message.id
        // );
        self.listener_anchor1_data = message;
        self.dwm1001Network[1].id = self.listener_anchor1_data.id;
          self.dwm1001Network[1].x = self.listener_anchor1_data.x;
          self.dwm1001Network[1].y = self.listener_anchor1_data.y;
          self.dwm1001Network[1].z = self.listener_anchor1_data.z;
          self.dwm1001Network[1].distanceFromTag = self.listener_anchor1_data.distanceFromTag;
          self.dwm1001Network[1].topic = listener_anchor1.name;
      });


      listener_anchor2.subscribe(function(message) {
        // console.log(
        //  "Received message on " + listener_anchor2.name + ": " + message.id
        // );
        self.listener_anchor2_data = message;
        self.dwm1001Network[2].id = self.listener_anchor2_data.id;
          self.dwm1001Network[2].x = self.listener_anchor2_data.x;
          self.dwm1001Network[2].y = self.listener_anchor2_data.y;
          self.dwm1001Network[2].z = self.listener_anchor2_data.z;
          self.dwm1001Network[2].distanceFromTag = self.listener_anchor2_data.distanceFromTag;
          self.dwm1001Network[2].topic = listener_anchor2.name;
      });

      listener_anchor3.subscribe(function(message) {
        // console.log(
        //  "Received message on " + listener_anchor3.name + ": " + message.id
        // );
        self.listener_anchor3_data = message;
        self.dwm1001Network[3].id = self.listener_anchor3_data.id;
          self.dwm1001Network[3].x = self.listener_anchor3_data.x;
          self.dwm1001Network[3].y = self.listener_anchor3_data.y;
          self.dwm1001Network[3].z = self.listener_anchor3_data.z;
          self.dwm1001Network[3].distanceFromTag = self.listener_anchor3_data.distanceFromTag;
          self.dwm1001Network[3].topic = listener_anchor3.name;
      });

      listener_tag.subscribe(function(message) {
        // console.log(
        //  "Received message on " + listener_tag.name + ": " + message.x
        // );
        self.listener_tag_data = message;
          self.dwm1001Network[4].x = self.listener_tag_data.x;
          self.dwm1001Network[4].y = self.listener_tag_data.y;
          self.dwm1001Network[4].z = self.listener_tag_data.z;
          self.dwm1001Network[4].topic = listener_tag.name;
      });


      listener_ardrone_camera.subscribe(function(message) {
        console.log(
         "Received message on " + listener_ardrone_camera.name + ": " + message
        );
        self.listener_ardrone_camera = message;
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
  }
};
</script>

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
