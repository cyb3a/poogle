<template>
  <div id="app">
    <el-container>
      <el-header id="header">
        <h1>POOGLE</h1>
      </el-header>
      <el-main>
        <el-row type="flex" justify="center">
          <el-form label-position="right" label-width="100px" :model="searchObject">
            <el-row>
              <custom-search-input v-model="searchObject.searchString"/>
            </el-row>

            <el-form-item label="Zeitspanne">
              <el-col>
                <custom-date-picker v-model="searchObject.searchDaterange" style="width: 100%;"/>
              </el-col>
            </el-form-item>
            <el-form-item label="Ort">
              <el-col>
                <custom-select v-model="searchObject.searchLocations" style="width: 100%;"/>
              </el-col>
            </el-form-item>

            <el-row>
              <el-button type="primary" @click="onSubmit" style="width: 100%;">Suchen</el-button>
            </el-row>
          </el-form>
        </el-row>
        <el-row>
          <div v-if="isSubmit">
            <el-row type="flex" justify="center">
              <el-col :span="12">
                <debug-result v-bind:result="searchObject"/>
              </el-col>
            </el-row>
          </div>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>


<script>
import CustomDatePicker from './components/CustomDatePicker.vue';
import CustomSelect from './components/CustomSelect.vue';
import CustomSearchInput from './components/CustomSearchInput.vue';
import DebugResult from './components/DebugResult.vue';

export default {
  name: 'app',
  components: {
    CustomDatePicker,
    CustomSelect,
    CustomSearchInput,
    DebugResult,
  },
  data() {
    return {
      searchObject: {
        searchString: null,
        searchDaterange: null,
        searchLocations: null,
      },
      isSubmit: false,
    };
  },
  methods: {
    onSubmit() {
      this.isSubmit = true;
    },
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
#header {
  background-color: #327cbb;
  color: #f2fdfe;
  text-align: center;
}
.el-row {
  margin-bottom: 20px;
}
.el-col {
  border-radius: 4px;
}
</style>
