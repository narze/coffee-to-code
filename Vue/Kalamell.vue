<template>
    <button @click="convertCoffeeToCode">{{ text }}</button>
  </template>
  
  <script>
  export default {
    name: "convertcoffeetocode",
    data: () => ({
      text: "coffee",
    }),
    methods: {
      convertCoffeeToCode() {
        this.text = this.text.replace("coffee", "code");
      },
    },
  };
  </script>
  