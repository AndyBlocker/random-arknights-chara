<template>
    <div class="mixed-draw">
        <el-button @click="goBack" type="primary" icon="el-icon-back" class="back-button">返回</el-button>
        <h2>自选星级抽12个</h2>
        <el-checkbox-group v-model="selectedRarities">
            <el-checkbox v-for="rarity in rarities" :key="rarity" :label="rarity">
                {{ `★${rarity + 1}` }}
            </el-checkbox>
        </el-checkbox-group>
        <el-button type="primary" @click="drawCharacters">抽取</el-button>
        <CharacterGrid v-if="drawnCharacters.length > 0" :characters="drawnCharacters" @mark-not-owned="markNotOwned" />
        <ExcludedCharacters :excluded-characters="excludedCharacters" @restore-character="restoreCharacter" />
    </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { ElMessage } from 'element-plus';
import CharacterGrid from './CharacterGrid.vue';
import ExcludedCharacters from './ExcludedCharacters.vue';

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
        const rarities = [0, 1, 2, 3, 4, 5];
        const selectedRarities = ref([5]);
        const drawnCharacters = ref([]);

        const goBack = () => {
            router.push('/');
        };

        const availableCharacters = computed(() => {
            const excludedNames = props.excludedCharacters.map(char => char.name);
            return props.characters.filter(char =>
                selectedRarities.value.includes(char.rarity) && !excludedNames.includes(char.name)
            );
        });

        const drawCharacters = () => {
            if (availableCharacters.value.length < 12) {
                ElMessage.warning('可用角色不足12个，请选择更多星级或减少排除的角色');
                return;
            }
            drawnCharacters.value = [];
            const tempAvailable = [...availableCharacters.value];
            while (drawnCharacters.value.length < 12 && tempAvailable.length > 0) {
                const randomIndex = Math.floor(Math.random() * tempAvailable.length);
                const char = tempAvailable.splice(randomIndex, 1)[0];
                drawnCharacters.value.push(char);
            }
        };

        const markNotOwned = (name) => {
            const char = props.characters.find(c => c.name === name);
            if (char) {
                const newExcludedCharacters = [...props.excludedCharacters, char];
                emit('update:excludedCharacters', newExcludedCharacters);
                const indexToReplace = drawnCharacters.value.findIndex(c => c.name === name);
                if (indexToReplace !== -1) {
                    const replacementCandidates = availableCharacters.value.filter(c =>
                        !drawnCharacters.value.includes(c) &&
                        c.name !== name &&
                        !newExcludedCharacters.some(ec => ec.name === c.name)
                    );

                    if (replacementCandidates.length > 0) {
                        const randomIndex = Math.floor(Math.random() * replacementCandidates.length);
                        const replacementChar = replacementCandidates[randomIndex];
                        drawnCharacters.value[indexToReplace] = replacementChar;
                    } else {
                        drawnCharacters.value.splice(indexToReplace, 1);
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
            rarities,
            selectedRarities,
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
.mixed-draw {
    display: flex;
    flex-direction: column;
    align-items: center;
    /* padding: 20px; */
}

.back-button {
    position: absolute;
    top: 20px;
    right: 20px;
}
</style>