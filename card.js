(function() {
  // Return an event handler, flipping the card passed as an argument.
  function flipper(_card) {
    return function(event) {
      event.preventDefault();
      if (_card.classList.contains("flipped")) {
        _card.classList.remove("flipped");
      }
      else {
        _card.classList.add("flipped");
      }
    }
  }

  function setup() {
    // Get all the "cards" (really, sides of the cards)
    var card = document.querySelector('.card');
    var about = document.querySelector('#about');

    if (card) {
      card.addEventListener("click", flipper(card));
      about.addEventListener("click", flipper(card));
    }
  }

  setup();
})();
