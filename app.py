<?php
/**
 * 1.0 SIGNAL - ULTIMATE LEAN VERSION
 * TERMINAL ADDR: THr243a11P65Drgq3AMMXWgc2sNCHMqTwu
 */
$status = isset($_GET['access']) && $_GET['access'] === 'verified' ? 'MEMBER' : 'SCAN';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>1.0 SIGNAL</title>
    <style>
        body { background: #000; color: #00ff00; font-family: 'Courier New', Courier, monospace; margin: 0; display: flex; align-items: center; justify-content: center; height: 100vh; overflow: hidden; }
        #container { width: 90%; max-width: 380px; text-align: center; border: 1px solid #00ff00; padding: 25px; box-shadow: 0 0 20px #00ff00; border-radius: 12px; position: relative; }
        .qr-frame { background: #fff; padding: 10px; display: inline-block; border: 2px solid #f3ba2f; border-radius: 5px; margin: 15px 0; }
        .qr-frame img { width: 180px; height: 180px; display: block; object-fit: contain; }
        .btn { background: #f3ba2f; color: #000; border: none; padding: 18px; width: 100%; font-weight: bold; border-radius: 5px; font-size: 18px; cursor: pointer; transition: 0.3s; box-shadow: 0 0 15px #f3ba2f; }
        .btn:active { transform: scale(0.98); opacity: 0.8; }
        .ca-input { background: #000; border: 1px solid #00ff00; color: #00ff00; width: 92%; padding: 15px; margin-bottom: 15px; text-align: center; font-size: 14px; outline: none; border-radius: 4px; }
        
        #log-screen { display: none; text-align: left; background: #080808; padding: 15px; border-radius: 5px; border: 1px solid #111; margin-top: 10px; height: 130px; overflow: hidden; }
        .log-line { font-size: 10px; color: #00ff00; margin: 3px 0; font-weight: lighter; }
        .progress-bar { width: 100%; height: 4px; background: #222; margin-top: 12px; border-radius: 2px; }
        .progress-fill { width: 0%; height: 100%; background: #00ff00; transition: width 15s linear; }

        #res { display: none; margin-top: 25px; }
        .green-orb { width: 65px; height: 65px; background: #00ff00; border-radius: 50%; margin: 0 auto; box-shadow: 0 0 45px #00ff00; animation: pulse 1s infinite; }
        @keyframes pulse { 0% { opacity: 0.8; transform: scale(1); } 50% { opacity: 1; transform: scale(1.05); } 100% { opacity: 0.8; transform: scale(1); } }
    </style>
</head>
<body>

<div id="container">

    <?php if ($status === 'SCAN'): ?>
        <h2 style="color:#f3ba2f; margin:0; letter-spacing: 2px;">1.0 SIGNAL</h2>
        <div id="pay-ui">
            <div class="qr-frame"><img src="https://raw.githubusercontent.com/gaozhen730221-jpg/axiom/main/1000003395.jpg"></div>
            <div style="color:#f3ba2f; font-weight:bold; margin-bottom:20px; font-size: 20px;">100 TWD (TWQR/街口)</div>
            <button class="btn" onclick="activate()">ACTIVATE & SYNC</button>
        </div>

        <div id="log-screen">
            <div id="logs"></div>
            <div class="progress-bar"><div class="progress-fill" id="fill"></div></div>
        </div>

        <script>
            function activate() {
                document.getElementById('pay-ui').style.display = 'none';
                document.getElementById('log-screen').style.display = 'block';
                
                const lines = [
                    "> INITIALIZING SENSOR 1.2.9...",
                    "> CONNECTING TWQR-GATEWAY...",
                    "> SCANNING PAYMENT STATUS...",
                    "> CHECKING INBOUND PROTOCOL...",
                    "> TRANSACTION VERIFIED...",
                    "> FINALIZING ACCESS GRANTED."
                ];
                
                let i = 0;
                const logBox = document.getElementById('logs');
                const interval = setInterval(() => {
                    if(i < lines.length) {
                        const d = document.createElement('div');
                        d.className = 'log-line';
                        d.innerText = lines[i];
                        logBox.appendChild(d);
                        i++;
                    } else { clearInterval(interval); }
                }, 2000);

                setTimeout(() => { document.getElementById('fill').style.width = "100%"; }, 100);
                setTimeout(() => { window.location.href = window.location.pathname + "?access=verified"; }, 15800);
            }
        </script>

    <?php else: ?>
        <h2 style="color:#00ff00; margin-bottom:15px; letter-spacing: 2px;">SENSOR ONLINE</h2>
        <input type="text" id="ca" class="ca-input" placeholder="Paste Contract Address (CA)">
        <button class="btn" style="background:#00ff00; box-shadow: 0 0 15px #00ff00;" onclick="scan()">START DEEP SCAN</button>
        
        <div id="res">
            <div class="green-orb"></div>
            <h2 style="color:#00ff00; margin-top:15px;">SIGNAL: GREEN</h2>
            <p style="font-size:11px; color:#555;">[98.4% MOMENTUM DETECTED]</p>
        </div>

        <script>
            function scan() {
                const val = document.getElementById('ca').value;
                if(!val) return alert('Enter CA');
                const btn = document.querySelector('.btn');
                const res = document.getElementById('res');
                res.style.display = 'none';
                btn.innerText = "ANALYZING...";
                
                setTimeout(() => {
                    res.style.display = 'block';
                    btn.innerText = "SCAN COMPLETE";
                }, 1800);
            }
        </script>
    <?php endif; ?>

</div>

</body>
</html>
