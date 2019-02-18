// CommitChart.js
import { Line} from 'vue-chartjs'

export default {
  extends: Line,
  props: ['label', 'colour'],
  data () {
    return {
      active: null
    }
  },

  mounted () {
    // Overwriting base render method with actual data.
    this.renderChart({
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
      datasets: [
        {
          label: this.label,
          fill : false,
          backgroundColor: this.colour,
          data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11]
        }
      ]
    })
  }
}

