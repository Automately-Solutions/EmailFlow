// script.js
import { Application } from '@splinetool/runtime';

document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('canvas3d');
    const app = new Application(canvas);
    app.load('https://prod.spline.design/GLXPK8YSvoNy7ecA/scene.splinecode');
});
