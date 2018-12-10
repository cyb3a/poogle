<template>
  <el-select v-model="selected" multiple placeholder="Ort in Berlin" @change="updateLocations">
    <el-option
      v-for="location in options"
      :key="location.value"
      :label="location.label"
      :value="location.value"
    ></el-option>
  </el-select>
</template>

<script>
export default {
  name: 'CustomSelect',
  props: ['value'],
  data() {
    return {
      options: [
        {
          value: 'Mitte',
          label: 'Mitte',
        },
        {
          value: 'Friedrichshain-Kreuzberg',
          label: 'Friedrichshain-Kreuzberg',
        },
        {
          value: 'Pankow',
          label: 'Pankow',
        },
        {
          value: 'Charlottenburg-Wilmersdorf',
          label: 'Charlottenburg-Wilmersdorf',
        },
        {
          value: 'Spandau',
          label: 'Spandau',
        },
        {
          value: 'Steglitz-Zehlendorf',
          label: 'Steglitz-Zehlendorf',
        },
        {
          value: 'Tempelhof-Schöneberg',
          label: 'Tempelhof-Schöneberg',
        },
        {
          value: 'Neukölln',
          label: 'Neukölln',
        },
        {
          value: 'Treptow-Köpenick',
          label: 'Treptow-Köpenick',
        },
        {
          value: 'Marzahn-Hellersdorf',
          label: 'Marzahn-Hellersdorf',
        },
        {
          value: 'Lichtenberg',
          label: 'Lichtenberg',
        },
        {
          value: 'Reinickendorf',
          label: 'Reinickendorf',
        },
      ],
      selected: [],
    };
  },
  methods: {
    updateLocations(event) {
      this.$emit('input', event);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
