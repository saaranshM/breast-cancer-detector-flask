<template>
  <div>
    <h1>{{ msg }}</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="image" @change="saveImage"/>
      <!-- <input type="submit" value="Predict" /> -->

    </form>
    <button @click="predict">Pre</button>
    <h3>Prediction: {{prediction}}</h3>
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
      prediction: 0,
      image: null,
    };
  },
  methods: {
    getMessage() {
      const path = "http://localhost:5000/";
      axios
        .get(path)
        .then((res) => {
          this.msg = res.data.title;
          this.prediction = res.data.prediction;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    saveImage(event) {

      this.image = event.target.files[0];

    },
    predict() {
      console.log('predict');
      const path = "http://localhost:5000/";
      let form = new FormData();
      form.append('image', this.image )
      axios.post(path, form).then((res) => {
        console.log(res);
        this.prediction = res.data.prediction
        console.log("SUCCESS")
      }).catch((err) => {
        console.log(err)
      })
    }
  },
  created() {
    this.getMessage();
  },
};
</script>

<style></style>
