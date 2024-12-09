<template>
    <div class="character-grid-container">
        <div class="character-grid" :style="gridStyle">
            <div v-for="char in characters" :key="char.name" class="character-cell">
                <div class="character-card" :style="cardStyle">
                    <CharacterHalfPic :profession="char.职业" :rarity="char.rarity" :elite="char.elite" :logo="char.标志"
                        :zh="char.name" :scale="cardScale" />
                    <div class="overlay" :style="overlayStyle" @click="markNotOwned(char.name)">
                        <el-button class="not-owned-button" type="danger" icon="Close" :style="buttonStyle">
                            未拥有
                        </el-button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, computed, onMounted, onUnmounted } from 'vue';
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
        const windowWidth = ref(window.innerWidth);

        const updateWindowWidth = () => {
            windowWidth.value = window.innerWidth;
        };

        onMounted(() => {
            window.addEventListener('resize', updateWindowWidth);
        });

        onUnmounted(() => {
            window.removeEventListener('resize', updateWindowWidth);
        });

        const columns = computed(() => {
            if (windowWidth.value >= 750) return 6;
            if (windowWidth.value >= 510) return 4;
            return 3;
        });

        const cardScale = computed(() => {
            const baseWidth = 120; // Original width of CharacterHalfPic
            const availableWidth = (windowWidth.value / columns.value) - 8; // Accounting for gap
            return Math.min(1, availableWidth / baseWidth);
        });

        const gridStyle = computed(() => {
            const gap = 4;
            return `
          display: grid;
          grid-template-columns: repeat(${columns.value}, 1fr);
          gap: ${gap}px;
          width: 100%;
          box-sizing: border-box;
        `;
        });

        const cardStyle = computed(() => {
            const width = 120 * cardScale.value;
            const height = 250 * cardScale.value;
            return `
          width: ${width}px;
          height: ${height}px;
        `;
        });

        const overlayStyle = computed(() => `
        width: 100%;
        height: 100%;
      `);

        const buttonStyle = computed(() => {
            const baseFontSize = windowWidth.value < 576 ? 10 : 12;
            return `
          font-size: ${baseFontSize}px;
          padding: ${baseFontSize / 2}px ${baseFontSize}px;
        `;
        });

        const markNotOwned = (name) => {
            emit("mark-not-owned", name);
        };

        return {
            gridStyle,
            cardStyle,
            cardScale,
            overlayStyle,
            buttonStyle,
            markNotOwned,
        };
    },
};
</script>

<style scoped>
.character-grid-container {
    display: flex;
    justify-content: center;
    width: 100%;
}

.character-grid {
    display: grid;
    margin: 0 auto;
    max-width: 1440px;
}

.character-cell {
    display: flex;
    justify-content: center;
    align-items: center;
}

.character-card {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
}

.overlay {
    position: absolute;
    top: 0;
    left: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(0, 0, 0, 0.5);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.character-card:hover .overlay,
.character-card:active .overlay {
    opacity: 1;
}

.not-owned-button {
    background-color: #f44336;
    color: white;
    border: none;
    cursor: pointer;
}

@media (hover: none) {
    .overlay {
        opacity: 1;
        background: rgba(0, 0, 0, 0.3);
    }

    .not-owned-button {
        opacity: 0.8;
    }
}
</style>