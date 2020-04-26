<template>
  <div style="padding-top:12%;">
    <div class="d-flex justify-content-around">
      <div>
        <div class="d-flex" id="title">
          <img src="../assets/bitcoin.jpg" width="220" alt />
          <p>itcoin</p>
        </div>

        <div id="title2">
          <p>prediction</p>
        </div>
      </div>
      <div>
        <v-card class="mx-auto" width="500" max-height="400">
          <v-card-text>
            <div>
              <img src="../assets/twitter.png" width="80" alt />
            </div>
            <div id="cardText">" {{ this.tweet }} "</div>
            <div class="d-flex" style="padding-left:30px; font-size:30px;">
              <div style="padding-top:8%;">
                <p>
                  Weight
                  {{ this.score }}
                </p>
              </div>
              <div>
                <v-icon large :color="this.arrow_color" style="font-size:90px;"
                  >mdi-arrow-{{ this.arrow_direction }}-thick</v-icon
                >
              </div>
            </div>
          </v-card-text>
        </v-card>
      </div>
    </div>
    <br />
    <br />
    <br />
    <div class="d-flex justify-content-center">
      <v-btn large>GRAPHS</v-btn>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      tweet: null,
      score: null,
      arrow_direction: null,
      arrow_color: null,
    };
  },
  methods: {
    async getTweets() {
      let randomID = Math.floor(Math.random() * 1000) + 1;
      let data = await axios.get(`http://127.0.0.1:3000/data?id=${randomID}`);

      this.tweet = data.data[0].tweet;
      this.score = data.data[0].score;
      if (this.score < 0) {
        this.arrow_direction = "down";
        this.arrow_color = "red";
      } else {
        this.arrow_direction = "up";
        this.arrow_color = "green";
      }
      setTimeout(() => {
        this.getTweets();
      }, 1000);
    },
  },
  created() {
    this.getTweets();
  },
};
</script>

<style scoped>
#title2 {
  font-size: 100px;
  padding-left: 50px;
}
#title {
  font-size: 140px;
}
#cardText {
  font-size: 20px;
  padding-left: 20px;
  font-weight: bold;
}
</style>
