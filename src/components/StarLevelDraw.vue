<template>
    <div class="star-level-draw">
        <el-button @click="goBack" type="primary" icon="el-icon-back" class="back-button">返回</el-button>
        <h2>按星级抽取</h2>
        <el-button type="primary" @click="drawCharacters">抽取</el-button>
        <div v-for="rarity in [3, 4, 5]" :key="rarity" class="rarity-section">
            <h3>{{ `★${rarity + 1}` }}</h3>
            <CharacterGrid :characters="drawnCharacters[rarity]" @mark-not-owned="markNotOwned" />
        </div>
        <ExcludedCharacters :excluded-characters="excludedCharacters" @restore-character="restoreCharacter" />
    </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import CharacterGrid from './CharacterGrid.vue';
import ExcludedCharacters from './ExcludedCharacters.vue';
import { ElMessage } from 'element-plus';

export default {
    components: {
        CharacterGrid,
        ExcludedCharacters,
    },
    props: {
        characters: Array,
        excludedCharacters: Array,
    },
    emits: ['update:excludedCharacters'],
    setup(props, { emit }) {
        const router = useRouter();
        const drawnCharacters = ref({ 3: [], 4: [], 5: [] });

        const goBack = () => {
            router.push('/');
        };

        const availableCharacters = computed(() => {
            const excludedNames = props.excludedCharacters.map(char => char.name);
            return {
                3: props.characters.filter(char => char.rarity === 3 && !excludedNames.includes(char.name)),
                4: props.characters.filter(char => char.rarity === 4 && !excludedNames.includes(char.name)),
                5: props.characters.filter(char => char.rarity === 5 && !excludedNames.includes(char.name)),
            };
        });

        const drawCharacters = () => {
            [3, 4, 5].forEach(rarity => {
                if (availableCharacters.value[rarity].length < 12) {
                    ElMessage.warning(`★${rarity + 1}可用角色不足12个，请减少排除的角色`);
                    return;
                }
                drawnCharacters.value[rarity] = [];
                const tempAvailable = [...availableCharacters.value[rarity]];
                while (drawnCharacters.value[rarity].length < 12 && tempAvailable.length > 0) {
                    const randomIndex = Math.floor(Math.random() * tempAvailable.length);
                    const char = tempAvailable.splice(randomIndex, 1)[0];
                    drawnCharacters.value[rarity].push(char);
                }
            });
        };

        const markNotOwned = (name) => {
            const char = props.characters.find(c => c.name === name);
            if (char) {
                const newExcludedCharacters = [...props.excludedCharacters, char];
                emit('update:excludedCharacters', newExcludedCharacters);
                const rarity = char.rarity;
                const indexToReplace = drawnCharacters.value[rarity].findIndex(c => c.name === name);
                if (indexToReplace !== -1) {
                    const replacementChar = availableCharacters.value[rarity].find(c =>
                        !drawnCharacters.value[rarity].includes(c) &&
                        c.name !== name &&
                        !newExcludedCharacters.some(ec => ec.name === c.name)
                    );
                    if (replacementChar) {
                        drawnCharacters.value[rarity][indexToReplace] = replacementChar;
                    } else {
                        drawnCharacters.value[rarity].splice(indexToReplace, 1);
                        ElMessage.warning('没有更多符合条件的干员可供替换');
                    }
                }
            }
        };

        const restoreCharacter = (index) => {
            const newExcludedCharacters = [...props.excludedCharacters];
            newExcludedCharacters.splice(index, 1);
            emit('update:excludedCharacters', newExcludedCharacters);
        };

        return {
            drawnCharacters,
            drawCharacters,
            markNotOwned,
            restoreCharacter,
            goBack
        };
    },
};
</script>

<style scoped>
.star-level-draw {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
}

.back-button {
    position: absolute;
    top: 20px;
    right: 20px;
}

.rarity-section {
    margin-bottom: 30px;
}
</style>