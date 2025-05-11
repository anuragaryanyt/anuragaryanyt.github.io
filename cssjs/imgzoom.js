const images = document.querySelectorAll('.pic');

const overlay = document.createElement('div');
overlay.style.position = 'fixed';
overlay.style.top = 0;
overlay.style.left = 0;
overlay.style.width = '100%';
overlay.style.height = '100%';
overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
overlay.style.zIndex = 999;
overlay.style.display = 'none';
overlay.style.cursor = 'zoom-out';
overlay.style.transition = 'opacity 0.3s ease';
overlay.style.opacity = 0;

document.body.appendChild(overlay);

images.forEach(image => {
  image.addEventListener('click', function () {
    const isZoomed = image.classList.contains('zoomed');
    images.forEach(img => img.classList.remove('zoomed'));

    if (!isZoomed) {
      document.body.style.overflow = 'hidden'; // Lock scroll
      image.classList.add('zoomed');
      overlay.style.display = 'block';
      setTimeout(() => {
        overlay.style.opacity = 1;
      }, 10);
    } else {
      overlay.click();
    }
  });
});

overlay.addEventListener('click', function () {
  images.forEach(img => img.classList.remove('zoomed'));
  overlay.style.opacity = 0;
  document.body.style.overflow = ''; // Unlock scroll
  setTimeout(() => {
    overlay.style.display = 'none';
  }, 300);
});
