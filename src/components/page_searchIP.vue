<!-- src/components/FirstPage.vue -->
<template>
    <div class="container">
  <div class="row">
    <div class="col-12">
      <div id="app" style="width: 75%;">
        <div  v-if="hasScroll">Scroll on the table</div>
        <div  v-else>Resize your window until a scrollbar appears</div>
        <div class="table-holder" @wheel.prevent="wheelHorizontal($event)">
          <div class="info" v-if="hasScroll" @touchmove.prevent="scrollHorizontal($event)" :class="{'show' : showInfo}">Scroll for more &rarr;</div>
          <div class="table-responsive" ref="table" @scroll.prevent="scrollHorizontal($event)">
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">Heading</th>
                  <th scope="col">Heading</th>
                  <th scope="col">Heading</th>
                  <th scope="col">Heading</th>
                  <th scope="col">Heading</th>
                  <th scope="col">Heading</th>
                  <th scope="col">Heading</th>
                  <th scope="col">Heading</th>
                  <th scope="col">Heading</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">1</th>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                </tr>
                <tr>
                  <th scope="row">2</th>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                </tr>
                <tr>
                  <th scope="row">3</th>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                  <td>Cell</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>
  </div>
</div>
  </template>
  
  <script>
  /* eslint-disable */
export default {
  name: 'page_searchIP',
  data() {
    return {
    showInfo: true,
    hasScroll: true
  };
},
  methods: {
    wheelHorizontal: function(e) {
      if (e.deltaY < 0) {
        this.$refs.table.scrollLeft = this.$refs.table.scrollLeft - 50
      } else {
        this.$refs.table.scrollLeft = this.$refs.table.scrollLeft + 50
      }
    },
    scrollHorizontal: function(e) {
    	if (this.$refs.table.scrollLeft > 0) {
        this.showInfo = false;
      }
      if (this.$refs.table.scrollLeft == 0) {
        this.showInfo = true;
      }
    }
  },
  mounted: function() {
    let app = this;
  	let table = this.$refs.table;
    function verifyScroll() {
    	if (table.scrollWidth-60 > table.clientWidth) {
      	app.hasScroll = true;
      } else {
      	app.hasScroll = false;
      }
    }
    verifyScroll();
    window.addEventListener('resize', verifyScroll);
  }
}
  </script>
  
  <style scoped>
  h1 {
    color: #42b983;
  }

  .container {
  max-width: 768px;
}

.table-holder, .table-responsive {
  position: relative;
}

.table-responsive::-webkit-scrollbar {
  height: 10px;
}

.table-responsive::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px #333333;
}

.table-responsive::-webkit-scrollbar-thumb {
  background: #333333;
  outline: 1px solid #333333;
}

.info {
  position: absolute;
  width: 200px;
  height: 100%;
  background: linear-gradient(to right, transparent, #ffffff);
  top: 0;
  right: 0;
  padding: 20px;
  text-align: right;
  font-weight: bold;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  transition: opacity 300ms ease-in-out, visibility 300ms ease-in-out;
  opacity: 0;
  visibility: hidden;
  z-index: 1;
  pointer-events: none;
}

.show {
  opacity: 1;
  visibility: visible;
}

tr th:first-child, tr td:first-child {
  position: sticky;
  min-width: 50px;
  left: 0;
  background: white;
}
  </style>
  