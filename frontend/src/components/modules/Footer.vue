<template>
    <footer>
        <div class="footer-widget">
            <div class="footer-widget-name">
                <h2>Follow me</h2>
            </div>
            <ul class="sns-button">
                <li>
                    <a
                        href="https://twitter.com/otodo3"
                        class="flow-button twitter"
                        ><i class="fab fa-twitter"></i
                    ></a>
                </li>
                <li>
                    <a
                        href="https://www.youtube.com/channel/UCih6MT0eHkyT23VZVcdgBxA"
                        class="flow-button youtube"
                        ><i class="fab fa-youtube"></i
                    ></a>
                </li>
            </ul>
        </div>
        <!-- <div class="footer-widget">
            <h2>About me</h2>
            <p>job:Unemployed</p>
        </div> -->
        <div class="copyright-bar">
            <p>Copyright © 2021. All rights reserved.</p>
        </div>
    </footer>
</template>

<style scoped>
footer {
    font-family: 'ヒラギノ角ゴ Pro W3', 'Hiragino Kaku Gothic Pro', 'メイリオ',
        Meiryo, Osaka, 'MSPゴシック', 'MS PGothic', sans-serif;
    -webkit-text-size-adjust: none;
    padding-bottom: 50%;
    position: relative;
}

.copyright-bar p {
    position: absolute;
    text-align: center;
    font-size: 15px;
    color: black;
    width: 100%;
    padding-top: 3px;
    padding-bottom: 3px;
    bottom: 0;
    background-color: white;
}

.footer-widget {
    color: white;
    text-align: center;
    width: 50%;
    float: left;
}

.footer-widget > p {
    font-size: 20px;
}

.footer-widget h2 {
    display: inline-block;
    font-size: 20px;
    border-bottom: white solid;
    padding-bottom: 2px;
    margin-bottom: 2%;
}

.sns-button {
    position: relative;
    display: inline-block;
    list-style: none;
}

.sns-button li {
    float: left;
}

.flow-button {
    border-radius: 50%;
    position: relative;
    display: inline-block;
    width: 50px;
    height: 50px;
    font-size: 30px;
    text-decoration: none;
    transition: 0.5s;
    background-color: rgb(82, 82, 82);
    color: #fff;
}

.flow-button i {
    position: absolute;
    top: 50%;
    left: 50%;
    -ms-transform: translate(-50%, -50%);
    -webkit-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
}

.twitter:hover {
    background: linear-gradient(135deg, #13f1fc 0%, #0470dc 100%);
}

.youtube:hover {
    background: linear-gradient(135deg, #f5515f 0%, #c9293c 100%);
}
</style>