<template>
  <el-card class="box-card">
    <div  slot="header">
      <span><strong>Suchobjekt</strong></span>
    </div>
    <pre>{{JSON.stringify(result, null, 2 )}}</pre>
  </el-card>
</template>

<script>
export default {
  name: 'DebugResult',
  props: [
    'result',
  ],
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
