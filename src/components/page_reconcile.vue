<!-- src/components/page_reconcile.vue -->
<template>
    <div class="contentcontainer">
      <h2 class="topic">Reconcile {{ reconcile_name }}</h2>
      
      
       
      <ul class="contenttable">
          <aside class='sidebar'>
        <button
              v-for="sheet in sheets"
              :key="sheet"
              :class="{ active: sheet === selectedSheet }"
              @click="selectSheet(sheet)"
            >
              {{ sheet }}
            </button>
        </aside>
        <main class="main" ref="responsiveTable"
          @mousedown="handleMouseDown"
          @mousemove="handleMouseMove"
          @mouseup="handleMouseUp"
          @mouseleave="handleMouseLeave">
      <table class="gfg" >
        <thead>
          <tr class="headertable">
            <th v-for="key in headers" :key="key" >{{ key }}</th>  
          </tr>
        </thead>
        <tbody>
          <tr class="rowtable" v-for="item in items" :key="item.id">
            <td class="col col-1" v-for="header in headers" :key="header">{{  item[header] }}</td>
          </tr>
        </tbody>
        

      </table>
    </main>
    </ul>
    <div class="pagination">
      <button @click="goToPage(1)" :disabled="page === 1">&laquo;</button>
      <button @click="prevPage" :disabled="page === 1">&lsaquo;</button>
      
      <span class="current-page">Page {{ page }} of {{ totalPages }}</span>

      <button @click="nextPage" :disabled="page >= totalPages">&rsaquo;</button>
      <button @click="goToPage(totalPages)" :disabled="page >= totalPages">&raquo;</button>
    </div>
   
      <ul class="responsive-table">
        <li class="table-header" >
          <div class="col col-2" v-for="key in headers" :key="key">{{ key }}</div>
          <!-- <div class="col col-2">Time</div>
          <div class="col col-3">Result</div> -->
        </li>
        <li class="table-row" v-for="item in items" :key="item.id">
        <div v-for="header in headers" :key="header" class="col col-2" :data-label="header">
          {{ item[header] }}
        </div>
        </li>
        <button @click="prevPage" :disabled="page === 1">Previous</button>
        <button @click="nextPage" :disabled="!hasNextPage">Next</button>
      </ul>
   
    </div> 
  </template>

<script>
import axios from 'axios';
import '../assets/css/table.css';
/* eslint-disable */
export default {
  props: ['id', 'label'],
  data() {
    return {
      reconcile_name: '',
      sheets: [],
      selectedSheet: '',
      items: [],
      headers: [],
      page: 1,
      totalPages: 0,
      limit: 10,
      hasNextPage: false,
      isDragging: false,
      startX: 0,
      scrollLeft: 0,
    };
  },
  created() {
    this.fetchSheets();
  },
  watch: {
    id() {
      this.fetchSheets();
    }
  },
  methods: {
    async fetchSheets() {
      const reconcile_names = {
        "daily_report": "Daily Report",
        "iBGP": "Routing IBGP",
        "eBGP": "Routing EBGP",
        "status_L2": "Status L2",
        "vrrp": "VRRP",
        "acl": "ACL",
        "acl_bgp": "ACL BGP Service",
        "services_L2": "Service L2",
        "services_L3": "Service L3",
        "network-queue": "Network Queue",
        "infra": "Infra",
        }
        this.reconcile_name = reconcile_names[this.id] || 'reconcile_name not found';
        const response = await axios.get(`http://127.0.0.1:8000/reconcile/${this.id}`)
        this.sheets = response.data;
        if (this.sheets.length > 0) {
          this.selectedSheet = this.sheets[0];
          this.fetchItems();
        }
    },
    async fetchItems() {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/reconcile/${this.id}/${this.selectedSheet}`, {
          params: {
            page: this.page,
            size: this.limit,
          },
        });
        
        this.items = response.data.items;
        this.totalPages = response.data.pages;
        this.hasNextPage = response.data.total > this.page;
        if (this.items.length > 0) {
            this.headers = Object.keys(this.items[0]);
        }
        this.scrollToTop();
      }
      catch (error) {
        console.error('Error fetching items:', error);
      }
    },
    selectSheet(sheet) {
        this.selectedSheet = sheet;
        this.fetchItems();
    },
    scrollToTop() {
      this.$nextTick(() => {
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        });
      });
    },
    prevPage() {
      if (this.page > 1) {
        this.page--;
        this.fetchItems();
      }
    },
    nextPage() {
      if (this.page < this.totalPages) {
        this.page++;
        this.fetchItems();
      }
    },
    goToPage(pageNumber) {
      if (pageNumber >= 1 && pageNumber <= this.totalPages) {
        this.page = pageNumber;
        this.fetchItems();
      }
    },
    handleMouseDown(e) {
    this.isDragging = true;
    this.startX = e.pageX - this.$refs.responsiveTable.offsetLeft;
    this.scrollLeft = this.$refs.responsiveTable.scrollLeft + 2;
    },
    handleMouseMove(e) {
      if (!this.isDragging) return;
      e.preventDefault();
      const x = e.pageX - this.$refs.responsiveTable.offsetLeft;
      const walk = (x - this.startX) * 3; // Adjust the scroll speed
      this.$refs.responsiveTable.scrollLeft = this.scrollLeft - walk;
    },
    handleMouseUp() {
      this.isDragging = false;
    },
    handleMouseLeave() {
      this.isDragging = false;
    },
  },
};
</script>
<style>

</style>
