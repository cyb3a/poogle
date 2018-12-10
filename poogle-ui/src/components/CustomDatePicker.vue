<template>
  <el-date-picker
    v-model="selected"
    type="daterange"
    start-placeholder="Start Datum"
    end-placeholder="End Datum"
    @input="updateDaterange"
  ></el-date-picker>
</template>

<script>
export default {
  name: 'CustomDatePicker',
  props: ['value'],
  data() {
    return {
      selected: '',
    };
  },
  methods: {
    updateDaterange(event) {
      this.$emit('input', event);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
