<template>
  <div>
    <h1>{{ msg }}</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="image" />
      <input type="submit" value="Predict" />
    </form>
  </div>
</template>

<script>
/* eslint-disable */
import axios from "axios";
export default {
  name: "Predict",
  data() {
    return {
      msg: "Predict",
    };
  },
  methods: {
    getMessage() {
      const path = "http://localhost:5000/predict";
      axios
        .get(path)
        .then((res) => {
          this.msg = res.data.title;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

<style></style>
