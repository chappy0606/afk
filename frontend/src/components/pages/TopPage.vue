<template>
<div class="top-page">

    <h1 class="logo">
		<a href="#"><img src="@/assets/logo.png" alt="AFK"/></a>
    </h1>

    <nav class="menubar">
		<ul>
			<li><router-link to="/pve_comp">pve_comp</router-link></li>
			<li><a href="#">transelate</a></li>
			<li><a href="#">mythic manage</a></li>
		</ul>
    </nav>

    <div class="iframe-wrraper">
		<iframe
        width="800"
        height="450"
        src="https://www.youtube.com/embed/?list=UUih6MT0eHkyT23VZVcdgBxA"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
		</iframe>
    </div>

</div>
</template>

<style>
@keyframes opa1 {
	0% {pacity: 0;}
	100% {opacity: 1;}
}

a {
	transition: 0.5s;
}

header {
	font-size: 20px;
	width: 100%;
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

.iframe-wrraper {
	position: relative;
	width: 100%;
	padding-bottom: 56.25%;
}

.iframe-wrraper iframe {
	position: absolute;
	display: block;
	padding-bottom: 10%;
	width: 100%;
	height: 100%;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	max-width: 800px;
	max-height: 450px;
}
</style>