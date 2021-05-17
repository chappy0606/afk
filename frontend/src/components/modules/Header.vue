<template>
    <header>
        <div id="site-header">
            <input @click="getIp" type="button" value="IPを取得">
        </div>
            <nav class="header-menu">
                <ul>
                    <form name="logout" method="POST" action="#">
                        <li><a href="javascript:logout.submit()">ログアウト</a></li>
                    </form>
                    <li><a href=#>ログイン</a></li>
                    <li><a href=#>ユーザー登録</a></li>
                </ul>
            </nav>
        </header>
</template>

<script>

export default {
    name: 'site-header',
      methods: {
      getIp() {
        this.axios.get('http://localhost:8000/api/v1/chapter_stage/')
    .then(response=>{
      console.log("status:",response.status)
      console.log("axiosGetData:",response.data)
    })
    .catch(err=>{
      console.log("axiosGetErr",err)
    })
      }
    }
}

</script>

<style>
header {
	font-size: 20px;
	width: 100%;
}
</style>