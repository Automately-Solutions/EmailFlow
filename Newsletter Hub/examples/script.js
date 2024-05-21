// script.js
import { Application } from '@splinetool/runtime';

document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('canvas3d');
    const app = new Application(canvas);
    app.load('https://prod.spline.design/GLXPK8YSvoNy7ecA/scene.splinecode');
});

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('signup-form');
    const message = document.getElementById('signup-message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const email = document.getElementById('email').value;

        if (email) {
            try {
                const response = await fetch('http://127.0.0.1:5000/add_email', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ email: email }),
                });

                const result = await response.json();

                if (response.ok) {
                    message.textContent = result.message;
                    message.style.color = 'green';
                    form.reset();
                } else {
                    message.textContent = result.message;
                    message.style.color = 'red';
                }
            } catch (error) {
                message.textContent = 'An error occurred. Please try again.';
                message.style.color = 'red';
                console.error('Error:', error);  // Added for debugging
            }
        }
    });
});