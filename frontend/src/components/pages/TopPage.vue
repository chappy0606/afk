<template>
    <div class="top-page">
        <h1 class="logo">
            <a href="#"><img src="@/assets/logo.png" alt="AFK"/></a>
        </h1>
        <nav class="menubar">
            <ul>
                <li>
                    <router-link :to="{ name: 'PveComp' }"
                        >pve_comp</router-link
                    >
                </li>
                <li>
                    <router-link :to="{ name: 'RelicCalcuator' }"
                        >RelicCalcuator</router-link
                    >
                </li>
            </ul>
        </nav>
    </div>
</template>

<style scoped>

@keyframes opa1 {
    0% {
        pacity: 0;
    }
    100% {
        opacity: 1;
    }
}

a {
    transition: 0.5s;
}

.logo img {
    position: relative;
    width: 30%;
    left: 35%;
    margin-top: 13%;
}

.menubar {
    position: relative;
    width: 100%;
    text-align: center;
    margin-top: 15%;
    margin-bottom: 10%;
}

.menubar li {
    display: inline-block;
    margin: 0 1%;
    animation-name: opa1;
    animation-delay: 1s;
    animation-duration: 1s;
    animation-fill-mode: both;
}

.menubar li a {
    text-decoration: none;
    display: block;
    text-align: center;
    width: 150px;
    color: white;
    border-bottom: 2px solid transparent;
    padding-bottom: 7px;
}

.menubar li a:hover {
    border-bottom: 2px solid #fff;
    letter-spacing: 0.1em;
}
</style>
