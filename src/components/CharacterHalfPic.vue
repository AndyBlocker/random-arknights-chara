<script setup>
import { computed } from 'vue';
import { charListData, getImagePath } from "@/utils/wiki"

const props = defineProps({
  profession: String,
  rarity: Number,
  elite: Number,
  logo: String,
  zh: {
    type: String,
    required: false
  },
  en: {
    type: String,
    required: false
  },
  scale: {
    type: Number,
    default: 1
  }
});

const containerStyle = computed(() => ({
  transform: `scale(${props.scale})`,
  transformOrigin: 'top left'
}));
</script>

<template>
  <div class="half-container" :style="containerStyle">
    <div class="uh">
      <img :src="getImagePath(`干员图鉴_uh_${rarity}.png`)" />
    </div>
    <div class="uhs">
      <img :src="charListData.uhs" width="70px" />
    </div>
    <div class="class_">
      <img :src="getImagePath(`图标_职业_${profession}.png`)" />
    </div>
    <div class="rarity">
      <img :src="getImagePath(`稀有度_黄_${rarity}.png`)" />
    </div>
    <div class="lh">
      <img :src="charListData.lh(rarity)" />
    </div>
    <div class="light">
      <img :src="getImagePath(`干员图鉴_稀有度_亮光_${rarity}.png`)" />
    </div>
    <div class="bg">
      <img :src="charListData.bg(rarity)" />
    </div>
    <div class="operator">
      <img :src="getImagePath(`半身像_${zh}_${elite}.png`)" />
    </div>
    <div class="patch" />
    <div class="logo">
      <img :src="getImagePath(`Logo_${logo}.png`)" />
    </div>
    <div class="zh">{{ zh }}</div>
  </div>
</template>

<style scoped>
.half-container {
  position: relative;
  width: 120px;
  height: 250px;
  background-color: transparent;
  display: inline-block;
  filter: drop-shadow(0 0 7px rgba(0, 0, 0, 0.7));
  transition: All 50ms ease-in-out;
  overflow: hidden;
}

.uh,
.uhs {
  position: absolute;
  top: 0;
}

.uh>img,
.uhs>img {
  width: 70px;
}

.class_ {
  position: absolute;
  left: 3px;
  top: 5px;
  z-index: 1;
}

.class_>img {
  width: 25px;
}

.rarity {
  position: absolute;
  left: 30px;
  top: 0;
  z-index: 2;
}

.rarity>img {
  height: 18px;
}

.lh {
  position: absolute;
  left: 0;
  bottom: 0;
  z-index: 2;
}

.lh>img {
  width: 120px;
}

.light {
  position: absolute;
  left: 3px;
  bottom: 25px;
  z-index: 1;
}

.light>img {
  width: 110px;
}

.bg {
  position: absolute;
  left: 3px;
  bottom: 7px;
  z-index: 0;
}

.bg>img {
  width: 110px;
}

.operator {
  position: absolute;
  bottom: 29px;
  z-index: 0;
  right: 7px;
}

.operator>img {
  transform: scale(0.61111);
  transform-origin: bottom right;
  max-width: initial;
  /*干掉移动前端 */
}

.patch {
  position: absolute;
  left: 3px;
  bottom: 7px;
  z-index: 1;
  width: 80px;
  height: 30px;
  background-color: #2c2c2c;
}

.logo {
  position: absolute;
  left: 2px;
  bottom: 13px;
  z-index: 3;
}

.logo>img {
  width: 50px;
}

.zh {
  position: absolute;
  left: 48px;
  bottom: 19px;
  z-index: 3;
  font-size: 14px;
  color: #fff;
  text-shadow: 0 0 10px #000;
  width: 70px;
  text-align: center;
}
</style>