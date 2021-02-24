<template>
  <div>
    <h1>{{ msg }}</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="image" @change="postImage"/>
      <input type="submit" value="Predict" />
    </form>
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
    };
  },
  methods: {
    getMessage() {
      const path = "http://localhost:5000/predict";
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
    postImage(event) {
      const path = "http://localhost:5000/predict";
      let form = new FormData();
      form.append('image', event.target.files[0] )
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
