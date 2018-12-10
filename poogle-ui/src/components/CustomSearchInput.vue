<template>
  <el-input
    placeholder="Sucheingabe"
    type="text"
    suffix-icon="el-icon-search"
    @input="updateString"
  />
</template>
<script>
export default {
  name: 'CustomSearchInput',
  props: ['value'],
  methods: {
    updateString(event) {
      this.$emit('input', event);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
