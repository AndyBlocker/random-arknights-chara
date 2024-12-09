<template>
    <div class="home">
        <h1>老缠杯🤓👆</h1>
        <div class="button-container">
            <el-button @click="$router.push('/mixed-draw')" type="primary">自选星级抽12个</el-button>
            <el-button @click="$router.push('/star-level-draw')" type="primary">456星各抽12个</el-button>
            <el-button @click="$router.push('/description-draw')" type="primary">随机描述抽取</el-button>
            <el-button type="primary">这里有个功能我还没做🤓👆</el-button>
        </div>
    </div>
</template>
<script>
export default {
    name: 'Home',
}
</script>
<style scoped>
.home {
    text-align: center;
}

.button-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    margin-top: 30px;
}

.button-container .el-button {
    width: 200px;
    margin: 0 auto;
} 

</style>