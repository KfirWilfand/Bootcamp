class CardSet {
  constructor(name, dirPath, cards) {
    this.name = name;
    this.dirPath = dirPath;
    this.cards = cards;
  }

  getFile(fileName) {
    return this.dirPath + fileName;
  }

  getMixCard() {
    let dupCardSet = this.cards.concat(this.cards);
    const length = dupCardSet.length;

    for (let i = 0; i < length; i++) {
      //rand between 0-19 dupCardSet.length
      let randPosition = Math.floor(Math.random() * length);

      //swap
      let temp = dupCardSet[randPosition];
      dupCardSet.splice(randPosition, 1, dupCardSet[i]);
      dupCardSet.splice(i, 1, temp);
    }

    return dupCardSet;
  }
}

class Card {
  constructor(id, fileName) {
    this.id = id;
    this.fileName = fileName;
  }
}

const cards = {
  animals: new CardSet("Animals", "./img/card/animal/", [
    new Card(1, "ca1.jpg"),
    new Card(2, "ca2.jpg"),
    new Card(3, "ca3.jpg"),
    new Card(4, "ca4.jpg"),
    new Card(5, "ca5.jpg"),
    new Card(6, "ca6.jpg"),
    new Card(7, "ca7.jpg"),
    new Card(8, "ca8.jpg"),
    new Card(9, "ca9.jpg"),
    new Card(10, "ca10.jpg")
  ]),
  food: new CardSet("Food", "./img/card/food/", [
    new Card(1, "ca1.jpg"),
    new Card(2, "ca2.jpg"),
    new Card(3, "ca3.jpg"),
    new Card(4, "ca4.jpg"),
    new Card(5, "ca5.jpg"),
    new Card(6, "ca6.jpg"),
    new Card(7, "ca7.jpg"),
    new Card(8, "ca8.jpg"),
    new Card(9, "ca9.jpg"),
    new Card(10, "ca10.jpg")
  ]),
  cars: new CardSet("Cars", "./img/card/car/", [
    new Card(1, "ca1.jpg"),
    new Card(2, "ca2.jpg"),
    new Card(3, "ca3.jpg"),
    new Card(4, "ca4.jpg"),
    new Card(5, "ca5.jpg"),
    new Card(6, "ca6.jpg"),
    new Card(7, "ca7.jpg"),
    new Card(8, "ca8.jpg"),
    new Card(9, "ca9.jpg"),
    new Card(10, "ca10.jpg")
  ])
};

let firstCard;
let isFirstCard = true;
let isBoardClickable = true;

function onClickCard(e) {
  if (!isBoardClickable) return;
  if ($(this).attr("solve") == "true") return;

  $(this).css("background-image", `url(${$(this).attr("image-data")})`);

  if (isFirstCard) {
    firstCard = $(this);
    isFirstCard = false;
    return;
  } else {
    isFirstCard = true;
  }

  if ($(this).attr("id") === $(firstCard).attr("id")) {
    $(this).attr("solve", "true");
    $(firstCard).attr("solve", "true");
  } else {
    isBoardClickable = false;
    setTimeout(() => {
      $(this).css("background-image", `url(${currentTheme.backCard})`);
      $(firstCard).css("background-image", `url(${currentTheme.backCard})`);
      isBoardClickable = true;
    }, 1000);
  }
}

$(document).ready(function() {
  let cardSet = cards["animals"];

  $("#dd-CardSheet-menu a").click(function(e) {
    cardSet = cards[`${$(this).attr("id")}`];
    $("#dd-CardSheet-btn").text($(this).text());
    buildBoard(cardSet);
  });

  buildBoard(cardSet);
});

function buildBoard(cardSet) {
  let boardCard = cardSet.getMixCard();
  $("#board").empty();

  boardCard.forEach(card => {
    let cardElement = $(`<div class="col-1 card-item" id="${card.id}"></div>`)
      .attr("image-data", `${cardSet.dirPath}${card.fileName}`)
      .css("background-image", `url(${currentTheme.backCard})`)
      .click(onClickCard);

    $("#board").append(cardElement);
  });
}
