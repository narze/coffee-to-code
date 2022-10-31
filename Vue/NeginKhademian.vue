<template>
  <button @click="convertCoffeeToCode">{{ coffeeToCode }}</button>
</template>

<script>
export default {
  name: "convertCoffeeToCode",
  data: () => ({
    coffeeToCode: "i worship coffee",
  }),
  methods: {
    convertCoffeeToCode() {
      this.coffeeToCode = this.coffeeToCode.replace("coffee", "code");
    },
  },
};
</script>
