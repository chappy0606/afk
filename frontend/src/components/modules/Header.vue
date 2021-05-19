<template>
    <header>
        <nav class="header-menu">
            <ul>
                <form name="logout" method="POST" action="#">
                    <li><a href="javascript:logout.submit()">ログアウト</a></li>
                </form>
                <li><a href="#">ログイン</a></li>
                <li><a href="#">ユーザー登録</a></li>
            </ul>
        </nav>
    </header>
</template>

<script lang="ts"></script>

<style>
header {
    font-size: 20px;
    width: 100%;
}
</style>
