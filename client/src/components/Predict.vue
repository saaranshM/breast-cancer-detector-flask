<template>
  <div>
    <h1>{{ msg }}</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="image" @change="saveImage" />
      <!-- <input type="submit" value="Predict" /> -->
    </form>
    <v-btn v-if="image" @click="predict">Pre</v-btn>
    <v-img height="50" width="50" v-if="imageToShow" :src="imageToShow"></v-img>
    <h3>Prediction: {{ prediction }}</h3>
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
      imageToShow:null,
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
      var reader = new FileReader();

      reader.onload = e => {
        this.imageToShow = e.target.result
      }

      this.imageToShow = reader.readAsDataURL(event.target.files[0])
    },
    predict() {
      console.log("predict");
      const path = "http://localhost:5000/";
      let form = new FormData();
      form.append("image", this.image);
      axios
        .post(path, form)
        .then((res) => {
          console.log(res);
          if(res.data.prediction.indexOf(Math.round(...res.data.prediction))){
            this.prediction = "HAS CANCER!"
          } else {
            this.prediction = "NO CANCER!"
          }
          console.log("SUCCESS");
        })
        .catch((err) => {
          console.log(err);
          alert("Something went wrong")
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

<style></style>
