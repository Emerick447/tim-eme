const dvd = document.getElementById("dvd");

// Position initiale aléatoire
let x = Math.random() * (window.innerWidth - dvd.offsetWidth);
let y = Math.random() * (window.innerHeight - dvd.offsetHeight);

// Vitesse réduite pour un mouvement plus lent
let speedX = 2;  // Au lieu de 6
let speedY = 2;  // Au lieu de 6

function randomColor() {
    return Math.floor(Math.random() * 360);
}

function animate() {
    x += speedX;
    y += speedY;

    // Rebond sur les bords gauche/droite
    if (x + dvd.offsetWidth >= window.innerWidth || x <= 0) {
        speedX = -speedX;
        dvd.style.filter = `hue-rotate(${randomColor()}deg)`;
    }

    // Rebond sur les bords haut/bas
    if (y + dvd.offsetHeight >= window.innerHeight || y <= 0) {
        speedY = -speedY;
        dvd.style.filter = `hue-rotate(${randomColor()}deg)`;
    }

    dvd.style.left = x + "px";
    dvd.style.top = y + "px";

    requestAnimationFrame(animate);
}

// Lance une seule fois l'animation
animate();