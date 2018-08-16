<template>
<section class="container">
	<div>
		<h1>tweet steam screenshot</h1>
		<h2>Nuxt + Electron</h2>
    <div>
      <input type="text" @change="showPath" ref="folder" name="folder" />
    </div>
	</div>
</section>
</template>

<script>
export default {
    methods: {
        showPath(e) {
            console.log('test');
        }
    }
}
</script>

<style scoped>
.container {
	  min-height: 100vh;
	  display: flex;
	  justify-content: center;
	  align-items: center;
	  text-align: center;
}
.btn {
	  margin: 0 8px;
}
</style>
