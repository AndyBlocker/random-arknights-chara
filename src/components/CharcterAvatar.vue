<script setup>
import { getImagePath } from "@/utils/wiki";
import { computed } from "vue";

const props = defineProps({
  profession: String,
  rarity: Number,
  name: String,
  elite: Number,
  size: {
    type: String,
    validator(value) {
      return ['sm', 'xs'].includes(value);
    },
    required: false
  },
  name: String,
});

</script>

<template>
  <div class="avatar-container" :class="size">
    <img v-if="elite === 2" class="avatar" :src="getImagePath(`头像_${name}_${elite}.png`)" />
    <img v-else class="avatar" :src="getImagePath(`头像_${name}.png`)" />
    <div class="rarity">
    <img :src="getImagePath(`稀有度_黄_${rarity}.png`)" />
    </div>
    <div class="profession">
    <img :src="getImagePath(`图标_职业_${profession}.png`)" />
    </div>
  </div>
</template>

<style scoped>
.avatar-container {
  position: relative;
  width: 100px;
  height: 100px;
}
.avatar-container.sm {
  width: 80px;
  height: 80px;
}
.avatar-container.xs {
  width: 50px;
  height: 50px;
}
.avatar {
  width: 100px;
}
.sm .avatar {
  width: 80px;
}
.xs .avatar {
  width: 50px;
}
.rarity {
  position: absolute;
  bottom: 0px;
  right: 0px;
}
.rarity > img {
  height: 18px;
}
.sm .rarity > img {
  height: 14px;
}
.xs .rarity > img {
  height: 9px;
}
.profession {
  position: absolute;
  top: 0px;
}
.profession > img {
  height: 25px;
}
.xs .profession > img {
  height: 12px;
}
</style>
