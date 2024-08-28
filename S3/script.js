let currentSlide = 0;
const slides = document.querySelectorAll(".slideshow img");
const totalSlides = slides.length;

function showSlide(index) {
  const slideshow = document.querySelector(".slideshow");
  slideshow.style.transform = `translateX(-${index * 300}px)`;
}

function nextSlide() {
  currentSlide = (currentSlide + 1) % totalSlides;
  showSlide(currentSlide);
}

setInterval(nextSlide, 3000);
