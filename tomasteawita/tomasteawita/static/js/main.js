const slidesContainer = document.getElementById("slides-container");
const slide = document.querySelector(".Tcard-carousel");
const prevButton = document.getElementById("slide-arrow-prev");
const nextButton = document.getElementById("slide-arrow-next");

nextButton.addEventListener("click", () => {
  const slideWidth = slide.clientWidth;
  slidesContainer.scrollLeft += slideWidth;
});

prevButton.addEventListener("click", () => {
  const slideWidth = slide.clientWidth;
  slidesContainer.scrollLeft -= slideWidth;
});

$(window).on('load', function () {
  setTimeout(function () {
$(".loader-page").css({visibility:"hidden",opacity:"0"})
}, 2000);});
