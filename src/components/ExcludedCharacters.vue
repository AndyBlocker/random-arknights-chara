<template>
    <div class="excluded-characters">
        <h2>未拥有的角色：</h2>
        <div class="small-grid" :style="gridStyle">
            <div v-for="(char, index) in excludedCharacters" :key="char.index" class="small-card" :style="cardStyle">
                <div class="small-card-container" :style="containerStyle">
                    <CharcterAvatar class="small-grid" :profession="char.职业" :rarity="char.rarity" :elite="char.elite"
                        :name="char.name" />
                    <div class="restore-overlay">
                        <el-button class="restore-button" type="success" icon="Check" @click="restoreCharacter(index)"
                            :style="buttonStyle">
                            恢复
                        </el-button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, onMounted, onUnmounted, watch } from 'vue';
import CharcterAvatar from './CharcterAvatar.vue';
export default {
    props: {
        excludedCharacters: {
            type: Array,
            default: () => [],
        },
    },
    components: {
        CharcterAvatar
    },
    emits: ["restore-character"],
    setup(props, { emit }) {
        const gridStyle = ref("");
        const cardStyle = ref("");
        const containerStyle = ref("");
        const buttonStyle = ref("");

        watch(() => props.excludedCharacters, (newValue) => {}, { deep: true, immediate: true });

        const updateGridLayout = () => {
            const containerWidth = window.innerWidth;
            const gap = 16;
            const maxCardWidth = 90;
            const minCardWidth = 30;

            const availableWidth = containerWidth - gap;
            const columns = Math.floor(availableWidth / maxCardWidth);
            const adjustedColumns = Math.max(1, columns);

            const cardWidth = Math.min(
                maxCardWidth,
                (availableWidth - gap * (adjustedColumns - 1)) / adjustedColumns
            );
            const adjustedCardWidth = Math.max(minCardWidth, cardWidth);

            gridStyle.value = `
          display: grid;
          grid-template-columns: repeat(${adjustedColumns}, ${adjustedCardWidth}px);
          gap: ${gap}px;
          justify-content: center;
        `;
            cardStyle.value = `
          width: ${adjustedCardWidth}px;
          height: auto;
          text-align: center;
        `;
            containerStyle.value = `
          width: ${adjustedCardWidth}px;
          height: ${adjustedCardWidth}px;
          position: relative;
        `;
            buttonStyle.value = `
          font-size: ${Math.max(8, adjustedCardWidth * 0.1)}px;
          padding: ${Math.max(2, adjustedCardWidth * 0.05)}px ${Math.max(4, adjustedCardWidth * 0.1)}px;
          border-radius: ${Math.max(2, adjustedCardWidth * 0.02)}px;
        `;
        };

        const restoreCharacter = (index) => {
            emit("restore-character", index);
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
            containerStyle,
            buttonStyle,
            restoreCharacter,
        };
    },
};
</script>

<style scoped>
.excluded-characters {
    padding: 20px;
    margin-top: 32px;
}

.small-grid {
    display: grid;
    justify-content: center;
    gap: 16px;
}

.small-card-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
}

.restore-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: none;
    align-items: center;
    justify-content: center;
    background: rgba(0, 0, 0, 0.6);
    transition: opacity 0.3s ease;
}

.small-card-container:hover .restore-overlay {
    display: flex;
}

.restore-button {
    background-color: #4caf50;
    color: white;
    border: none;
    cursor: pointer;
}
</style>