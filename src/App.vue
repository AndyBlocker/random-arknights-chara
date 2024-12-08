<template>
  <div class="app-container">
    <router-view :characters="characters" :excludedCharacters="excludedCharacters"
      @update:excludedCharacters="updateExcludedCharacters"></router-view>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import Cookies from 'js-cookie';
import allCharacters from "@/assets/operator_data.json";

export default {
  name: 'App',
  setup() {
    const characters = ref([]);
    const excludedCharacters = ref([]);

    const initializeCharacters = () => {
      characters.value = allCharacters.map((item) => ({
        name: item.干员,
        ...item,
        rarity: Number(item.稀有度),
        elite: Number(item.稀有度) >= 3 ? 2 : 1,
      }));
    };

    const loadExcludedCharacters = () => {
      const cookieData = Cookies.get("excludedCharacters");
      if (cookieData) {
        const excludedNames = JSON.parse(cookieData);
        excludedCharacters.value = characters.value.filter((char) =>
          excludedNames.includes(char.name)
        );
      }
    };

    const updateExcludedCharacters = (newExcludedCharacters) => {
      excludedCharacters.value = newExcludedCharacters;
      const excludedNames = newExcludedCharacters.map(char => char.name);
      Cookies.set("excludedCharacters", JSON.stringify(excludedNames), { expires: 365 });
    };

    onMounted(() => {
      initializeCharacters();
      loadExcludedCharacters();
    });

    return {
      characters,
      excludedCharacters,
      updateExcludedCharacters,
    };
  },
};
</script>

<style>
.app-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}
</style>
