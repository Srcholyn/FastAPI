<template>
    <div>
      <div class="tabs">
        <button
          v-for="sheet in sheets"
          :key="sheet"
          :class="{ active: sheet === selectedSheet }"
          @click="selectSheet(sheet)"
        >
          {{ sheet }}
        </button>
      </div>
      <div class="table-wrapper">
        <div class="table-container" ref="tableContainer">
          <table class="fixed-column-table">
            <thead>
              <tr>
                <th v-for="key in headers" :key="key" >{{ key }}</th>  
                <!-- Add more columns as needed -->
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in items" :key="item.id">
                <td class="fixed-column">{{ item }}</td>
                <!-- Add more columns as needed -->
              </tr>
            </tbody>
          </table>
          <div class="overflow-indicator" v-if="isOverflowing">...</div>
        </div>
        <div class="pagination">
          <button @click="fetchData(1)" :disabled="page === 1">First</button>
          <button @click="fetchData(page - 1)" :disabled="page === 1">Previous</button>
          <button v-for="pageNum in totalPages" :key="pageNum" @click="fetchData(pageNum)">
            {{ pageNum }}
          </button>
          <button @click="fetchData(page + 1)" :disabled="page === totalPages">Next</button>
          <button @click="fetchData(totalPages)" :disabled="page === totalPages">Last</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    props: ['id', 'label'],
    data() {
      return {
        sheets: [],
        selectedSheet: '',
        items: [],
        headers: [],
        page: 1,
        pageSize: 10,
        totalItems: 0,
        isOverflowing: false,
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
        const response = await axios.get(`http://127.0.0.1:8000/reconcile/${this.id}`);
        this.sheets = response.data;
        if (this.sheets.length > 0) {
          this.selectedSheet = this.sheets[0];
          this.fetchData();
        }
      },
      async fetchData(page = 1) {
        this.page = page;
        const response = await axios.get(`http://127.0.0.1:8000/reconcile/${this.id}/${this.selectedSheet}`, {
          params: { page: this.page, page_size: this.pageSize },
        });
        this.items = response.data.items;
        this.totalItems = response.data.total;
        
        this.checkOverflow();
        if (this.items.length > 0) {
            this.headers = Object.keys(this.items[0]);
        }
      },
      selectSheet(sheet) {
        this.selectedSheet = sheet;
        this.fetchData();
      },
      checkOverflow() {
        const tableContainer = this.$refs.tableContainer;
        this.isOverflowing = tableContainer.scrollWidth > tableContainer.clientWidth;
      },
    },
  };
  </script>
  
  <style>
  .tabs {
    display: flex;
    margin-bottom: 10px;
    margin-top: 20vh;
  }
  
  .tabs button {
    padding: 10px;
    margin-right: 5px;
    border: 1px solid #ccc;
    background-color: #f9f9f9;
    cursor: pointer;
  }
  
  .tabs button.active {
    background-color: #ddd;
  }
  
  .table-wrapper {
    position: relative;
  }
  
  .table-container {
    overflow-x: auto;
    position: relative;
  }
  
  .fixed-column-table {
    border-collapse: collapse;
    width: 100%;
  }
  
  .fixed-column-table th,
  .fixed-column-table td {
    padding: 10px;
    border: 1px solid #ccc;
    text-align: left;
  }
  
  .fixed-column-table thead {
    background-color: #f9f9f9;
  }
  
  .fixed-column {
    position: sticky;
    left: 0;
    background-color: #f9f9f9;
    z-index: 1;
    border-right: 1px solid #ccc;
  }
  
  .overflow-indicator {
    position: absolute;
    top: 0;
    right: 0;
    padding: 10px;
    background-color: rgba(255, 255, 255, 0.8);
    border-left: 1px solid #ccc;
    border-bottom: 1px solid #ccc;
    pointer-events: none;
  }
  
  .pagination {
    display: flex;
    justify-content: center;
    margin-top: 20px;
  }
  
  .pagination button {
    margin: 0 5px;
    padding: 5px 10px;
    border: 1px solid #ccc;
    background-color: #f9f9f9;
    cursor: pointer;
  }
  
  .pagination button:disabled {
    background-color: #eee;
    cursor: not-allowed;
  }
  </style>
  