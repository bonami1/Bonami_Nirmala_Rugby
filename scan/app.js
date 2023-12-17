import QrScanner from '/scan/qr-scanner.umd.min.js'; // if using plain es6 import
import QrScanner from 'qr-scanner'; // if installed via package and bundling with a module bundler like webpack or rollup

import('scan/qr-scanner.umd.min.js').then((module) => {
    const QrScanner = module.default;
    // do something with QrScanner
});

const startScanner = () => {
    const videoElem = document.querySelector("#scanner video");

    const qrScanner = new QrScanner(videoElem, (result) => {
        console.log('Contenu du QR Code :', result);
    });
    
    qrScanner.setCamera("environment");
    qrScanner.start();
}

document.querySelector("#start").addEventListener("click", () => {
    startScanner();
});
