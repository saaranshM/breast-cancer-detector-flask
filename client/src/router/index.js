/* eslint-disable */
import Vue from "vue";
import VueRouter from "vue-router";
import Predict from "@/components/Predict.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Predict",
    component: Predict,
  },
  {
    path: "/predict",
    name: "Predict",
    component: Predict,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
