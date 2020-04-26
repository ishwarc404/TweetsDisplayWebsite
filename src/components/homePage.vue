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
            <div id="cardText">
              " Bitcoin should again outshine most crypto assets in 2020 as the unique and
              appreciating digital version of gold, the report continues. Bitcoin is winning the adoption race,
              notably as a store of value in an environment that favors independent quasi-currencies. "
            </div>
            <div class="d-flex" style="padding-left:30px; font-size:30px;">
              <div style="padding-top:8%;">
                <p>
                  Weight
                  0.232
                </p>
              </div>
              <div>
                <v-icon large color="green" style="font-size:90px;">mdi-arrow-up-thick</v-icon>
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
export default {};
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
