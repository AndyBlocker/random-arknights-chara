<template>
    <div class="character-grid" :style="gridStyle">
        <div class="character-cards" v-for="char in characters" :key="char.name" :style="cardStyle">
            <CharacterHalfPic :profession="char.职业" :rarity="char.rarity" :elite="char.elite" :logo="char.标志" :zh="char.name"/>
            <div class="overlay">
                <el-button class="not-owned-button" type="danger" icon="Close" @click="markNotOwned(char.name)"
                    :style="buttonStyle">
                    未拥有
                </el-button>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue';
import CharacterHalfPic from './CharacterHalfPic.vue';
export default {
    props: {
        characters: Array,
    },
    components: {
        CharacterHalfPic
    },
    emits: ['mark-not-owned'],
    setup(props, { emit }) {
        const gridStyle = ref("");
        const cardStyle = ref("");
        const imageStyle = ref("");
        const buttonStyle = ref("");

        const updateGridLayout = () => {
            const containerWidth = window.innerWidth;
            const maxColumns = 12;
            const gap = 12;
            const maxImageWidth = 180;
            const minImageWidth = 50;

            const availableWidth = containerWidth - gap * (maxColumns - 1);
            let columns = Math.floor(availableWidth / maxImageWidth);

            if (columns >= 6) columns = 6;
            else if (columns >= 4 && columns < 6) columns = 4;
            else if (columns < 4) columns = 4;

            const imageWidth = Math.min(
                maxImageWidth,
                (availableWidth - gap * (columns - 1)) / columns
            );
            const adjustedImageWidth = Math.max(minImageWidth, imageWidth);

            gridStyle.value = `
          display: grid;
          grid-template-columns: repeat(${columns}, ${adjustedImageWidth}px);
          gap: ${gap}px;
          justify-content: center;
        `;
            cardStyle.value = `
          width: ${adjustedImageWidth}px;
          height: auto;
          text-align: center;
        `;
            imageStyle.value = `
          max-width: 100%;
          height: auto;
          object-fit: contain;
        `;
            buttonStyle.value = `
          font-size: ${Math.max(8, adjustedImageWidth * 0.1)}px;
          padding: ${Math.max(2, adjustedImageWidth * 0.05)}px ${Math.max(4, adjustedImageWidth * 0.1)}px;
          border-radius: ${Math.max(2, adjustedImageWidth * 0.02)}px;
        `;
        };

        const markNotOwned = (name) => {
            emit("mark-not-owned", name);
        };

        onMounted(() => {
            updateGridLayout();
            window.addEventListener("resize", updateGridLayout);
        });

        onUnmounted(() => {
            window.removeEventListener("resize", updateGridLayout);
        });

        return {
            gridStyle,
            cardStyle,
            imageStyle,
            buttonStyle,
            markNotOwned,
        };
    },
};
</script>

<style scoped>
.character-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
    grid-template-rows: repeat(2, minmax(120px, auto));
    gap: 16px;
    justify-content: center;
    margin: 24px auto;
}

.character-cards {
    position: relative;
    text-align: center;
}

.character-image {
    max-width: 100%;
    height: auto;
    object-fit: contain;
}

.overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    background: rgba(0, 0, 0, 0.5);
    transition: opacity 0.3s ease;
}

.character-cards:hover .overlay {
    opacity: 1;
}

.not-owned-button {
    background-color: #f44336;
    color: white;
    border: none;
    cursor: pointer;
}

.character-name {
    margin-top: 8px;
    font-size: 14px;
    text-align: center;
    color: #333;
    font-weight: bold;
}
</style>